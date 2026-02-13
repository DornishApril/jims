"""
Example Script: Running the Hybrid Energy System Simulation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from trial1_simulation import HybridEnergySystem


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load and prepare hourly data
    
    Parameters
    ----------
    filepath : str
        Path to Excel file containing hourly data
        
    Returns
    -------
    pd.DataFrame
        Prepared data with standardized column names
    """
    data = pd.read_excel(filepath)
    
    # Standardize column names if needed
    column_mapping = {
        'Avg Solar Irradiance': 'Solar Irradiance (W/sq.m)',
        'Avg Wind Speed': 'Wind Speed (m/s)',
    }
    
    data = data.rename(columns=column_mapping)
    
    return data


def run_single_simulation():
    """
    Run a single simulation with a given system configuration
    """
    print("="*80)
    print("HYBRID ENERGY SYSTEM SIMULATION")
    print("="*80)
    
    # Define system parameters
    parameters = {
        # Efficiencies
        'eta_PV': 0.15,           # PV panel efficiency (15%)
        'eta_FC': 16.65,          # Fuel cell efficiency: 50% * 33.3 kWh/kg = 16.65 kWh/kg
        'eta_EL': 0.020,          # Electrolyzer efficiency: 70% / 33.3 = 0.021 kg/kWh
        
        # Capital costs ($/unit)
        'c_PV': 1500,             # $/kW
        'c_WT': 3000,             # $/kW
        'c_H2': 500,              # $/kg storage capacity
        'c_FC_cap': 2000,         # $/kW
        'c_EL_cap': 1500,         # $/kW
        'c_DG_cap': 400,          # $/kW
        
        # Operating costs ($/kWh)
        'c_FC': 0.01,
        'c_DG': 0.30,
        'c_EL': 0.01,
        
        # O&M costs ($/unit/year)
        'om_PV': 20,
        'om_WT': 50,
        'om_H2': 10,
        'om_FC': 30,
        'om_EL': 25,
        'om_DG': 15,
        
        # Emission factors (kg CO2/kWh)
        'e_FC': 0.0,
        'e_DG': 0.8,
        'e_EL': 0.0,
        
        # Economic parameters
        'T_life': 20,
        'r': 0.05,
        'p_grid': 0.08,
        
        # Technical parameters
        'A_PV': 6.67,             # m²/kW for 15% efficiency
        'P_DG_min': 0.3,
        
        # Component lifetimes
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
        'N_PV': 150,      # kW PV capacity
        'N_WT': 100,      # kW WT rated capacity
        'Cap_H2': 200,    # kg H2 storage
        'Cap_FC': 80,     # kW fuel cell
        'Cap_EL': 80,     # kW electrolyzer
        'Cap_DG': 50,     # kW diesel generator
    }
    
    print("\nSystem Configuration:")
    print(f"  PV Capacity:         {config['N_PV']} kW")
    print(f"  Wind Turbine:        {config['N_WT']} kW")
    print(f"  H2 Storage:          {config['Cap_H2']} kg")
    print(f"  Fuel Cell:           {config['Cap_FC']} kW")
    print(f"  Electrolyzer:        {config['Cap_EL']} kW")
    print(f"  Diesel Generator:    {config['Cap_DG']} kW")
    
    # Load hourly data
    # Try to load from either file
    try:
        data = pd.read_excel('data/Load.xlsx')
        print("\nData loaded from: data/Load.xlsx")
    except:
        try:
            data = pd.read_excel('data/combined.xlsx')
            print("\nData loaded from: data/combined.xlsx")
        except:
            print("\nError: Could not load data file!")
            print("Please ensure data/Load.xlsx or data/combined.xlsx exists")
            return
    
    print(f"Data points: {len(data)} hours")
    
    # Run simulation
    print("\nRunning simulation...")
    C_total, E_total, LPSP = system.simulate_year(config, data)
    
    # Display results
    print("\n" + "="*80)
    print("SIMULATION RESULTS")
    print("="*80)
    print(f"\nTotal Annualized Cost:    ${C_total:,.2f} /year")
    print(f"Total Annual Emissions:   {E_total:,.2f} kg CO2/year")
    print(f"Loss of Power Supply:     {LPSP*100:.4f} %")
    print(f"Reliability:              {(1-LPSP)*100:.4f} %")
    
    # Cost breakdown
    C_cap = (parameters['c_PV'] * config['N_PV'] + 
             parameters['c_WT'] * config['N_WT'] + 
             parameters['c_H2'] * config['Cap_H2'] + 
             parameters['c_FC_cap'] * config['Cap_FC'] + 
             parameters['c_EL_cap'] * config['Cap_EL'] + 
             parameters['c_DG_cap'] * config['Cap_DG'])
    
    print(f"\nInitial Capital Cost:     ${C_cap:,.2f}")
    
    # Calculate levelized cost of energy (LCOE)
    L = data['Community Load'].values
    if 'RO Load (kWh)' in data.columns:
        L = L + data['RO Load (kWh)'].values
    L_year = np.sum(L)
    
    LCOE = C_total / L_year
    print(f"Annual Energy Demand:     {L_year:,.2f} kWh/year")
    print(f"Levelized Cost of Energy: ${LCOE:.4f} /kWh")
    
    return C_total, E_total, LPSP, system, config, data


def sensitivity_analysis():
    """
    Perform sensitivity analysis on key parameters
    """
    print("\n" + "="*80)
    print("SENSITIVITY ANALYSIS")
    print("="*80)
    
    # Base parameters
    parameters = {
        'eta_PV': 0.15,
        'eta_FC': 16.65,
        'eta_EL': 0.020,
        'c_PV': 1500, 'c_WT': 3000, 'c_H2': 500,
        'c_FC_cap': 2000, 'c_EL_cap': 1500, 'c_DG_cap': 400,
        'c_FC': 0.01, 'c_DG': 0.30, 'c_EL': 0.01,
        'om_PV': 20, 'om_WT': 50, 'om_H2': 10,
        'om_FC': 30, 'om_EL': 25, 'om_DG': 15,
        'e_FC': 0.0, 'e_DG': 0.8, 'e_EL': 0.0,
        'T_life': 20, 'r': 0.05, 'p_grid': 0.08,
        'A_PV': 6.67, 'P_DG_min': 0.3,
        'life_PV': 25, 'life_WT': 20, 'life_H2': 20,
        'life_FC': 10, 'life_EL': 15, 'life_DG': 15,
    }
    
    # Base configuration
    base_config = {
        'N_PV': 150,
        'N_WT': 100,
        'Cap_H2': 200,
        'Cap_FC': 80,
        'Cap_EL': 80,
        'Cap_DG': 50,
    }
    
    # Load data
    try:
        data = pd.read_excel('data/Load.xlsx')
    except:
        data = pd.read_excel('data/combined.xlsx')
    
    system = HybridEnergySystem(parameters)
    
    # Test different PV capacities
    print("\nTesting different PV capacities:")
    pv_capacities = [50, 100, 150, 200, 250]
    
    results = []
    for pv in pv_capacities:
        config = base_config.copy()
        config['N_PV'] = pv
        C_total, E_total, LPSP = system.simulate_year(config, data)
        results.append((pv, C_total, E_total, LPSP))
        print(f"  PV={pv:3d} kW: Cost=${C_total:10,.0f}, Emissions={E_total:8,.0f} kg, LPSP={LPSP*100:6.3f}%")
    
    return results


if __name__ == "__main__":
    # Run single simulation
    C_total, E_total, LPSP, system, config, data = run_single_simulation()
    
    # Uncomment to run sensitivity analysis
    # sensitivity_results = sensitivity_analysis()
