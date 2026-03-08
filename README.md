# Hybrid Energy System Simulation

A comprehensive Python-based simulation framework for designing and optimizing **hybrid renewable energy systems** with photovoltaic (PV), wind turbines, hydrogen storage, fuel cells, electrolyzers, and diesel generators.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Components](#core-components)
- [System Parameters](#system-parameters)
- [Usage Examples](#usage-examples)
- [Output & Analysis](#output--analysis)
- [Unit Conventions](#unit-conventions)
- [File Structure](#file-structure)

## 🌍 Overview

This project simulates a **hybrid renewable energy system** designed to meet electricity loads through a combination of:

- **Renewable Sources**: Photovoltaic panels and wind turbines
- **Energy Storage**: Hydrogen storage with electrolyzer (generation) and fuel cell (discharge)
- **Backup**: Diesel generator for reliability and peak shaving
- **Grid Integration**: Optional grid connection for selling excess power

The simulation calculates three key performance metrics:
1. **Economic Performance**: Total annualized costs including capital, operating, and maintenance expenses
2. **Environmental Impact**: Annual CO₂ emissions from diesel use
3. **Reliability**: Loss of Power Supply Probability (LPSP) and unmet energy

### Use Cases
- **Off-grid communities**: Remote locations without grid access
- **Microgrids**: Industrial facilities or campuses with critical loads
- **Island systems**: Isolated locations requiring energy independence
- **Sustainability studies**: Analyzing renewable energy integration strategies

## ✨ Features

### Simulation Capabilities
- ✅ **Hourly resolution**: Detailed hourly-based energy balance modeling
- ✅ **Dynamic hydrogen storage**: Real-time hydrogen charging/discharging with efficiency losses
- ✅ **Wind power curves**: Non-linear wind turbine output based on cut-in, rated, and cut-out speeds
- ✅ **Diesel fuel consumption**: Realistic fuel curve accounting for no-load consumption
- ✅ **Multi-year flexibility**: Simulates any duration (typically 1 year of hourly data)

### Economic Analysis
- ✅ **Capital cost breakdown**: Detailed cost allocation across all components
- ✅ **Replacement costs**: Time-value-adjusted costs for component replacement over project lifetime
- ✅ **Operation & maintenance (O&M)**: Annual costs for each component type
- ✅ **Operating costs**: Fuel and grid interaction costs
- ✅ **Levelized Cost of Energy (LCOE)**: Economic efficiency metric
- ✅ **Capital Recovery Factor (CRF)**: Net present value calculations with discounting

### Environmental Analysis
- ✅ **CO₂ emissions tracking**: Real-time emissions from diesel consumption
- ✅ **Emission intensity**: g CO₂/kWh metric for comparison
- ✅ **Green hydrogen support**: Zero-emission operation when using renewable H₂ production

### Reliability Metrics
- ✅ **Loss of Power Supply Probability (LPSP)**: Percentage of unmet demand
- ✅ **Reliability percentage**: 1 - LPSP
- ✅ **Energy balance verification**: Hourly tracking of all flows

## 🏗️ System Architecture

### Component Structure

```
┌─────────────────────────────────────────────────────┐
│         HYBRID RENEWABLE ENERGY SYSTEM               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────────┐    ┌──────────────┐                │
│  │     PV      │    │  Wind Turbine│                │
│  │   Panels    │    │      (WT)    │                │
│  └────┬────────┘    └───────┬──────┘                │
│       │                    │                        │
│       └────────┬───────────┘                        │
│                │ (kWh) Renewable Power              │
│       ┌────────▼─────────────────┐                 │
│       │  Inverter (AC/DC Conv.)  │                 │
│       └────────┬─────────────────┘                 │
│                │                                   │
│    ┌───────────┴──────────┬──────────────┐         │
│    │                      │              │         │
│ ┌──▼──┐            ┌──────▼───┐     ┌───▼───┐     │
│ │ EL  │ →Excess→   │    H2    │ →   │ Fuel  │     │
│ │     │   Power    │ Storage  │  Demand   Cell│    │
│ │     │ ◄─Shortage │    (H2)  │ ◄─  │      │     │
│ └─────┘            └──────────┘     └───────┘     │
│                      (kg)                          │
│                                                   │
│       ┌────────────────────────┐                  │
│       │  Diesel Generator (DG) │                  │
│       │  (Last Resort/Peak)    │                  │
│       └────────────────────────┘                  │
│                                                   │
│       ┌────────────────────────┐                  │
│       │   Grid Connection      │                  │
│       │   (Optional)           │                  │
│       └────────────────────────┘                  │
│                                                   │
└─────────────────────────────────────────────────────┘
         │ Supplies → Community Load
         │ ← Unmet Load = Shortage (LPSP)
```

### Energy Flow Priority
1. **Renewable Generation** (PV + WT) meets load first
2. **Excess** power charges electrolyzer → H₂ storage
3. **Shortage** discharged from fuel cell (if H₂ available) or diesel backup
4. **Grid** sells excess or buys power (if available)

## 📦 Installation

### Requirements
- **Python 3.8+**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Plotting and visualization
- **openpyxl**: Excel file reading for load data

### Setup

```bash
# Clone or download the repository
cd c:\Users\Admin\OneDrive\Desktop\jims

# Install required packages
pip install pandas numpy matplotlib openpyxl

# Verify installation
python -c "import pandas; import numpy; import matplotlib; print('All dependencies installed!')"
```

## 🚀 Quick Start

### 1. Prepare Your Data
Your hourly load data should be in Excel format with columns:
- `Community Load` (kWh): Hourly electricity demand
- `Solar Power` or `Solar Irradiance (W/sq.m)`: Solar resource data
- `Wind Speed (m/s)`: Hourly wind speed

Example data files:
- `data/semi_final_load.xlsx`
- `data/combined.xlsx`

### 2. Run a Basic Simulation

```python
from trial1_simulation import HybridEnergySystem
import pandas as pd

# Load your data
data = pd.read_excel('data/semi_final_load.xlsx')

# Define system parameters (see System Parameters section for all options)
parameters = {
    'rated_PV': 0.327,          # kW per panel
    'rated_power': 25.0,        # kW per wind turbine
    'Cap_H2': 6,                # kg per storage unit
    'Cap_FC': 2,                # kW per fuel cell
    'Cap_EL': 2,                # kW per electrolyzer
    'Cap_DG': 50,               # kW per diesel generator
    'eta_PV': 0.15,             # 15% efficiency
    'eta_FC': 0.50,             # 50% efficiency
    'eta_EL': 0.70,             # 70% efficiency
    'H2_LHV': 33.3,             # kWh/kg
    'c_PV': 1500,               # $/kW
    'c_WT': 3000,               # $/kW
    'c_H2': 500,                # $/kg
    # ... (see example_simulation.py for complete parameters)
}

# Create system instance
system = HybridEnergySystem(parameters)

# Define system configuration
config = {
    'N_PV': 200,                # 200 PV panels → 65.4 kW capacity
    'N_WT': 10,                 # 10 wind turbines → 250 kW capacity
    'N_H2': 50,                 # 50 storage units → 300 kg capacity
    'N_FC': 50,                 # 50 fuel cells → 100 kW capacity
    'N_EL': 50,                 # 50 electrolyzers → 100 kW capacity
    'N_DG': 5,                  # 5 diesel generators → 250 kW capacity
}

# Run simulation
C_total, E_total, LPSP, details = system.simulate_year(config, data)

print(f"Total Annual Cost: ${C_total:,.2f}")
print(f"Annual Emissions: {E_total:,.2f} kg CO2")
print(f"Reliability: {(1-LPSP)*100:.2f}%")
```

### 3. Visualize Results

```python
import matplotlib.pyplot as plt
import numpy as np

# Plot hydrogen storage trajectory
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

hours = np.arange(len(details['H_trajectory']))
axes[0].plot(hours / 24, details['H_trajectory'], linewidth=0.8)
axes[0].set_xlabel('Day')
axes[0].set_ylabel('Hydrogen Storage (kg)')
axes[0].set_title('Hydrogen Storage Level Over Time')
axes[0].grid(True, alpha=0.3)

# Plot energy generation mix
energy_sources = ['PV', 'Wind', 'Fuel Cell', 'Diesel']
energy_values = [
    details['E_PV_total'],
    details['E_WT_total'],
    details['E_FC_total'],
    details['E_DG_total'],
]
axes[1].pie(energy_values, labels=energy_sources, autopct='%1.1f%%')
axes[1].set_title('Annual Energy Generation Mix')

plt.tight_layout()
plt.savefig('simulation_results.png', dpi=150)
plt.show()
```

## 🔧 Core Components

### HybridEnergySystem Class

The main simulation engine. Located in `trial1_simulation.py`.

#### Key Methods

```python
# Initialize system with parameters
system = HybridEnergySystem(parameters)

# Run annual simulation
C_total, E_total, LPSP, details = system.simulate_year(config, data)
```

#### Wind Power Curve

```python
def wind_power_curve(self, v: float) -> float:
    """
    Calculate wind output based on wind speed using cubic interpolation.
    
    - Below cut-in (2.75 m/s): Zero output
    - Cut-in to rated (2.75-9.0 m/s): Cubic relationship
    - Above rated (>9.0 m/s): Rated power
    """
```

#### Cost Calculations

**Capital Costs** (one-time):
```
C_cap = (N_PV × rated_PV × c_PV) 
      + (N_WT × rated_power × c_WT)
      + (N_H2 × Cap_H2 × c_H2)
      + (N_FC × Cap_FC × c_FC_cap)
      + (N_EL × Cap_EL × c_EL_cap)
      + (N_DG × Cap_DG × c_DG_cap)
      + c_INVT
```

**Operating Costs** (annual):
```
C_op = ∑(fuel consumed × c_DG_FUEL) + ∑(grid energy sold × p_grid)
```

**O&M Costs** (annual):
```
C_om = (cap_PV × om_PV) + (cap_WT × om_WT) + (cap_H2 × om_H2) + ...
```

**Annualized Cost**:
```
C_total = C_cap × CRF + C_om + C_op_annual + C_rep_annual
```

Where `CRF = r(1+r)^T / ((1+r)^T - 1)` (Capital Recovery Factor)

### Example Simulation Script

Located in `example_simulation.py`. Includes:
- `run_single_simulation(data)`: Full simulation with detailed output
- `plot_results(details, config, system)`: Visualization functions
- `sensitivity_analysis(file_path)`: Parameter sweep analysis

## 📊 System Parameters

All parameters are defined in a dictionary and passed to `HybridEnergySystem()`. Below is the complete parameter list:

### Generator Configurations

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `rated_PV` | float | kW | 0.327 | Rated power per PV panel |
| `v_cut_in` | float | m/s | 2.75 | Wind turbine cut-in speed |
| `v_rated` | float | m/s | 9.0 | Wind turbine rated speed |
| `rated_power` | float | kW | 25.0 | Rated power per wind turbine |
| `Cap_H2` | float | kg | 6 | Capacity of one H₂ storage unit |
| `Cap_FC` | float | kW | 2 | Rated power of one fuel cell unit |
| `Cap_EL` | float | kW | 2 | Rated power of one electrolyzer unit |
| `Cap_DG` | float | kW | 50 | Rated power of one diesel generator unit |
| `H_min_percentage` | float | fraction | 0 | Minimum H₂ storage level (0-1) |
| `H_max_percentage` | float | fraction | 0 | Maximum H₂ storage override (0-1) |

### Diesel Fuel Curve

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `f_0` | float | litre/kW/h | 0.246 | Intercept coefficient (no-load consumption) |
| `f_1` | float | litre/kWh | 0.08145 | Slope coefficient (load-dependent) |

**Fuel consumption formula**: `fuel = (f_0 × P_rated + f_1 × P_output) × dt`

### Efficiency Parameters

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `eta_PV` | float | fraction | 0.15 | PV panel efficiency (15%) |
| `eta_FC` | float | fraction | 0.50 | Fuel cell efficiency (50%) |
| `eta_EL` | float | fraction | 0.70 | Electrolyzer efficiency (70%) |
| `eta_INVT` | float | fraction | 0.90 | Inverter efficiency (90%) |
| `H2_LHV` | float | kWh/kg | 33.3 | Hydrogen lower heating value |

**Key relationships**:
- Fuel cell output: `P_FC = H2_kg_consumed × H2_LHV × eta_FC`
- Electrolyzer input: `E_required = kg_produced × H2_LHV / eta_EL`
- Round-trip efficiency: `eta_FC × eta_EL ≈ 35%`

### Capital Costs (one-time investment)

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `c_PV` | float | $/kW | 1500 | PV system capital cost |
| `c_WT` | float | $/kW | 3000 | Wind turbine capital cost |
| `c_H2` | float | $/kg | 500 | Hydrogen storage capital cost |
| `c_FC_cap` | float | $/kW | 2000 | Fuel cell capital cost |
| `c_EL_cap` | float | $/kW | 1500 | Electrolyzer capital cost |
| `c_DG_cap` | float | $/kW | 400 | Diesel generator capital cost |
| `c_INVT` | float | $ | 300 | Inverter capital cost (flat) |

### Operating Costs

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `c_FC` | float | $/kWh | 0 | Fuel cell operating cost per kWh produced |
| `c_DG` | float | $/kWh | 0 | Diesel operating cost per kWh |
| `c_EL` | float | $/kWh | 0 | Electrolyzer operating cost per kWh |
| `c_DG_FUEL` | float | $/litre | 0.82 | Diesel fuel cost |

### Operation & Maintenance (O&M) Costs (annual)

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `om_PV` | float | $/kW/year | 20 | PV O&M cost |
| `om_WT` | float | $/kW/year | 50 | Wind turbine O&M |
| `om_H2` | float | $/kg/year | 10 | Hydrogen storage O&M |
| `om_FC` | float | $/kW/year | 30 | Fuel cell O&M |
| `om_EL` | float | $/kW/year | 25 | Electrolyzer O&M |
| `om_DG` | float | $/h | 0.03 | Diesel generator O&M (per operating hour) |
| `om_INVT` | float | $ | 0 | Inverter O&M (flat) |

### Replacement Costs (present value)

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `rc_PV` | float | $/kW | 0 | PV replacement cost |
| `rc_WT` | float | $/kW | 1750 | Wind turbine replacement |
| `rc_H2` | float | $/kg | 10 | Hydrogen storage replacement |
| `rc_FC` | float | $/kW | 30 | Fuel cell replacement |
| `rc_EL` | float | $/kW | 25 | Electrolyzer replacement |
| `rc_DG` | float | $/kW | 500 | Diesel generator replacement |
| `rc_INVT` | float | $ | 300 | Inverter replacement |

### Emission Factors

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `e_FC` | float | kg CO₂/kWh | 0.0 | Fuel cell emissions (green H₂ = 0) |
| `e_DG` | float | kg CO₂/litre | 2.6391 | Diesel emissions (per litre) |
| `e_EL` | float | kg CO₂/kWh | 0.0 | Electrolyzer direct emissions |

### Economic Parameters

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `T_life` | int | years | 20 | Project lifetime |
| `r` | float | fraction | 0.05 | Annual discount rate (5%) |
| `p_grid` | float | $/kWh | 0.08 | Grid energy selling price |

### Technical Parameters

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `A_PV` | float | m²/kW | 6.67 | PV area per kW capacity |
| `P_DG_min` | float | fraction | 0.3 | Minimum diesel load ratio (30%) |

### Component Lifetimes

| Parameter | Type | Unit | Default | Description |
|-----------|------|------|---------|-------------|
| `life_PV` | int | years | 25 | PV panel lifetime |
| `life_WT` | int | years | 20 | Wind turbine lifetime |
| `life_H2` | int | years | 20 | Hydrogen storage lifetime |
| `life_FC` | int | years | 10 | Fuel cell lifetime |
| `life_EL` | int | years | 15 | Electrolyzer lifetime |
| `life_DG` | int | years | 15 | Diesel generator lifetime |
| `life_INVT` | int | years | 15 | Inverter lifetime |

## 💡 Usage Examples

### Example 1: Basic Simulation with Default Parameters

```python
from trial1_simulation import HybridEnergySystem
import pandas as pd

# Load hourly data (8760 hours = 1 year)
data = pd.read_excel('data/semi_final_load.xlsx')

# Use example configuration
parameters = {
    'rated_PV': 0.327,
    'rated_power': 25.0,
    'Cap_H2': 6,
    'Cap_FC': 2,
    'Cap_EL': 2,
    'Cap_DG': 50,
    'eta_PV': 0.15,
    'eta_FC': 0.50,
    'eta_EL': 0.70,
    'eta_INVT': 0.90,
    'H2_LHV': 33.3,
    'c_PV': 1500,
    'c_WT': 3000,
    'c_H2': 500,
    'c_FC_cap': 2000,
    'c_EL_cap': 1500,
    'c_DG_cap': 400,
    'c_INVT': 300,
    'c_DG_FUEL': 0.82,
    'om_PV': 20,
    'om_WT': 50,
    'om_H2': 10,
    'om_FC': 30,
    'om_EL': 25,
    'om_DG': 0.03,
    'om_INVT': 0,
    'rc_PV': 0,
    'rc_WT': 1750,
    'rc_H2': 10,
    'rc_FC': 30,
    'rc_EL': 25,
    'rc_DG': 500,
    'rc_INVT': 300,
    'e_FC': 0.0,
    'e_DG': 2.6391,
    'e_EL': 0.0,
    'T_life': 20,
    'r': 0.05,
    'p_grid': 0.08,
    'A_PV': 6.67,
    'P_DG_min': 0.3,
    'life_PV': 25,
    'life_WT': 20,
    'life_H2': 20,
    'life_FC': 10,
    'life_EL': 15,
    'life_DG': 15,
    'life_INVT': 15,
}

system = HybridEnergySystem(parameters)

config = {
    'N_PV': 200,
    'N_WT': 10,
    'N_H2': 50,
    'N_FC': 50,
    'N_EL': 50,
    'N_DG': 5,
}

C_total, E_total, LPSP, details = system.simulate_year(config, data)
```

### Example 2: Sensitivity Analysis (H₂ Storage Capacity)

```python
from trial1_simulation import HybridEnergySystem
import pandas as pd

data = pd.read_excel('data/semi_final_load.xlsx')
system = HybridEnergySystem(parameters)

# Sweep hydrogen storage capacity
n_h2_values = [10, 20, 30, 40, 50, 75, 100]

results = []
for n_h2 in n_h2_values:
    config = {
        'N_PV': 200,
        'N_WT': 10,
        'N_H2': n_h2,          # Vary H₂ storage
        'N_FC': 50,
        'N_EL': 50,
        'N_DG': 5,
    }
    
    C_total, E_total, LPSP, details = system.simulate_year(config, data)
    h2_capacity = n_h2 * system.Cap_H2
    
    results.append({
        'N_H2': n_h2,
        'H2_Capacity_kg': h2_capacity,
        'Cost_$/yr': C_total,
        'Emissions_kg_CO2': E_total,
        'LPSP_%': LPSP * 100,
    })
    
    print(f"N_H2={n_h2:3d} | Capacity={h2_capacity:6.1f} kg | Cost=${C_total:10,.0f} | LPSP={LPSP*100:6.2f}%")
```

### Example 3: Multi-Scenario Comparison

```python
from trial1_simulation import HybridEnergySystem
import pandas as pd

data = pd.read_excel('data/semi_final_load.xlsx')

scenarios = {
    "High Renewable": {
        'N_PV': 300, 'N_WT': 15, 'N_H2': 75, 'N_FC': 75, 'N_EL': 75, 'N_DG': 2
    },
    "Balanced": {
        'N_PV': 200, 'N_WT': 10, 'N_H2': 50, 'N_FC': 50, 'N_EL': 50, 'N_DG': 5
    },
    "Low Cost": {
        'N_PV': 100, 'N_WT': 5, 'N_H2': 25, 'N_FC': 25, 'N_EL': 25, 'N_DG': 10
    },
}

system = HybridEnergySystem(parameters)

print(f"{'Scenario':<20} | {'Cost ($/yr)':<15} | {'Emissions':<15} | {'Reliability':<12}")
print("-" * 70)

for name, config in scenarios.items():
    C_total, E_total, LPSP, details = system.simulate_year(config, data)
    reliability = (1 - LPSP) * 100
    print(f"{name:<20} | ${C_total:>12,.0f} | {E_total:>12,.0f} kg CO₂ | {reliability:>10.2f}%")
```

## 📈 Output & Analysis

### Simulation Output Structure

The `simulate_year()` method returns a tuple:

```python
C_total, E_total, LPSP, details = system.simulate_year(config, data)
```

#### Return Values

| Variable | Type | Description |
|----------|------|-------------|
| `C_total` | float | Total annualized cost ($/year) |
| `E_total` | float | Total annual CO₂ emissions (kg CO₂/year) |
| `LPSP` | float | Loss of Power Supply Probability (0-1) |
| `details` | dict | Comprehensive results dictionary (see below) |

#### Details Dictionary

```python
details = {
    # Economic
    'C_cap': float,              # Capital cost ($)
    'C_rep': float,              # Replacement costs ($)
    'C_om_annual': float,        # Annual O&M cost ($/year)
    'C_op': float,               # Annual operating cost ($/year)
    'CRF': float,                # Capital recovery factor
    
    # Energy (kWh/year)
    'L_year': float,             # Total annual load
    'E_PV_total': float,         # PV generation
    'E_WT_total': float,         # Wind generation
    'E_FC_total': float,         # Fuel cell output
    'E_EL_total': float,         # Electrolyzer input
    'E_DG_total': float,         # Diesel generation
    'E_unmet': float,            # Unmet energy (blackouts)
    'E_grid': float,             # Grid interaction (positive = sales)
    
    # Hydrogen (kg)
    'H_trajectory': list,        # Hourly H₂ storage level
    
    # Reliability
    'LPSP': float,               # Loss of power supply probability
}
```

### Example Output Display

```
================================================================================
SIMULATION RESULTS
================================================================================

--- ECONOMIC PERFORMANCE ---
  Total Annualized Cost:    $125,450.00 /year
  Capital Cost:             $450,000.00
  Replacement Cost (PV):    $15,000.00
  Annual O&M Cost:          $25,450.00 /year
  Annual Operating Cost:    $35,000.00 /year
  Capital Recovery Factor:  0.065410

--- ENVIRONMENTAL PERFORMANCE ---
  Total Annual Emissions:   285,432.50 kg CO2/year
  Emission Intensity:       0.2603 g CO2/kWh

--- RELIABILITY PERFORMANCE ---
  Loss of Power Supply:     2.3400 %
  Reliability:              97.6600 %
  Unmet Energy:             25,680.00 kWh/year

--- ENERGY BALANCE ---
  Annual Load:              1,100,000.00 kWh/year
  PV Generation:            180,000.00 kWh/year
  Wind Generation:          450,000.00 kWh/year
  Total Renewable:          630,000.00 kWh/year
  FC Output:                320,000.00 kWh/year
  DG Output:                150,000.00 kWh/year
  EL Input:                 280,000.00 kWh/year
  Grid Sales:               40,000.00 kWh/year

--- COST & PERFORMANCE SUMMARY ---
  Renewable Fraction:       57.27 %
  Levelized Cost (LCOE):    $0.1140 /kWh

--- CAPITAL COST BREAKDOWN ---
  PV System:                $90,000.00 (20.0%)
  Wind Turbines:            $300,000.00 (66.7%)
  H2 Storage:               $30,000.00 (6.7%)
  Fuel Cell:                $50,000.00 (11.1%)
  Electrolyzer:             $37,500.00 (8.3%)
  Diesel Generator:         $10,000.00 (2.2%)
```

## 📝 Unit Conventions

All calculations use consistent SI-derived units:

| Quantity | Unit | Symbol | Notes |
|----------|------|--------|-------|
| Power | Kilowatt | kW | Instantaneous generation/demand |
| Energy | Kilowatt-hour | kWh | Energy over time (1 kWh = 3.6 MJ) |
| Hydrogen mass | Kilogram | kg | Storage quantity |
| Temperature | Celsius | °C | Ambient conditions |
| Wind speed | Meters/second | m/s | Weather input |
| Solar irradiance | Watts/m² | W/m² | Weather input |
| Currency | US Dollar | $ | All monetary values |
| Time | Hour | h | Simulation timestep |
| Emissions | Kilograms CO₂ | kg CO₂ | Annual total |
| Efficiency | Fraction | 0-1 | Percentage as decimal |
| Cost | Dollar per unit | $/kW, $/kg | Prices and rates |

## 📂 File Structure

```
c:\Users\Admin\OneDrive\Desktop\jims\
│
├── trial1_simulation.py          # Core simulation engine
│   └── HybridEnergySystem class
│       ├── __init__()            # Parameter initialization
│       ├── wind_power_curve()    # Wind turbine model
│       ├── calculate_replacement_cost()
│       └── simulate_year()       # Main simulation loop
│
├── example_simulation.py          # Example usage and visualization
│   ├── run_single_simulation()   # Complete simulation workflow
│   ├── plot_results()            # Matplotlib visualizations
│   └── sensitivity_analysis()    # Parameter sweep
│
├── data/
│   ├── semi_final_load.xlsx      # Primary load data
│   ├── combined.xlsx             # Alternative dataset
│   ├── Load.xlsx
│   └── Thesis_Load.xlsx
│
├── README.md                      # Original documentation
├── README2.md                     # This file (comprehensive guide)
├── simulation_results_cutin2.75.png  # Sample output plot
│
└── gitignore_files/              # Archive and supporting materials
```

## 🔍 Key Formulas

### Wind Power Output

```
If v < v_cut_in:
    P_wind = 0

If v_cut_in ≤ v < v_rated:
    P_wind = P_rated × (v³ - v_cut_in³) / (v_rated³ - v_cut_in³)

If v ≥ v_rated:
    P_wind = P_rated
```

### Diesel Fuel Consumption

```
fuel_consumed (litre/hour) = f_0 × P_rated + f_1 × P_output
```

Where:
- `f_0`: No-load fuel consumption coefficient
- `f_1`: Load-dependent fuel consumption coefficient
- `P_rated`: Diesel generator rated power
- `P_output`: Actual power output

### Hydrogen Mass Balance (per hour)

```
H_new = H_old + E_surplus × eta_EL / H2_LHV - E_shortage / (eta_FC × H2_LHV)

Where:
- E_surplus: Excess renewable generation (kWh)
- E_shortage: Unmet energy demand (kWh)
- eta_EL: Electrolyzer efficiency (70%)
- eta_FC: Fuel cell efficiency (50%)
- H2_LHV: Hydrogen lower heating value (33.3 kWh/kg)
```

### Capital Recovery Factor (CRF)

```
CRF = r(1 + r)^T / ((1 + r)^T - 1)

Where:
- r: Annual discount rate
- T: Project lifetime (years)
```

### Levelized Cost of Energy (LCOE)

```
LCOE = C_total / L_year

Where:
- C_total: Total annualized cost ($/year)
- L_year: Total annual energy demand (kWh)
```

### Loss of Power Supply Probability (LPSP)

```
LPSP = E_unmet / L_year × 100%

Where:
- E_unmet: Total unmet energy (kWh/year)
- L_year: Total load (kWh/year)
```

## 🤝 Contributing & Modifications

### Adding Custom Components

To extend the system with new components:

1. **Add parameters** in `__init__()` method
2. **Create a method** for the component (e.g., `calculate_component_output()`)
3. **Update `simulate_year()`** to include component in hourly loop
4. **Update cost calculations** with capital, O&M, and replacement costs
5. **Update emission calculations** if relevant

### Common Modifications

**Increase PV efficiency to 20%**:
```python
parameters['eta_PV'] = 0.20
```

**Add grid purchase price**:
```python
parameters['p_grid_purchase'] = 0.15  # $/kWh to buy from grid
# Then modify cost tracking in simulate_year()
```

**Adjust hydrogen storage minimum level**:
```python
parameters['H_min_percentage'] = 0.15  # Keep 15% minimum
```

## 📚 References & Resources

- **Hydrogen Energy**: Lower Heating Value (LHV) = 33.3 kWh/kg
- **Diesel Emissions**: 2.6391 kg CO₂ per litre
- **PV Technology**: Typical efficiency 15-22% (varies by type)
- **Wind Turbines**: Power curve depends on blade design
- **Fuel Cells**: Typical efficiency 40-60% (PEM type)
- **Electrolyzers**: Typical efficiency 60-75%

## 📞 Support & Troubleshooting

### Common Issues

**Error: "Data not found"**
- Ensure `data/semi_final_load.xlsx` exists
- Check file path and Excel formatting
- Verify columns exist: `Community Load`, solar data, wind speed

**Error: "Negative capacity"**
- Ensure all `N_*` values in config are non-negative
- Check parameter dictionary for errors

**LPSP too high (>10%)**
- Increase renewable capacity (↑ N_PV, N_WT)
- Increase hydrogen storage (↑ N_H2)
- Increase fuel cell capacity (↑ N_FC)

**Cost too high**
- Reduce system size
- Check efficiency parameters (should be 0-1)
- Verify cost parameters are realistic

## 📄 License & Citation

This project is provided as-is for research and educational purposes.

---

**Last Updated**: March 2026  
**Version**: 2.0 (Corrected with proper unit conversions)  
**Status**: Production Ready
