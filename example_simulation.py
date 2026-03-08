"""
Example Script: Running the CORRECTED Hybrid Energy System Simulation

This script demonstrates the corrected version with proper unit conversions
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from trial1_simulation import HybridEnergySystem


def run_single_simulation(data):

    """


    Run a single simulation with a given system configuration


    """
    print("="*80)
    print("CORRECTED HYBRID ENERGY SYSTEM SIMULATION")
    print("="*80)
    
    # =========================================================================
    # DEFINE CORRECTED SYSTEM PARAMETERS
    # =========================================================================
    parameters = {
    # =================================================================
    # GENERATOR CONFIGS
    # =================================================================
    'rated_PV': 0.327,          # kW - rated power per PV panel
    'v_cut_in': 2.75,           # m/s - cut-in wind speed
    'v_rated': 9.0,             # m/s - rated wind speed
    'rated_power': 25.0,        # kW - wind turbine rated power
    'Cap_H2': 6,                # kg - capacity of 1 H2 storage unit
    'Cap_FC': 2,                # kW - rated power per fuel cell unit
    'Cap_EL': 2,                # kW - rated power per electrolyzer unit
    'Cap_DG': 50,               # kW - rated power per diesel generator unit
    'H_min_percentage': 0,      # fraction - minimum H2 storage level (0 = 0%)
    'H_max_percentage': 0,      # fraction - maximum H2 storage level override

    # =================================================================
    # DIESEL CONSTANTS
    # =================================================================
    'f_0': 0.246,               # litre/kW/h - diesel curve intercept coefficient
    'f_1': 0.08145,             # litre/kWh  - diesel curve slope coefficient

    # =================================================================
    # EFFICIENCY PARAMETERS
    # =================================================================
    'eta_PV': 0.15,             # fraction - PV panel efficiency (15%)
    'eta_FC': 0.50,             # fraction - fuel cell efficiency (50%)
    'eta_EL': 0.70,             # fraction - electrolyzer efficiency (70%)
    'eta_INVT': 0.90,           # fraction - inverter efficiency (90%)
    'H2_LHV': 33.3,             # kWh/kg   - hydrogen lower heating value

    # =================================================================
    # CAPITAL COSTS
    # =================================================================
    'c_PV': 1500,               # $/kW     - PV capital cost
    'c_WT': 3000,               # $/kW     - wind turbine capital cost
    'c_H2': 500,                # $/kg     - hydrogen storage capital cost
    'c_FC_cap': 2000,           # $/kW     - fuel cell capital cost
    'c_EL_cap': 1500,           # $/kW     - electrolyzer capital cost
    'c_DG_cap': 400,            # $/kW     - diesel generator capital cost
    'c_INVT': 300,              # $        - inverter capital cost (flat, not per-kW)

    # =================================================================
    # OPERATING COSTS
    # =================================================================
    'c_FC': 0,                  # $/kWh    - fuel cell operating cost per kWh produced
    'c_DG': 0,                  # $/kWh    - diesel operating cost per kWh produced
    'c_EL': 0,                  # $/kWh    - electrolyzer operating cost per kWh consumed
    'c_DG_FUEL': 0.82,          # $/litre  - diesel fuel cost

    # =================================================================
    # O&M COSTS
    # =================================================================
    'om_PV': 20,                # $/kW/year  - PV O&M
    'om_WT': 50,                # $/kW/year  - wind turbine O&M
    'om_H2': 10,                # $/kg/year  - hydrogen storage O&M
    'om_FC': 30,                # $/kW/year  - fuel cell O&M
    'om_EL': 25,                # $/kW/year  - electrolyzer O&M
    'om_DG': 0.03,              # $/h        - diesel generator O&M (per operating hour)
    'om_INVT': 0,               # $          - inverter O&M

    # =================================================================
    # REPLACEMENT COSTS
    # =================================================================
    'rc_PV': 0,                 # $/kW  - PV replacement cost
    'rc_WT': 1750,              # $/kW  - wind turbine replacement cost
    'rc_H2': 10,                # $/kg  - hydrogen storage replacement cost
    'rc_FC': 30,                # $/kW  - fuel cell replacement cost
    'rc_EL': 25,                # $/kW  - electrolyzer replacement cost
    'rc_DG': 500,               # $/kW  - diesel generator replacement cost
    'rc_INVT': 300,             # $     - inverter replacement cost (flat, per unit)

    # =================================================================
    # EMISSION FACTORS
    # =================================================================
    'e_FC': 0.0,                # kg CO2/kWh    - fuel cell emissions (green H2 = 0)
    'e_DG': 2.6391,             # kg CO2/litre  - diesel generator emissions
    'e_EL': 0.0,                # kg CO2/kWh    - electrolyzer direct emissions

    # =================================================================
    # ECONOMIC PARAMETERS
    # =================================================================
    'T_life': 20,               # years    - project lifetime
    'r': 0.05,                  # fraction - annual discount rate (5%)
    'p_grid': 0.08,             # $/kWh    - grid energy selling price

    # =================================================================
    # TECHNICAL PARAMETERS
    # =================================================================
    'A_PV': 6.67,               # m²/kW   - PV area per kW capacity
    'P_DG_min': 0.3,            # fraction - minimum diesel generator load ratio (30%)

    # =================================================================
    # COMPONENT LIFETIMES
    # =================================================================
    'life_PV': 25,              # years - PV panel lifetime
    'life_WT': 20,              # years - wind turbine lifetime
    'life_H2': 20,              # years - hydrogen storage lifetime
    'life_FC': 10,              # years - fuel cell lifetime
    'life_EL': 15,              # years - electrolyzer lifetime
    'life_DG': 15,              # years - diesel generator lifetime
    'life_INVT': 15,            # years - inverter lifetime
}
    # =========================================================================
    # CREATE SYSTEM INSTANCE
    # =========================================================================
    system = HybridEnergySystem(parameters)
    
    # =========================================================================
    # DEFINE SYSTEM CONFIGURATION
    # =========================================================================
    config = {
        'N_PV': 200,      # number of PV panels
        'N_WT': 10,       # number of wind turbines
        'N_H2': 50,      # number of H2 storage units
        'N_FC': 50,       # number of fuel cell units
        'N_EL': 50,       # number of electrolyzer units
        'N_DG': 5,       # number of diesel generator units
    }

    # Derived capacities for display
    cap_PV  = config['N_PV']  * system.rated_PV     # kW
    cap_WT  = config['N_WT']  * system.rated_power  # kW
    cap_H2  = config['N_H2']  * system.Cap_H2       # kg
    cap_FC  = config['N_FC']  * system.Cap_FC        # kW
    cap_EL  = config['N_EL']  * system.Cap_EL        # kW
    cap_DG  = config['N_DG']  * system.Cap_DG        # kW
    
    print("\n" + "="*80)
    print("SYSTEM CONFIGURATION")
    print("="*80)
    print(f"  PV Capacity: RatedPV {system.rated_PV:>4}kW              {config['N_PV']:>4} panels  ->  {cap_PV:>8.2f} kW")
    print(f"  Wind Turbine Capacity: Rated Power {system.rated_power:>4}kW    {config['N_WT']:>4} turbines ->  {cap_WT:>8.2f} kW")
    print(f"  H2 Storage Capacity: CapH2 {system.Cap_H2:>4}kg      {config['N_H2']:>4} units   ->  {cap_H2:>8.2f} kg")
    print(f"  Fuel Cell Capacity: CapFC {system.Cap_FC:>4}kW       {config['N_FC']:>4} units   ->  {cap_FC:>8.2f} kW")
    print(f"  Electrolyzer Capacity: CapEL {system.Cap_EL:>4}kW    {config['N_EL']:>4} units   ->  {cap_EL:>8.2f} kW")
    print(f"  Diesel Generator: CapDG {system.Cap_DG:>4}kW         {config['N_DG']:>4} units   ->  {cap_DG:>8.2f} kW")
    
    print("\n" + "="*80)
    print("EFFICIENCY DETAILS")
    print("="*80)
    print(f"  PV Efficiency:            {parameters['eta_PV']*100:>6.1f} %")
    print(f"  Fuel Cell Efficiency:     {parameters['eta_FC']*100:>6.1f} %")
    print(f"  Electrolyzer Efficiency:  {parameters['eta_EL']*100:>6.1f} %")
    print(f"  Inverter Efficiency:      {parameters['eta_INVT']*100:>6.1f} %")
    print(f"  H2 Lower Heating Value:   {parameters['H2_LHV']:>6.1f} kWh/kg")
    print()
    print(f"  FC Output:                {parameters['eta_FC']*parameters['H2_LHV']:>6.2f} kWh per kg H2")
    print(f"  EL Input Required:        {parameters['H2_LHV']/parameters['eta_EL']:>6.2f} kWh per kg H2")
    print(f"  Round-trip Efficiency:    {parameters['eta_FC']*parameters['eta_EL']*100:>6.1f} %")
    
    
    print(f"  Data Points:              {len(data):>8} hours")
    print(f"  Represents:               {len(data)/24:>8.1f} days")
    
    # =========================================================================
    # RUN SIMULATION
    # =========================================================================
    print("\n" + "="*80)
    print("RUNNING SIMULATION...")
    print("="*80)
    
    C_total, E_total, LPSP, details = system.simulate_year(config, data)
    
    # =========================================================================
    # DISPLAY RESULTS
    # =========================================================================
    print("\n" + "="*80)
    print("SIMULATION RESULTS")
    print("="*80)
    
    print("\n--- ECONOMIC PERFORMANCE ---")
    print(f"  Total Annualized Cost:    ${C_total:>12,.2f} /year")
    print(f"  Capital Cost:             ${details['C_cap']:>12,.2f}")
    print(f"  Replacement Cost (PV):    ${details['C_rep']:>12,.2f}")
    print(f"  Annual O&M Cost:          ${details['C_om_annual']:>12,.2f} /year")
    print(f"  Annual Operating Cost:    ${details['C_op']:>12,.2f} /year")
    print(f"  Capital Recovery Factor:  {details['CRF']:>12.6f}")
    
    print("\n--- ENVIRONMENTAL PERFORMANCE ---")
    print(f"  Total Annual Emissions:   {E_total:>12,.2f} kg CO2/year")
    print(f"  Emission Intensity:       {E_total/details['L_year']*1000:>12.4f} g CO2/kWh")
    
    print("\n--- RELIABILITY PERFORMANCE ---")
    print(f"  Loss of Power Supply:     {LPSP*100:>12.4f} %")
    print(f"  Reliability:              {(1-LPSP)*100:>12.4f} %")
    print(f"  Unmet Energy:             {details['E_unmet']:>12,.2f} kWh/year")
    
    print("\n--- ENERGY BALANCE ---")
    print(f"  Annual Load:              {details['L_year']:>12,.2f} kWh/year")
    print(f"  PV Generation:            {details['E_PV_total']:>12,.2f} kWh/year")
    print(f"  Wind Generation:          {details['E_WT_total']:>12,.2f} kWh/year")
    print(f"  Total Renewable:          {details['E_PV_total']+details['E_WT_total']:>12,.2f} kWh/year")
    print(f"  FC Output:                {details['E_FC_total']:>12,.2f} kWh/year")
    print(f"  DG Output:                {details['E_DG_total']:>12,.2f} kWh/year")
    print(f"  EL Input:                 {details['E_EL_total']:>12,.2f} kWh/year")
    print(f"  Grid Sales:               {details['E_grid']:>12,.2f} kWh/year")
    
    print("\n--- COST & PERFORMANCE SUMMARY ---")
    RE_fraction = (details['E_PV_total'] + details['E_WT_total']) / details['L_year'] * 100
    print(f"  Renewable Fraction:       {RE_fraction:>12.2f} %")
    
    LCOE = C_total / details['L_year']
    print(f"  Levelized Cost (LCOE):    ${LCOE:>12.4f} /kWh")
    
    # Capital cost breakdown — correctly using per-component capacities
    c_pv_cost  = parameters['c_PV']     * cap_PV
    c_wt_cost  = parameters['c_WT']     * cap_WT
    c_h2_cost  = parameters['c_H2']     * cap_H2
    c_fc_cost  = parameters['c_FC_cap'] * cap_FC
    c_el_cost  = parameters['c_EL_cap'] * cap_EL
    c_dg_cost  = parameters['c_DG_cap'] * cap_DG
    
    print("\n--- CAPITAL COST BREAKDOWN ---")
    print(f"  PV System:                ${c_pv_cost:>12,.2f} ({c_pv_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  Wind Turbines:            ${c_wt_cost:>12,.2f} ({c_wt_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  H2 Storage:               ${c_h2_cost:>12,.2f} ({c_h2_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  Fuel Cell:                ${c_fc_cost:>12,.2f} ({c_fc_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  Electrolyzer:             ${c_el_cost:>12,.2f} ({c_el_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  Diesel Generator:         ${c_dg_cost:>12,.2f} ({c_dg_cost/details['C_cap']*100:>5.1f}%)")
    
    print("\n" + "="*80)
    
    # Return system and config so callers can use them (e.g. for plotting)
    return C_total, E_total, LPSP, system, config, data, details


def plot_results(details, config, system):
    """
    Create visualization of system performance.

    Parameters
    ----------
    details : dict
        Detailed results dict returned by simulate_year()
    config : dict
        System configuration (N_PV, N_WT, N_H2, N_FC, N_EL, N_DG)
    system : HybridEnergySystem
        Instantiated system object (needed for capacities like Cap_H2)
    """
    H_min_level = system.H_min_percentage * config['N_H2'] * system.Cap_H2
    H_max_level = config['N_H2'] * system.Cap_H2

    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # --- Hydrogen storage trajectory ---
    hours = np.arange(len(details['H_trajectory']))
    axes[0].plot(hours / 24, details['H_trajectory'], linewidth=0.8, label='H2 Level')
    axes[0].axhline(y=H_max_level,  color='red',    linestyle='--', linewidth=1.0, label=f'Max Capacity ({H_max_level:.0f} kg)')
    axes[0].axhline(y=H_min_level,  color='orange', linestyle='--', linewidth=1.0, label=f'Min Level ({H_min_level:.0f} kg)')
    axes[0].set_xlabel('Day')
    axes[0].set_ylabel('Hydrogen Storage (kg)')
    axes[0].set_title('Hydrogen Storage Level Over Time')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # --- Energy generation mix pie chart ---
    energy_sources = ['PV', 'Wind', 'Fuel Cell', 'Diesel']
    energy_values  = [
        details['E_PV_total'],
        details['E_WT_total'],
        details['E_FC_total'],
        details['E_DG_total'],
    ]
    
    # Filter out zero/negligible values for a cleaner chart
    filtered = [(s, v) for s, v in zip(energy_sources, energy_values) if v > 0]
    
    if filtered:
        labels, values = zip(*filtered)
        axes[1].pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        axes[1].set_title('Energy Generation Mix')
    else:
        axes[1].text(0.5, 0.5, 'No Energy Generated', ha='center', va='center',
                     transform=axes[1].transAxes)
        axes[1].set_title('Energy Generation Mix')
    
    plt.tight_layout()
    plt.savefig('simulation_results_cutin2.75.png', dpi=150, bbox_inches='tight')
    print("\nPlot saved to: simulation_results_cutin2.75.png")
    plt.close()


def sensitivity_analysis(file_path):
    """
    Perform sensitivity analysis on hydrogen storage capacity
    (number of H2 storage units, N_H2).
    """
    print("\n" + "="*80)
    print("SENSITIVITY ANALYSIS: Hydrogen Storage Capacity")
    print("="*80)
    
    # Base parameters
    parameters = {
        'eta_PV': 0.15, 'eta_FC': 0.50, 'eta_EL': 0.70, 'H2_LHV': 33.3,
        'eta_INVT': 0.90,
        'c_PV': 1500, 'c_WT': 3000, 'c_H2': 500,
        'c_FC_cap': 2000, 'c_EL_cap': 1500, 'c_DG_cap': 400,
        'c_FC': 0, 'c_DG': 0, 'c_EL': 0, 'c_DG_FUEL': 0.82,
        'om_PV': 20, 'om_WT': 50, 'om_H2': 10,
        'om_FC': 30, 'om_EL': 25, 'om_DG': 15,
        'rc_PV': 20, 'rc_WT': 50, 'rc_H2': 10,
        'rc_FC': 30, 'rc_EL': 25, 'rc_DG': 15,
        'e_FC': 0.0, 'e_DG': 2.639, 'e_EL': 0.0,
        'T_life': 20, 'r': 0.05, 'p_grid': 0.08,
        'A_PV': 6.67, 'P_DG_min': 0.3,
        'life_PV': 25, 'life_WT': 20, 'life_H2': 20,
        'life_FC': 10, 'life_EL': 15, 'life_DG': 15,
    }
    
    system = HybridEnergySystem(parameters)
    
    # Base configuration
    base_config = {
        'N_PV': 100,
        'N_WT': 2,
        'N_H2': 100,   # varied below
        'N_FC': 50,
        'N_EL': 50,
        'N_DG': 30,
    }
    
    # Load data
    try:
        data = pd.read_excel(file_path)
    except FileNotFoundError:
        try:
            data = pd.read_excel('data/combined.xlsx')
        except FileNotFoundError:
            print("Error: No data file found!")
            return None

    # Number of H2 storage units to sweep (total capacity = N_H2 * Cap_H2 kg)
    n_h2_values = [10, 20, 30, 40, 50, 75, 100]

    print(f"\n{'N_H2':>8} | {'H2 Cap (kg)':>12} | {'Cost ($/yr)':>13} | {'Emissions (kg CO2)':>18} | {'LPSP (%)':>9}")
    print("-" * 75)
    
    results = []
    for n_h2 in n_h2_values:
        config = base_config.copy()
        config['N_H2'] = n_h2  # vary the number of H2 units in the config

        total_h2_kg = n_h2 * system.Cap_H2

        C_total, E_total, LPSP, details = system.simulate_year(config, data)
        results.append((n_h2, total_h2_kg, C_total, E_total, LPSP))
        
        print(f"{n_h2:>8} | {total_h2_kg:>12.1f} | {C_total:>13,.0f} | {E_total:>18,.0f} | {LPSP*100:>9.3f}")
    
    return results


if __name__ == "__main__":

    file_path = 'data/semi_final_load.xlsx'


    # =========================================================================
    # LOAD DATA
    # =========================================================================
    try:
        data = pd.read_excel(file_path)
        print("\n" + "="*80)
        print("DATA LOADED")
        print("="*80)
        print(f"  Source: {file_path}")
    except FileNotFoundError:
        try:
            print("Trying Alternative combined")
            data = pd.read_excel('data/combined.xlsx')
            print("\n" + "="*80)
            print("DATA LOADED")
            print("="*80)
            print(f"  Source: data/combined.xlsx")
        except FileNotFoundError:
            print("\n" + "="*80)
            print("ERROR: Could not load data file!")
            print("="*80)
            print("Please ensure one of the following exists:")
            print(f"  - {file_path}")
            print("  - data/combined.xlsx")

    
    # Run single simulation
    result = run_single_simulation(data)
    
    if result is not None:
        C_total, E_total, LPSP, system, config, data, details = result
        
        # Create plots — pass system so plot_results can access capacities
        plot_results(details, config, system)
        
        # Uncomment to run sensitivity analysis
        # sensitivity_results = sensitivity_analysis()