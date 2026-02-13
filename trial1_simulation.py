"""
Hybrid Energy System Simulation Function
Based on NSGA-II Optimization Algorithm
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, List


class HybridEnergySystem:
    """
    Simulates a hybrid renewable energy system with:
    - Photovoltaic (PV) panels
    - Wind Turbines (WT)
    - Hydrogen Storage (H2)
    - Fuel Cell (FC)
    - Electrolyzer (EL)
    - Diesel Generator (DG)
    """
    
    def __init__(self, parameters: Dict):
        """
        Initialize system parameters
        
        Parameters
        ----------
        parameters : dict
            Dictionary containing all system parameters including:
            - Efficiencies (eta_PV, eta_FC, eta_EL)
            - Costs (c_PV, c_WT, c_H2, c_FC_cap, c_EL_cap, c_DG_cap)
            - Operating costs (c_FC, c_DG, c_EL)
            - O&M costs (om_PV, om_WT, om_H2, om_FC, om_EL, om_DG)
            - Emission factors (e_FC, e_DG, e_EL)
            - Other parameters (T_life, r, p_grid, P_DG_min, etc.)
        """
        # Efficiencies
        self.eta_PV = parameters.get('eta_PV', 0.15)  # PV efficiency
        self.eta_FC = parameters.get('eta_FC', 0.50)  # Fuel cell efficiency (kWh per kg H2)
        self.eta_EL = parameters.get('eta_EL', 0.70)  # Electrolyzer efficiency (kg H2 per kWh)
        
        # Capital costs ($/unit)
        self.c_PV = parameters.get('c_PV', 1500)      # $/kW
        self.c_WT = parameters.get('c_WT', 3000)      # $/kW
        self.c_H2 = parameters.get('c_H2', 500)       # $/kg capacity
        self.c_FC_cap = parameters.get('c_FC_cap', 2000)  # $/kW
        self.c_EL_cap = parameters.get('c_EL_cap', 1500)  # $/kW
        self.c_DG_cap = parameters.get('c_DG_cap', 400)   # $/kW
        
        # Operating costs ($/kWh)
        self.c_FC = parameters.get('c_FC', 0.01)
        self.c_DG = parameters.get('c_DG', 0.30)
        self.c_EL = parameters.get('c_EL', 0.01)
        
        # O&M costs ($/unit/year)
        self.om_PV = parameters.get('om_PV', 20)
        self.om_WT = parameters.get('om_WT', 50)
        self.om_H2 = parameters.get('om_H2', 10)
        self.om_FC = parameters.get('om_FC', 30)
        self.om_EL = parameters.get('om_EL', 25)
        self.om_DG = parameters.get('om_DG', 15)
        
        # Emission factors (kg CO2/kWh)
        self.e_FC = parameters.get('e_FC', 0.0)   # Assuming H2 from renewables
        self.e_DG = parameters.get('e_DG', 0.8)   # Diesel emissions
        self.e_EL = parameters.get('e_EL', 0.0)   # Electrolyzer emissions
        
        # Economic parameters
        self.T_life = parameters.get('T_life', 20)  # Project lifetime (years)
        self.r = parameters.get('r', 0.05)          # Discount rate
        self.p_grid = parameters.get('p_grid', 0.08)  # Grid selling price ($/kWh)
        
        # Technical parameters
        self.A_PV = parameters.get('A_PV', 1.0)     # PV area per unit (m²/kW)
        self.P_DG_min = parameters.get('P_DG_min', 0.3)  # Minimum DG load ratio
        
        # Component lifetimes (years)
        self.life_PV = parameters.get('life_PV', 25)
        self.life_WT = parameters.get('life_WT', 20)
        self.life_H2 = parameters.get('life_H2', 20)
        self.life_FC = parameters.get('life_FC', 10)
        self.life_EL = parameters.get('life_EL', 15)
        self.life_DG = parameters.get('life_DG', 15)
        
    
    def wind_power_curve(self, v: float, rated_power: float = 20.0) -> float:
        """
        Calculate wind turbine power output based on wind speed
        Using a simplified power curve model
        
        Parameters
        ----------
        v : float
            Wind speed (m/s)
        rated_power : float
            Rated power of wind turbine (kW)
            
        Returns
        -------
        float
            Power output (kW)
        """
        v_cut_in = 3.0   # Cut-in wind speed (m/s)
        v_rated = 12.0   # Rated wind speed (m/s)
        v_cut_out = 25.0 # Cut-out wind speed (m/s)
        
        if v < v_cut_in or v > v_cut_out:
            return 0.0
        elif v >= v_cut_in and v < v_rated:
            # Linear interpolation between cut-in and rated
            return rated_power * ((v - v_cut_in) / (v_rated - v_cut_in)) ** 3
        else:  # v_rated <= v <= v_cut_out
            return rated_power
    
    
    def calculate_replacement_cost(self, system: Dict, T_life: int, r: float) -> float:
        """
        Calculate replacement costs for components with lifetime < project lifetime
        
        Parameters
        ----------
        system : dict
            System configuration with capacities
        T_life : int
            Project lifetime (years)
        r : float
            Discount rate
            
        Returns
        -------
        float
            Total replacement cost ($)
        """
        C_rep = 0.0
        
        components = [
            ('N_PV', self.c_PV, self.life_PV),
            ('N_WT', self.c_WT, self.life_WT),
            ('Cap_H2', self.c_H2, self.life_H2),
            ('Cap_FC', self.c_FC_cap, self.life_FC),
            ('Cap_EL', self.c_EL_cap, self.life_EL),
            ('Cap_DG', self.c_DG_cap, self.life_DG),
        ]
        
        for comp_name, unit_cost, life in components:
            capacity = system.get(comp_name, 0)
            
            # Calculate number of replacements needed
            n_replacements = int(T_life / life)
            
            # Add discounted replacement costs
            for n in range(1, n_replacements + 1):
                replacement_year = n * life
                if replacement_year < T_life:
                    # Present value of replacement cost
                    pv_cost = (capacity * unit_cost) / ((1 + r) ** replacement_year)
                    C_rep += pv_cost
        
        return C_rep
    
    
    def simulate_year(self, system: Dict, data: pd.DataFrame) -> Tuple[float, float, float]:
        """
        Simulate one year of system operation
        
        Parameters
        ----------
        system : dict
            System configuration containing:
            - N_PV: Number of PV units (kW)
            - N_WT: Number of wind turbines (kW rated)
            - Cap_H2: Hydrogen storage capacity (kg)
            - Cap_FC: Fuel cell capacity (kW)
            - Cap_EL: Electrolyzer capacity (kW)
            - Cap_DG: Diesel generator capacity (kW)
        
        data : pd.DataFrame
            Hourly data with columns:
            - 'Solar Irradiance (W/sq.m)' or 'Avg Solar Irradiance'
            - 'Wind Speed (m/s)' or 'Avg Wind Speed'
            - 'Community Load' and/or 'RO Load (kWh)'
            
        Returns
        -------
        Tuple[float, float, float]
            C_total: Total annualized cost ($)
            E_total: Total annual emissions (kg CO2)
            LPSP: Loss of power supply probability
        """
        # Extract system configuration
        N_PV = system.get('N_PV', 0)
        N_WT = system.get('N_WT', 0)
        Cap_H2 = system.get('Cap_H2', 0)
        Cap_FC = system.get('Cap_FC', 0)
        Cap_EL = system.get('Cap_EL', 0)
        Cap_DG = system.get('Cap_DG', 0)
        
        # Storage limits
        H_max = Cap_H2  # Maximum hydrogen storage (kg)
        H_min = 0.1 * Cap_H2  # Minimum hydrogen level (10% of capacity)
        
        # Initialize cumulative variables
        C_op = 0.0       # Operating cost ($)
        E_CO2 = 0.0      # CO2 emissions (kg)
        E_unmet = 0.0    # Unmet energy (kWh)
        E_grid = 0.0     # Energy sold to grid (kWh)
        
        # Initialize hydrogen storage
        H = np.zeros(len(data) + 1)
        H[0] = 0.5 * Cap_H2  # Start at 50% capacity
        
        # Detect column names
        if 'Solar Irradiance (W/sq.m)' in data.columns:
            irrad_col = 'Solar Irradiance (W/sq.m)'
        elif 'Avg Solar Irradiance' in data.columns:
            irrad_col = 'Avg Solar Irradiance'
        else:
            raise ValueError("Solar irradiance column not found")
        
        if 'Wind Speed (m/s)' in data.columns:
            wind_col = 'Wind Speed (m/s)'
        elif 'Avg Wind Speed' in data.columns:
            wind_col = 'Avg Wind Speed'
        else:
            raise ValueError("Wind speed column not found")
        
        # Calculate total load
        L = data['Community Load'].values
        if 'RO Load (kWh)' in data.columns:
            L = L + data['RO Load (kWh)'].values
        
        L_year = np.sum(L)
        
        # Hourly simulation loop
        for t in range(len(data)):
            # Get hourly inputs
            I_t = data.iloc[t][irrad_col] / 1000.0  # Convert W/m² to kW/m²
            v_t = data.iloc[t][wind_col]
            L_t = L[t]
            
            # Calculate renewable energy generation
            E_PV = self.eta_PV * self.A_PV * I_t * N_PV
            E_WT = self.wind_power_curve(v_t, rated_power=1.0) * N_WT
            E_RE = E_PV + E_WT
            
            # Net power
            E_net = E_RE - L_t
            
            # CASE 1: DEFICIT (E_net < 0)
            if E_net < 0:
                E_deficit = abs(E_net)
                
                # Try to use fuel cell
                if H[t] > H_min:
                    # Maximum FC power limited by hydrogen availability and capacity
                    P_FC_limit = min(H[t] * self.eta_FC, Cap_FC)
                    
                    if E_deficit <= P_FC_limit:
                        # FC can cover entire deficit
                        E_FC = E_deficit
                        H_consumed = E_FC / self.eta_FC
                        H[t+1] = H[t] - H_consumed
                        
                        C_op += self.c_FC * E_FC
                        E_CO2 += self.e_FC * E_FC
                    
                    else:
                        # FC runs at maximum, need additional source
                        E_FC = P_FC_limit
                        H_consumed = E_FC / self.eta_FC
                        E_remaining = E_deficit - E_FC
                        
                        # Try diesel generator
                        P_DG_min_abs = self.P_DG_min * Cap_DG
                        if E_remaining >= P_DG_min_abs and E_remaining <= Cap_DG:
                            # DG can operate within limits
                            E_DG = E_remaining
                            H[t+1] = H[t] - H_consumed
                            
                            C_op += self.c_FC * E_FC + self.c_DG * E_DG
                            E_CO2 += self.e_FC * E_FC + self.e_DG * E_DG
                            
                            # Check if DG produces excess
                            E_total_gen = E_RE + E_FC + E_DG
                            E_excess = E_total_gen - L_t
                            
                            if E_excess > 0:
                                # Sell excess to grid
                                E_grid += E_excess
                                C_op -= self.p_grid * E_excess
                            else:
                                # Still have unmet load (shouldn't happen in this logic)
                                E_unmet += abs(E_excess)
                        
                        else:
                            # DG cannot operate or doesn't meet demand
                            H[t+1] = H[t] - H_consumed
                            E_unmet += E_remaining
                            
                            C_op += self.c_FC * E_FC
                            E_CO2 += self.e_FC * E_FC
                
                else:
                    # No hydrogen available, try diesel generator
                    H[t+1] = H[t]
                    
                    # Check if diesel generator can operate within limits
                    P_DG_min_abs = self.P_DG_min * Cap_DG
                    if E_deficit >= P_DG_min_abs and E_deficit <= Cap_DG:
                        # DG can operate and meet demand
                        E_DG = E_deficit
                        C_op += self.c_DG * E_DG
                        E_CO2 += self.e_DG * E_DG
                        
                        # Check if DG produces excess
                        E_total_gen = E_RE + E_DG
                        E_excess = E_total_gen - L_t
                        
                        if E_excess > 0:
                            # Sell excess to grid
                            E_grid += E_excess
                            C_op -= self.p_grid * E_excess
                        else:
                            # Still have unmet load
                            E_unmet += abs(E_excess)
                    else:
                        # DG cannot operate (below minimum or above capacity)
                        E_unmet += E_deficit
            
            # CASE 2: SURPLUS (E_net > 0)
            elif E_net > 0:
                E_surplus = E_net
                
                # Try to store energy as hydrogen
                if H[t] < H_max:
                    H_space = H_max - H[t]
                    
                    # Maximum electrolyzer power limited by surplus, capacity, and storage space
                    E_EL_limit = min(E_surplus, Cap_EL, H_space / self.eta_EL)
                    
                    E_EL = E_EL_limit
                    H_produced = E_EL * self.eta_EL
                    H[t+1] = H[t] + H_produced
                    
                    C_op += self.c_EL * E_EL
                    E_CO2 += self.e_EL * E_EL
                    
                    # Remaining surplus after electrolysis
                    E_leftover = E_surplus - E_EL
                    
                    if E_leftover > 0:
                        # Sell leftover to grid
                        E_grid += E_leftover
                        C_op -= self.p_grid * E_leftover
                
                else:
                    # Storage is full, sell all surplus to grid
                    H[t+1] = H[t]
                    E_grid += E_surplus
                    C_op -= self.p_grid * E_surplus
            
            # CASE 3: BALANCED (E_net == 0)
            else:
                H[t+1] = H[t]
        
        # Calculate LPSP
        LPSP = E_unmet / L_year if L_year > 0 else 0.0
        
        # Calculate costs
        # Capital cost
        C_cap = (self.c_PV * N_PV + 
                 self.c_WT * N_WT + 
                 self.c_H2 * Cap_H2 + 
                 self.c_FC_cap * Cap_FC + 
                 self.c_EL_cap * Cap_EL + 
                 self.c_DG_cap * Cap_DG)
        
        # O&M cost over lifetime
        C_om = ((self.om_PV * N_PV + 
                 self.om_WT * N_WT + 
                 self.om_H2 * Cap_H2 + 
                 self.om_FC * Cap_FC + 
                 self.om_EL * Cap_EL + 
                 self.om_DG * Cap_DG) * self.T_life)
        
        # Replacement cost
        C_rep = self.calculate_replacement_cost(system, self.T_life, self.r)
        
        # Capital Recovery Factor
        CRF = (self.r * (1 + self.r) ** self.T_life) / ((1 + self.r) ** self.T_life - 1)
        
        # Total annualized cost
        C_total = (C_cap + C_rep) * CRF + C_om + C_op
        
        # Total emissions
        E_total = E_CO2
        
        return C_total, E_total, LPSP


def example_usage():
    """
    Example of how to use the simulation
    """
    # Define system parameters
    parameters = {
        'eta_PV': 0.15,
        'eta_FC': 50.0,  # kWh per kg H2 (LHV of H2 ~ 33.3 kWh/kg * efficiency)
        'eta_EL': 0.70,  # kg H2 per kWh
        'c_PV': 1500,
        'c_WT': 3000,
        'c_H2': 500,
        'c_FC_cap': 2000,
        'c_EL_cap': 1500,
        'c_DG_cap': 400,
        'c_FC': 0.01,
        'c_DG': 0.30,
        'c_EL': 0.01,
        'om_PV': 20,
        'om_WT': 50,
        'om_H2': 10,
        'om_FC': 30,
        'om_EL': 25,
        'om_DG': 15,
        'e_FC': 0.0,
        'e_DG': 0.8,
        'e_EL': 0.0,
        'T_life': 20,
        'r': 0.05,
        'p_grid': 0.08,
        'A_PV': 6.67,  # m²/kW for 15% efficiency
        'P_DG_min': 0.3,
    }
    
    # Create system instance
    system = HybridEnergySystem(parameters)
    
    # Example system configuration
    config = {
        'N_PV': 100,      # kW
        'N_WT': 50,       # kW rated
        'Cap_H2': 100,    # kg
        'Cap_FC': 50,     # kW
        'Cap_EL': 50,     # kW
        'Cap_DG': 30,     # kW
    }
    
    # Load data (example)
    # data = pd.read_excel('data/Load.xlsx')
    # C_total, E_total, LPSP = system.simulate_year(config, data)
    
    print("Simulation function created successfully!")
    print("\nUsage:")
    print("  system = HybridEnergySystem(parameters)")
    print("  C_total, E_total, LPSP = system.simulate_year(config, data)")


if __name__ == "__main__":
    example_usage()
