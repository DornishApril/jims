"""
Hybrid Energy System Simulation Function
Based on NSGA-II Optimization Algorithm

CORRECTED VERSION with proper unit conversions and cost calculations
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
    
    UNIT CONVENTIONS:
    - Power: kW (kilowatts)
    - Energy: kWh (kilowatt-hours)
    - Hydrogen mass: kg (kilograms)
    - Time: hours
    - Currency: USD ($)
    """
    
    def __init__(self, parameters: Dict):
        """
        Initialize system parameters
        
        Parameters
        ----------
        parameters : dict
            Dictionary containing all system parameters:
            
            EFFICIENCY PARAMETERS:
            - eta_PV: PV panel efficiency (dimensionless, 0-1)
                     Default: 0.15 (15% conversion of solar to electrical)
            - eta_FC: Fuel cell electrical efficiency (dimensionless, 0-1)
                     Default: 0.50 (50% of H2 energy to electricity)
            - eta_EL: Electrolyzer efficiency (dimensionless, 0-1)
                     Default: 0.70 (70% of electrical energy to H2)
            
            CAPITAL COSTS (one-time investment):
            - c_PV: PV capital cost ($/kW)
            - c_WT: Wind turbine capital cost ($/kW)
            - c_H2: Hydrogen storage capital cost ($/kg capacity)
            - c_FC_cap: Fuel cell capital cost ($/kW)
            - c_EL_cap: Electrolyzer capital cost ($/kW)
            - c_DG_cap: Diesel generator capital cost ($/kW)
            
            OPERATING COSTS (per kWh of energy produced/consumed):
            - c_FC: Fuel cell operating cost ($/kWh produced)
            - c_DG: Diesel fuel cost ($/kWh produced)
            - c_EL: Electrolyzer operating cost ($/kWh consumed)
            
            OPERATION & MAINTENANCE COSTS (annual, per unit capacity):
            - om_PV: PV O&M cost ($/kW/year)
            - om_WT: Wind turbine O&M cost ($/kW/year)
            - om_H2: Hydrogen storage O&M cost ($/kg/year)
            - om_FC: Fuel cell O&M cost ($/kW/year)
            - om_EL: Electrolyzer O&M cost ($/kW/year)
            - om_DG: Diesel generator O&M cost ($/kW/year)
            
            EMISSION FACTORS (kg CO2 per kWh):
            - e_FC: Fuel cell emissions (kg CO2/kWh)
                   Default: 0.0 (assuming green H2)
            - e_DG: Diesel generator emissions (kg CO2/kWh)
                   Default: 0.8
            - e_EL: Electrolyzer emissions (kg CO2/kWh)
                   Default: 0.0 (direct emissions)
            
            ECONOMIC PARAMETERS:
            - T_life: Project lifetime (years)
            - r: Discount rate (dimensionless, e.g., 0.05 = 5%)
            - p_grid: Grid selling price ($/kWh)
            
            TECHNICAL PARAMETERS:
            - A_PV: PV area per kW capacity (m²/kW)
                   For eta_PV = 0.15: A_PV = 1000W/m² / (0.15 * 1000W/kW) = 6.67 m²/kW
            - P_DG_min: Minimum diesel generator load ratio (0-1)
                       Default: 0.3 (must run at ≥30% of rated capacity)
            - H2_LHV: Lower heating value of hydrogen (kWh/kg)
                     Default: 33.3 kWh/kg (thermodynamic constant)
            
            COMPONENT LIFETIMES (years):
            - life_PV, life_WT, life_H2, life_FC, life_EL, life_DG
        """
        # =================================================================
        # EFFICIENCY PARAMETERS
        # =================================================================
        self.eta_PV = parameters.get('eta_PV', 0.15)  # PV efficiency (fraction)
        self.eta_FC = parameters.get('eta_FC', 0.50)  # Fuel cell efficiency (fraction)
        self.eta_EL = parameters.get('eta_EL', 0.70)  # Electrolyzer efficiency (fraction)
        
        # Hydrogen energy content (thermodynamic constant)
        self.H2_LHV = parameters.get('H2_LHV', 33.3)  # kWh/kg (Lower Heating Value)
        
        # =================================================================
        # CAPITAL COSTS ($/unit)
        # =================================================================
        self.c_PV = parameters.get('c_PV', 1500)      # $/kW
        self.c_WT = parameters.get('c_WT', 3000)      # $/kW
        self.c_H2 = parameters.get('c_H2', 500)       # $/kg capacity
        self.c_FC_cap = parameters.get('c_FC_cap', 2000)  # $/kW
        self.c_EL_cap = parameters.get('c_EL_cap', 1500)  # $/kW
        self.c_DG_cap = parameters.get('c_DG_cap', 400)   # $/kW
        
        # =================================================================
        # OPERATING COSTS ($/kWh)
        # =================================================================
        self.c_FC = parameters.get('c_FC', 0.01)  # $/kWh produced
        self.c_DG = parameters.get('c_DG', 0.30)  # $/kWh produced (diesel fuel)
        self.c_EL = parameters.get('c_EL', 0.01)  # $/kWh consumed
        
        # =================================================================
        # O&M COSTS ($/unit/year)
        # =================================================================
        self.om_PV = parameters.get('om_PV', 20)  # $/kW/year
        self.om_WT = parameters.get('om_WT', 50)  # $/kW/year
        self.om_H2 = parameters.get('om_H2', 10)  # $/kg/year
        self.om_FC = parameters.get('om_FC', 30)  # $/kW/year
        self.om_EL = parameters.get('om_EL', 25)  # $/kW/year
        self.om_DG = parameters.get('om_DG', 15)  # $/kW/year
        
        # =================================================================
        # EMISSION FACTORS (kg CO2/kWh)
        # =================================================================
        self.e_FC = parameters.get('e_FC', 0.0)   # Assuming H2 from renewables
        self.e_DG = parameters.get('e_DG', 0.8)   # Diesel emissions
        self.e_EL = parameters.get('e_EL', 0.0)   # Electrolyzer direct emissions
        
        # =================================================================
        # ECONOMIC PARAMETERS
        # =================================================================
        self.T_life = parameters.get('T_life', 20)    # Project lifetime (years)
        self.r = parameters.get('r', 0.05)            # Discount rate
        self.p_grid = parameters.get('p_grid', 0.08)  # Grid selling price ($/kWh)
        
        # =================================================================
        # TECHNICAL PARAMETERS
        # =================================================================
        self.A_PV = parameters.get('A_PV', 6.67)      # PV area per kW (m²/kW)
        self.P_DG_min = parameters.get('P_DG_min', 0.3)  # Minimum DG load ratio
        
        # =================================================================
        # COMPONENT LIFETIMES (years)
        # =================================================================
        self.life_PV = parameters.get('life_PV', 25)
        self.life_WT = parameters.get('life_WT', 20)
        self.life_H2 = parameters.get('life_H2', 20)
        self.life_FC = parameters.get('life_FC', 10)
        self.life_EL = parameters.get('life_EL', 15)
        self.life_DG = parameters.get('life_DG', 15)
    
    
    def wind_power_curve(self, v: float, rated_power: float = 1.0) -> float:
        """
        Calculate wind turbine power output based on wind speed
        Using a simplified power curve model
        
        Parameters
        ----------
        v : float
            Wind speed (m/s)
        rated_power : float
            Rated power of wind turbine (kW)
            Default: 1.0 kW (for per-kW calculations)
            
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
            # Cubic relationship between cut-in and rated
            return rated_power * ((v - v_cut_in) / (v_rated - v_cut_in)) ** 3
        else:  # v_rated <= v <= v_cut_out
            return rated_power
    
    
    def calculate_replacement_cost(self, system: Dict, T_life: int, r: float) -> float:
        """
        Calculate replacement costs for components with lifetime < project lifetime
        Returns the NET PRESENT VALUE of all future replacement costs
        
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
            Total replacement cost in present value ($)
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
            
            if capacity == 0 or life >= T_life:
                continue
            
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
    
    
    def simulate_year(self, system: Dict, data: pd.DataFrame) -> Tuple[float, float, float, Dict]:
        """
        Simulate one year of system operation
        
        Parameters
        ----------
        system : dict
            System configuration containing:
            - N_PV: PV capacity (kW)
            - N_WT: Wind turbine rated capacity (kW)
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
        Tuple[float, float, float, Dict]
            C_total: Total annualized cost ($/year)
            E_total: Total annual emissions (kg CO2/year)
            LPSP: Loss of power supply probability (0-1)
            details: Dictionary with detailed results
        """
        # =================================================================
        # EXTRACT SYSTEM CONFIGURATION
        # =================================================================
        N_PV = system.get('N_PV', 0)
        N_WT = system.get('N_WT', 0)
        Cap_H2 = system.get('Cap_H2', 0)
        Cap_FC = system.get('Cap_FC', 0)
        Cap_EL = system.get('Cap_EL', 0)
        Cap_DG = system.get('Cap_DG', 0)
        
        # Validate inputs
        if Cap_H2 < 0 or Cap_FC < 0 or Cap_EL < 0:
            raise ValueError("Capacities cannot be negative")
        
        # =================================================================
        # HYDROGEN STORAGE LIMITS
        # =================================================================
        H_max = Cap_H2  # Maximum hydrogen storage (kg)
        H_min = 0.1 * Cap_H2  # Minimum hydrogen level (10% of capacity)
        
        # =================================================================
        # INITIALIZE TRACKING VARIABLES
        # =================================================================
        C_op = 0.0       # Operating cost ($)
        E_CO2 = 0.0      # CO2 emissions (kg)
        E_unmet = 0.0    # Unmet energy (kWh)
        E_grid = 0.0     # Energy sold to grid (kWh)
        
        E_PV_total = 0.0
        E_WT_total = 0.0
        E_FC_total = 0.0
        E_EL_total = 0.0
        E_DG_total = 0.0
        
        # Initialize hydrogen storage trajectory
        H = np.zeros(len(data) + 1)
        H[0] = 0.5 * Cap_H2  # Start at 50% capacity
        
        # =================================================================
        # DETECT COLUMN NAMES
        # =================================================================
        if 'Solar Irradiance (W/sq.m)' in data.columns:
            irrad_col = 'Solar Irradiance (W/sq.m)'
        elif 'Avg Solar Irradiance' in data.columns:
            irrad_col = 'Avg Solar Irradiance'
        else:
            raise ValueError("Solar irradiance column not found in data")
        
        if 'Wind Speed (m/s)' in data.columns:
            wind_col = 'Wind Speed (m/s)'
        elif 'Avg Wind Speed' in data.columns:
            wind_col = 'Avg Wind Speed'
        else:
            raise ValueError("Wind speed column not found in data")
        
        # =================================================================
        # CALCULATE TOTAL LOAD
        # =================================================================
        L = data['Community Load'].values.copy()
        if 'RO Load (kWh)' in data.columns:
            L = L + data['RO Load (kWh)'].values
        
        L_year = np.sum(L)  # Total annual load (kWh)
        
        # =================================================================
        # HOURLY SIMULATION LOOP
        # =================================================================
        for t in range(len(data)):
            # Get hourly inputs
            I_t = data.iloc[t][irrad_col] / 1000.0  # Convert W/m² to kW/m²
            v_t = data.iloc[t][wind_col]            # Wind speed (m/s)
            L_t = L[t]                               # Load (kWh for this hour)
            
            # ---------------------------------------------------------
            # RENEWABLE ENERGY GENERATION
            # ---------------------------------------------------------
            # PV generation: Power = efficiency × area × irradiance × capacity
            E_PV = self.eta_PV * self.A_PV * I_t * N_PV  # kWh
            
            # Wind generation: Power = power_curve(wind_speed) × capacity
            E_WT = self.wind_power_curve(v_t, rated_power=1.0) * N_WT  # kWh
            
            E_RE = E_PV + E_WT  # Total renewable energy (kWh)
            
            E_PV_total += E_PV
            E_WT_total += E_WT
            
            # ---------------------------------------------------------
            # NET POWER BALANCE
            # ---------------------------------------------------------
            E_net = E_RE - L_t  # Positive = surplus, Negative = deficit
            
            # =============================================================
            # CASE 1: DEFICIT (E_net < 0)
            # =============================================================
            if E_net < 0:
                E_deficit = abs(E_net)  # kWh needed
                E_FC = 0.0
                E_DG = 0.0
                
                # ---------------------------------------------------------
                # STEP 1: TRY FUEL CELL FIRST
                # ---------------------------------------------------------
                if H[t] > H_min and Cap_FC > 0:
                    # -------------------------------------------------
                    # FUEL CELL OPERATION
                    # -------------------------------------------------
                    # Maximum H2 available for use (kg)
                    H2_available = H[t] - H_min
                    
                    # Maximum energy from available H2 (kWh)
                    # Energy = H2_mass × LHV × efficiency
                    E_FC_max_from_H2 = H2_available * self.H2_LHV * self.eta_FC
                    
                    # Maximum energy from FC capacity (kWh in 1 hour)
                    E_FC_max_from_cap = Cap_FC * 1.0  # kW × 1 hour
                    
                    # Actual FC limit is minimum of both constraints
                    E_FC_max = min(E_FC_max_from_H2, E_FC_max_from_cap)
                    
                    # FC produces what it can (up to deficit)
                    E_FC = min(E_deficit, E_FC_max)
                    
                    # H2 consumed (kg)
                    # H2_consumed = Energy / (LHV × efficiency)
                    H2_consumed = E_FC / (self.H2_LHV * self.eta_FC)
                    
                    # Update hydrogen storage
                    H[t+1] = max(0, H[t] - H2_consumed)
                    
                    # Add costs and emissions
                    C_op += self.c_FC * E_FC
                    E_CO2 += self.e_FC * E_FC
                    E_FC_total += E_FC
                    
                    # Update remaining deficit
                    E_deficit = E_deficit - E_FC
                else:
                    # No fuel cell available, keep current H2 level
                    H[t+1] = H[t]
                
                # ---------------------------------------------------------
                # STEP 2: IF STILL DEFICIT, TRY DIESEL GENERATOR
                # ---------------------------------------------------------
                if E_deficit > 0.001 and Cap_DG > 0:  # Small tolerance
                    # -------------------------------------------------
                    # DIESEL GENERATOR OPERATION
                    # -------------------------------------------------
                    # Diesel generator must run above minimum load
                    P_DG_min_abs = self.P_DG_min * Cap_DG  # Minimum power (kW)
                    
                    # Check if deficit is within operable range
                    if E_deficit >= P_DG_min_abs:
                        # DG can operate
                        E_DG = min(E_deficit, Cap_DG)  # Limited by capacity
                        #We can choose to run the DG several times to minimize deficit
                        #As long as we are being above the minimum so if deficit is 5c and capacity is c
                        #we run DG 5 times. If deficit is 5c+k, then unmet load is k
                        
                        # Add costs and emissions
                        C_op += self.c_DG * E_DG
                        E_CO2 += self.e_DG * E_DG
                        E_DG_total += E_DG
                        
                        # Update remaining deficit
                        E_deficit = E_deficit - E_DG
                    # else: deficit too small for DG minimum load, remains unmet
                
                # ---------------------------------------------------------
                # STEP 3: ANY REMAINING DEFICIT IS UNMET LOAD
                # ---------------------------------------------------------
                if E_deficit > 0.001:  # Small tolerance
                    E_unmet += E_deficit
            
            # =============================================================
            # CASE 2: SURPLUS (E_net > 0)
            # =============================================================
            elif E_net > 0:
                E_surplus = E_net  # kWh available
                
                # Check if storage has space and electrolyzer exists
                if H[t] < H_max and Cap_EL > 0:
                    # -------------------------------------------------
                    # ELECTROLYZER OPERATION
                    # -------------------------------------------------
                    # Available storage space (kg)
                    H2_space = H_max - H[t]
                    
                    # Maximum energy that can be converted to H2 based on storage space
                    # Energy = H2_mass / (efficiency / LHV)
                    # H2_produced = Energy × efficiency / LHV
                    # So: Energy_max = H2_space × LHV / efficiency
                    E_EL_max_from_storage = H2_space * self.H2_LHV / self.eta_EL
                    
                    # Maximum energy from EL capacity (kWh in 1 hour)
                    E_EL_max_from_cap = Cap_EL * 1.0  # kW × 1 hour
                    
                    # Actual EL limit is minimum of all constraints
                    E_EL_max = min(E_surplus, E_EL_max_from_storage, E_EL_max_from_cap)
                    
                    # EL consumes what it can
                    E_EL = E_EL_max
                    
                    # H2 produced (kg)
                    # H2_produced = Energy × efficiency / LHV
                    H2_produced = E_EL * self.eta_EL / self.H2_LHV
                    
                    # Update hydrogen storage
                    H[t+1] = min(H_max, H[t] + H2_produced)
                    
                    # Add costs and emissions
                    C_op += self.c_EL * E_EL
                    E_CO2 += self.e_EL * E_EL
                    E_EL_total += E_EL
                    
                    # Remaining surplus after electrolysis
                    E_leftover = E_surplus - E_EL
                    
                    if E_leftover > 0.001:  # Small tolerance
                        # Sell leftover to grid
                        E_grid += E_leftover
                        C_op -= self.p_grid * E_leftover  # Revenue (negative cost)
                else:
                    # Storage is full or no electrolyzer, sell all surplus to grid
                    H[t+1] = H[t]
                    E_grid += E_surplus
                    C_op -= self.p_grid * E_surplus  # Revenue (negative cost)
            
            # =============================================================
            # CASE 3: BALANCED (E_net == 0)
            # =============================================================
            else:
                H[t+1] = H[t]
        
        # =================================================================
        # CALCULATE PERFORMANCE METRICS
        # =================================================================
        # Loss of Power Supply Probability
        LPSP = E_unmet / L_year if L_year > 0 else 0.0
        
        # =================================================================
        # CALCULATE COSTS
        # =================================================================
        # Capital cost (present value)
        C_cap = (self.c_PV * N_PV + 
                 self.c_WT * N_WT + 
                 self.c_H2 * Cap_H2 + 
                 self.c_FC_cap * Cap_FC + 
                 self.c_EL_cap * Cap_EL + 
                 self.c_DG_cap * Cap_DG)
        
        # Annual O&M cost
        C_om_annual = (self.om_PV * N_PV + 
                       self.om_WT * N_WT + 
                       self.om_H2 * Cap_H2 + 
                       self.om_FC * Cap_FC + 
                       self.om_EL * Cap_EL + 
                       self.om_DG * Cap_DG)
        
        # Replacement cost (present value)
        C_rep = self.calculate_replacement_cost(system, self.T_life, self.r)
        
        # Capital Recovery Factor (CRF)
        # Converts present value to equivalent annual cost
        if self.r > 0:
            CRF = (self.r * (1 + self.r) ** self.T_life) / ((1 + self.r) ** self.T_life - 1)
        else:
            CRF = 1.0 / self.T_life
        
        # Total annualized cost
        # = Annualized capital + Annualized replacement + Annual O&M + Annual operating
        C_total = (C_cap + C_rep) * CRF + C_om_annual + C_op
        
        # Total emissions
        E_total = E_CO2
        
        # =================================================================
        # PREPARE DETAILED RESULTS
        # =================================================================
        details = {
            'C_cap': C_cap,
            'C_rep': C_rep,
            'C_om_annual': C_om_annual,
            'C_op': C_op,
            'CRF': CRF,
            'E_PV_total': E_PV_total,
            'E_WT_total': E_WT_total,
            'E_FC_total': E_FC_total,
            'E_EL_total': E_EL_total,
            'E_DG_total': E_DG_total,
            'E_grid': E_grid,
            'E_unmet': E_unmet,
            'L_year': L_year,
            'H_trajectory': H,
        }
        
        return C_total, E_total, LPSP, details


def example_usage():
    """
    Example of how to use the corrected simulation
    """
    print("="*80)
    print("CORRECTED HYBRID ENERGY SYSTEM SIMULATION")
    print("="*80)
    
    # Define system parameters
    parameters = {
        # Efficiencies (all dimensionless, 0-1)
        'eta_PV': 0.15,    # 15% solar panel efficiency
        'eta_FC': 0.50,    # 50% fuel cell efficiency
        'eta_EL': 0.70,    # 70% electrolyzer efficiency
        
        # Hydrogen properties
        'H2_LHV': 33.3,    # kWh/kg (thermodynamic constant)
        
        # Capital costs
        'c_PV': 1500,      # $/kW
        'c_WT': 3000,      # $/kW
        'c_H2': 500,       # $/kg
        'c_FC_cap': 2000,  # $/kW
        'c_EL_cap': 1500,  # $/kW
        'c_DG_cap': 400,   # $/kW
        
        # Operating costs
        'c_FC': 0.01,      # $/kWh
        'c_DG': 0.30,      # $/kWh
        'c_EL': 0.01,      # $/kWh
        
        # O&M costs
        'om_PV': 20,       # $/kW/year
        'om_WT': 50,       # $/kW/year
        'om_H2': 10,       # $/kg/year
        'om_FC': 30,       # $/kW/year
        'om_EL': 25,       # $/kW/year
        'om_DG': 15,       # $/kW/year
        
        # Emissions
        'e_FC': 0.0,       # kg CO2/kWh
        'e_DG': 0.8,       # kg CO2/kWh
        'e_EL': 0.0,       # kg CO2/kWh
        
        # Economic
        'T_life': 20,      # years
        'r': 0.05,         # 5% discount rate
        'p_grid': 0.08,    # $/kWh
        
        # Technical
        'A_PV': 6.67,      # m²/kW
        'P_DG_min': 0.3,   # 30% minimum load
        
        # Lifetimes
        'life_PV': 25,
        'life_WT': 20,
        'life_H2': 20,
        'life_FC': 10,
        'life_EL': 15,
        'life_DG': 15,
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
    
    print("\nCORRECTED UNIT CONVERSIONS:")
    print(f"  Fuel Cell: {parameters['eta_FC']*100}% efficient")
    print(f"    - H2 LHV: {parameters['H2_LHV']} kWh/kg")
    print(f"    - Effective: {parameters['eta_FC']*parameters['H2_LHV']:.1f} kWh electrical per kg H2")
    print(f"  Electrolyzer: {parameters['eta_EL']*100}% efficient")
    print(f"    - Requires: {parameters['H2_LHV']/parameters['eta_EL']:.1f} kWh to produce 1 kg H2")
    
    print("\nTo use:")
    print("  system = HybridEnergySystem(parameters)")
    print("  C_total, E_total, LPSP, details = system.simulate_year(config, data)")
    
    return system, config


if __name__ == "__main__":
    system, config = example_usage()