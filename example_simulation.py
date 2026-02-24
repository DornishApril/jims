"""
Example Script: Running the CORRECTED Hybrid Energy System Simulation

This script demonstrates the corrected version with proper unit conversions
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from trial1_simulation import HybridEnergySystem


def run_single_simulation():
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
        # ---------------------------------------------------------------------
        # EFFICIENCIES (dimensionless, 0-1)
        # ---------------------------------------------------------------------
        'eta_PV': 0.15,           # 15% PV panel efficiency
        'eta_FC': 0.50,           # 50% fuel cell efficiency
        'eta_EL': 0.70,           # 70% electrolyzer efficiency
        
        # ---------------------------------------------------------------------
        # HYDROGEN PROPERTIES
        # ---------------------------------------------------------------------
        'H2_LHV': 33.3,           # Lower Heating Value: 33.3 kWh/kg (constant)
        
        # With these values:
        # - Fuel cell produces: 0.50 × 33.3 = 16.65 kWh per kg H2 consumed
        # - Electrolyzer needs: 33.3 / 0.70 = 47.6 kWh to produce 1 kg H2
        # - Round-trip efficiency: 0.50 × 0.70 = 35%
        
        # ---------------------------------------------------------------------
        # CAPITAL COSTS ($/unit)
        # ---------------------------------------------------------------------
        'c_PV': 1500,             # $/kW installed
        'c_WT': 3000,             # $/kW installed
        'c_H2': 500,              # $/kg storage capacity
        'c_FC_cap': 2000,         # $/kW fuel cell capacity
        'c_EL_cap': 1500,         # $/kW electrolyzer capacity
        'c_DG_cap': 400,          # $/kW diesel generator capacity
        
        # ---------------------------------------------------------------------
        # OPERATING COSTS ($/kWh)
        # ---------------------------------------------------------------------
        'c_FC': 0.01,             # Fuel cell O&M per kWh produced
        'c_DG': 0.30,             # Diesel fuel cost per kWh produced
        'c_EL': 0.01,             # Electrolyzer O&M per kWh consumed
        
        # ---------------------------------------------------------------------
        # ANNUAL O&M COSTS ($/unit/year)
        # ---------------------------------------------------------------------
        'om_PV': 20,              # $/kW/year
        'om_WT': 50,              # $/kW/year
        'om_H2': 10,              # $/kg/year
        'om_FC': 30,              # $/kW/year
        'om_EL': 25,              # $/kW/year
        'om_DG': 15,              # $/kW/year
        
        # ---------------------------------------------------------------------
        # EMISSION FACTORS (kg CO2/kWh)
        # ---------------------------------------------------------------------
        'e_FC': 0.0,              # Fuel cell (assuming green H2)
        'e_DG': 0.8,              # Diesel generator
        'e_EL': 0.0,              # Electrolyzer (direct emissions)
        
        # ---------------------------------------------------------------------
        # ECONOMIC PARAMETERS
        # ---------------------------------------------------------------------
        'T_life': 20,             # Project lifetime (years)
        'r': 0.05,                # Discount rate (5% annual)
        'p_grid': 0.08,           # Grid selling price ($/kWh)
        
        # ---------------------------------------------------------------------
        # TECHNICAL PARAMETERS
        # ---------------------------------------------------------------------
        'A_PV': 6.67,             # PV area: m²/kW (for 15% efficiency)
                                  # Calculation: 1000 W/m² / (0.15 × 1000 W/kW) = 6.67
        'P_DG_min': 0.1,          # Diesel must run at ≥30% capacity
        
        # ---------------------------------------------------------------------
        # COMPONENT LIFETIMES (years)
        # ---------------------------------------------------------------------
        'life_PV': 25,            # Solar panels
        'life_WT': 20,            # Wind turbines
        'life_H2': 20,            # Hydrogen storage tanks
        'life_FC': 10,            # Fuel cells (need replacement)
        'life_EL': 15,            # Electrolyzers
        'life_DG': 15,            # Diesel generators
    }
    
    # =========================================================================
    # CREATE SYSTEM INSTANCE
    # =========================================================================
    system = HybridEnergySystem(parameters)
    
    # =========================================================================
    # DEFINE SYSTEM CONFIGURATION
    # =========================================================================
    config = {
        'N_PV': 5,      # Number of PV
        'N_WT': 1120,      # kW wind turbine rated capacity
        'Cap_H2': 2000,    # kg hydrogen storage capacity
        'Cap_FC': 800,     # kW fuel cell capacity
        'Cap_EL': 800,     # kW electrolyzer capacity
        'Cap_DG': 450,     # kW diesel generator capacity
    }
    
    print("\n" + "="*80)
    print("SYSTEM CONFIGURATION")
    print("="*80)
    print(f"  PV Capacity:              {config['N_PV']:>8} kW")
    print(f"  Wind Turbine Capacity:    {config['N_WT']:>8} kW")
    print(f"  H2 Storage Capacity:      {config['Cap_H2']:>8} kg")
    print(f"  Fuel Cell Capacity:       {config['Cap_FC']:>8} kW")
    print(f"  Electrolyzer Capacity:    {config['Cap_EL']:>8} kW")
    print(f"  Diesel Generator:         {config['Cap_DG']:>8} kW")
    
    print("\n" + "="*80)
    print("EFFICIENCY DETAILS")
    print("="*80)
    print(f"  PV Efficiency:            {parameters['eta_PV']*100:>6.1f} %")
    print(f"  Fuel Cell Efficiency:     {parameters['eta_FC']*100:>6.1f} %")
    print(f"  Electrolyzer Efficiency:  {parameters['eta_EL']*100:>6.1f} %")
    print(f"  H2 Lower Heating Value:   {parameters['H2_LHV']:>6.1f} kWh/kg")
    print()
    print(f"  FC Output:                {parameters['eta_FC']*parameters['H2_LHV']:>6.2f} kWh per kg H2")
    print(f"  EL Input Required:        {parameters['H2_LHV']/parameters['eta_EL']:>6.2f} kWh per kg H2")
    print(f"  Round-trip Efficiency:    {parameters['eta_FC']*parameters['eta_EL']*100:>6.1f} %")
    
    # =========================================================================
    # LOAD DATA
    # =========================================================================
    try:
        data = pd.read_excel('data/Load.xlsx')
        print("\n" + "="*80)
        print("DATA LOADED")
        print("="*80)
        print(f"  Source: data/Load.xlsx")
    except:
        try:
            data = pd.read_excel('data/combined.xlsx')
            print("\n" + "="*80)
            print("DATA LOADED")
            print("="*80)
            print(f"  Source: data/combined.xlsx")
        except:
            print("\n" + "="*80)
            print("ERROR: Could not load data file!")
            print("="*80)
            print("Please ensure one of the following exists:")
            print("  - data/Load.xlsx")
            print("  - data/combined.xlsx")
            return None
    
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
    print(f"  Capital Cost (PV):        ${details['C_cap']:>12,.2f}")
    print(f"  Replacement Cost (PV):    ${details['C_rep']:>12,.2f}")
    print(f"  Annual O&M Cost:          ${details['C_om_annual']:>12,.2f} /year")
    print(f"  Annual Operating Cost:    ${details['C_op']:>12,.2f} /year")
    print(f"  Capital Recovery Factor:  {details['CRF']:>12.6f}")
    
    print("\n--- ENVIRONMENTAL PERFORMANCE ---")
    print(f"  Total Annual Emissions:   {E_total:>12,.2f} kg CO2/year")
    print(f"  Emission Intensity:       {E_total/details['L_year']*1000:>12,.4f} g CO2/kWh")
    
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
    
    print("\n--- COST BREAKDOWN ---")
    RE_fraction = (details['E_PV_total'] + details['E_WT_total']) / details['L_year'] * 100
    print(f"  Renewable Fraction:       {RE_fraction:>12.2f} %")
    
    LCOE = C_total / details['L_year']
    print(f"  Levelized Cost (LCOE):    ${LCOE:>12.4f} /kWh")
    
    # Capital cost breakdown
    c_pv_cost = parameters['c_PV'] * config['N_PV']
    c_wt_cost = parameters['c_WT'] * config['N_WT']
    c_h2_cost = parameters['c_H2'] * config['Cap_H2']
    c_fc_cost = parameters['c_FC_cap'] * config['Cap_FC']
    c_el_cost = parameters['c_EL_cap'] * config['Cap_EL']
    c_dg_cost = parameters['c_DG_cap'] * config['Cap_DG']
    
    print("\n--- CAPITAL COST BREAKDOWN ---")
    print(f"  PV System:                ${c_pv_cost:>12,.2f} ({c_pv_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  Wind Turbines:            ${c_wt_cost:>12,.2f} ({c_wt_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  H2 Storage:               ${c_h2_cost:>12,.2f} ({c_h2_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  Fuel Cell:                ${c_fc_cost:>12,.2f} ({c_fc_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  Electrolyzer:             ${c_el_cost:>12,.2f} ({c_el_cost/details['C_cap']*100:>5.1f}%)")
    print(f"  Diesel Generator:         ${c_dg_cost:>12,.2f} ({c_dg_cost/details['C_cap']*100:>5.1f}%)")
    
    print("\n" + "="*80)
    
    return C_total, E_total, LPSP, system, config, data, details


def plot_results(details, config):
    """
    Create visualization of system performance
    """
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # Hydrogen storage trajectory
    hours = np.arange(len(details['H_trajectory']))
    axes[0].plot(hours / 24, details['H_trajectory'], linewidth=0.8)
    # axes[0].axhline(y=config['Cap_H2'], color='r', linestyle='--', label='Max Capacity')
    axes[0].axhline(y=0.1*config['Cap_H2'], color='orange', linestyle='--', label='Min Level (10%)')
    axes[0].set_xlabel('Day')
    axes[0].set_ylabel('Hydrogen Storage (kg)')
    axes[0].set_title('Hydrogen Storage Level Over Time')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Energy balance pie chart
    energy_sources = ['PV', 'Wind', 'Fuel Cell', 'Diesel']
    energy_values = [
        details['E_PV_total'],
        details['E_WT_total'],
        details['E_FC_total'],
        details['E_DG_total']
    ]
    
    # Filter out zero values for cleaner visualization
    filtered_sources = []
    filtered_values = []
    for source, value in zip(energy_sources, energy_values):
        if value > 0:
            filtered_sources.append(source)
            filtered_values.append(value)
    
    if filtered_values:
        axes[1].pie(filtered_values, labels=filtered_sources, autopct='%1.1f%%', startangle=90)
        axes[1].set_title('Energy Generation Mix')
    else:
        axes[1].text(0.5, 0.5, 'No Energy Generated', ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig('simulation_results_cutin2.75.png', dpi=150, bbox_inches='tight')
    print("\nPlot saved to: simulation_results.png")
    plt.close()


def sensitivity_analysis():
    """
    Perform sensitivity analysis on hydrogen storage capacity
    """
    print("\n" + "="*80)
    print("SENSITIVITY ANALYSIS: Hydrogen Storage Capacity")
    print("="*80)
    
    # Base parameters
    parameters = {
        'eta_PV': 0.15, 'eta_FC': 0.50, 'eta_EL': 0.70, 'H2_LHV': 33.3,
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
    
    system = HybridEnergySystem(parameters)
    
    # Base configuration
    base_config = {
        'N_PV': 1500,
        'N_WT': 1000,
        'Cap_H2': 2000,  # Will vary this
        'Cap_FC': 800,
        'Cap_EL': 800,
        'Cap_DG': 500,
    }
    
    # Load data
    try:
        data = pd.read_excel('data/Load.xlsx')
    except:
        try:
            data = pd.read_excel('data/combined.xlsx')
        except:
            print("Error: No data file found!")
            return
    
    # Test different H2 storage capacities
    h2_capacities = [500, 1000, 1500, 2000, 2500, 3000, 4000]
    
    print("\nH2 Capacity (kg) | Cost ($/year) | Emissions (kg CO2) | LPSP (%)")
    print("-" * 80)
    
    results = []
    for h2_cap in h2_capacities:
        config = base_config.copy()
        config['Cap_H2'] = h2_cap
        
        C_total, E_total, LPSP, details = system.simulate_year(config, data)
        results.append((h2_cap, C_total, E_total, LPSP))
        
        print(f"{h2_cap:>16} | {C_total:>13,.0f} | {E_total:>18,.0f} | {LPSP*100:>7.3f}")
    
    return results


if __name__ == "__main__":
    # Run single simulation
    result = run_single_simulation()
    
    if result is not None:
        C_total, E_total, LPSP, system, config, data, details = result
        
        # Create plots
        plot_results(details, config)
        
        # Uncomment to run sensitivity analysis
        # sensitivity_results = sensitivity_analysis()