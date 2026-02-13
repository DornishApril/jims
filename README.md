# Hybrid Energy System Simulation - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Input Requirements](#input-requirements)
4. [Function Parameters](#function-parameters)
5. [Code Structure](#code-structure)
6. [Function Flow](#function-flow)
7. [Output Specifications](#output-specifications)
8. [Electrolyzer & Fuel Cell Logic Explained](#electrolyzer--fuel-cell-logic-explained)
9. [Usage Examples](#usage-examples)

---

## Overview

This is a **year-long hourly simulation** (8760 hours) of a hybrid renewable energy system that combines:
- Solar PV + Wind Turbines (renewable generation)
- Hydrogen Storage System (energy storage via electrolyzer + fuel cell)
- Diesel Generator (backup power)
- Grid Connection (sell excess energy)

**Purpose**: Evaluate any system configuration and return its total cost, emissions, and reliability.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    ENERGY SOURCES                            │
│  ┌──────────┐           ┌──────────┐                        │
│  │ Solar PV │           │   Wind   │                        │
│  │  Panels  │           │ Turbine  │                        │
│  └────┬─────┘           └────┬─────┘                        │
│       │                      │                               │
│       └──────────┬───────────┘                               │
│                  │                                           │
│            Renewable Energy                                  │
│                  │                                           │
│       ┌──────────▼──────────┐                               │
│       │  Is E_RE >= Load?   │                               │
│       └──────────┬──────────┘                               │
│                  │                                           │
│         ┌────────┴─────────┐                                │
│         │                  │                                 │
│    YES (Surplus)      NO (Deficit)                          │
│         │                  │                                 │
│         ▼                  ▼                                 │
│  ┌─────────────┐    ┌─────────────┐                        │
│  │Electrolyzer │    │  Fuel Cell  │                        │
│  │ (make H2)   │    │  (use H2)   │                        │
│  └──────┬──────┘    └──────┬──────┘                        │
│         │                  │                                 │
│         ▼                  ▼                                 │
│  ┌─────────────┐    ┌─────────────┐                        │
│  │   H2 Tank   │    │ Still need  │                        │
│  │  (storage)  │    │   power?    │                        │
│  └──────┬──────┘    └──────┬──────┘                        │
│         │                  │                                 │
│    Still excess?      YES  │                                │
│         │                  ▼                                 │
│         │          ┌──────────────┐                         │
│         │          │    Diesel    │                         │
│         │          │  Generator   │                         │
│         │          └──────┬───────┘                         │
│         │                 │                                  │
│         │            Still need                             │
│         │             power?                                │
│         │                 │                                  │
│         ▼                 ▼                                  │
│  ┌─────────────┐   ┌─────────────┐                         │
│  │  Sell to    │   │   Unmet     │                         │
│  │    Grid     │   │   Demand    │                         │
│  └─────────────┘   └─────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Input Requirements

### 1. **System Configuration** (dict)
This defines the SIZE of each component:

```python
system = {
    'N_PV': 150,      # PV capacity in kW
    'N_WT': 100,      # Wind turbine rated capacity in kW
    'Cap_H2': 200,    # Hydrogen storage capacity in kg
    'Cap_FC': 80,     # Fuel cell maximum power in kW
    'Cap_EL': 80,     # Electrolyzer maximum power in kW
    'Cap_DG': 50,     # Diesel generator capacity in kW
}
```

**What each means**:
- `N_PV`: Total solar panel capacity (e.g., 150 kW = 150 panels × 1 kW each)
- `N_WT`: Total wind turbine capacity when wind is at rated speed
- `Cap_H2`: How many kg of hydrogen can be stored
- `Cap_FC`: Maximum electrical output from fuel cell
- `Cap_EL`: Maximum electrical input to electrolyzer
- `Cap_DG`: Maximum diesel generator output

### 2. **Hourly Data** (pandas DataFrame)
Must contain **8760 rows** (one year of hourly data):

| Required Columns | Description | Units | Example |
|-----------------|-------------|-------|---------|
| `Solar Irradiance (W/sq.m)` OR `Avg Solar Irradiance` | Solar radiation | W/m² | 800 |
| `Wind Speed (m/s)` OR `Avg Wind Speed` | Wind speed | m/s | 5.2 |
| `Community Load` | Electricity demand | kW | 110.79 |
| `RO Load (kWh)` (optional) | Additional load | kW | 0 |

**Example data format**:
```
HR   Community Load   RO Load   Avg Solar Irradiance   Avg Wind Speed
0    110.79          0         0                      3.41
1    92.33           0         0                      3.75
2    88.45           0         50                     4.20
...
8759 105.23          0         0                      3.88
```

---

## Function Parameters

### HybridEnergySystem Class Constructor

```python
HybridEnergySystem(parameters: Dict)
```

The `parameters` dictionary contains **all system constants**. Here's what goes in:

#### **A. Efficiency Parameters**
```python
'eta_PV': 0.15       # PV efficiency (15% = typical silicon panel)
'eta_FC': 16.65      # Fuel cell: kWh electricity OUT per kg H2 IN
'eta_EL': 0.020      # Electrolyzer: kg H2 OUT per kWh electricity IN
```

#### **B. Capital Costs** (one-time purchase price)
```python
'c_PV': 1500         # $/kW of PV capacity
'c_WT': 3000         # $/kW of wind turbine capacity
'c_H2': 500          # $/kg of H2 storage capacity
'c_FC_cap': 2000     # $/kW of fuel cell capacity
'c_EL_cap': 1500     # $/kW of electrolyzer capacity
'c_DG_cap': 400      # $/kW of diesel generator capacity
```

#### **C. Operating Costs** (per kWh of energy processed)
```python
'c_FC': 0.01         # $/kWh cost to RUN the fuel cell
'c_DG': 0.30         # $/kWh cost to RUN the diesel (fuel price)
'c_EL': 0.01         # $/kWh cost to RUN the electrolyzer
```

#### **D. Operation & Maintenance Costs** (annual cost per unit)
```python
'om_PV': 20          # $/kW/year for PV maintenance
'om_WT': 50          # $/kW/year for wind turbine maintenance
'om_H2': 10          # $/kg/year for H2 tank maintenance
'om_FC': 30          # $/kW/year for fuel cell maintenance
'om_EL': 25          # $/kW/year for electrolyzer maintenance
'om_DG': 15          # $/kW/year for diesel generator maintenance
```

#### **E. Emission Factors** (kg CO2 per kWh)
```python
'e_FC': 0.0          # Fuel cell emissions (0 if H2 from renewables)
'e_DG': 0.8          # Diesel generator emissions
'e_EL': 0.0          # Electrolyzer emissions
```

#### **F. Economic Parameters**
```python
'T_life': 20         # Project lifetime in years
'r': 0.05            # Discount rate (5% = 0.05)
'p_grid': 0.08       # Grid electricity selling price in $/kWh
```

#### **G. Technical Parameters**
```python
'A_PV': 6.67         # PV area in m² per kW (for 15% efficiency)
'P_DG_min': 0.3      # Minimum diesel loading (30% of capacity)
```

#### **H. Component Lifetimes** (for replacement cost calculation)
```python
'life_PV': 25        # PV panels last 25 years
'life_WT': 20        # Wind turbines last 20 years
'life_H2': 20        # H2 storage lasts 20 years
'life_FC': 10        # Fuel cells last 10 years (replaced once)
'life_EL': 15        # Electrolyzers last 15 years
'life_DG': 15        # Diesel generators last 15 years
```

---

## Code Structure

### File Organization

```
project/
│
├── simulation.py              # Main simulation engine
│   ├── HybridEnergySystem     # Main class
│   │   ├── __init__()         # Initialize parameters
│   │   ├── wind_power_curve() # Calculate wind turbine output
│   │   ├── calculate_replacement_cost()  # NPV of replacements
│   │   └── simulate_year()    # MAIN SIMULATION FUNCTION
│   │
│   └── example_usage()        # Quick demo
│
├── example_simulation.py      # Complete working examples
│   ├── load_data()            # Load Excel data
│   ├── run_single_simulation() # Run one configuration
│   └── sensitivity_analysis() # Test multiple configurations
│
└── README.md                  # This file
```

### Class Methods Overview

#### 1. `__init__(parameters)`
**Purpose**: Initialize all system constants  
**Input**: Dictionary of parameters  
**Output**: None (stores parameters as instance variables)  
**Called**: Once when creating system object

#### 2. `wind_power_curve(v, rated_power=20.0)`
**Purpose**: Convert wind speed to power output  
**Input**: 
- `v`: Wind speed (m/s)
- `rated_power`: Turbine rated power (kW)

**Output**: Power output (kW)  
**Logic**:
```
If v < 3 m/s OR v > 25 m/s:     → Power = 0 (cut-in/cut-out)
If 3 ≤ v < 12 m/s:              → Power = rated × ((v-3)/(12-3))³
If 12 ≤ v ≤ 25 m/s:             → Power = rated
```

#### 3. `calculate_replacement_cost(system, T_life, r)`
**Purpose**: Calculate present value of all future replacements  
**Input**: 
- `system`: Configuration dict
- `T_life`: Project lifetime
- `r`: Discount rate

**Output**: Total replacement cost ($)  
**Logic**:
- For each component, check if lifetime < project lifetime
- Calculate how many times it needs replacement
- Discount each replacement to present value
- Sum all replacement costs

**Example**: Fuel cell costs $100k, lasts 10 years, project is 20 years
- 1 replacement needed at year 10
- PV of replacement = $100k / (1.05)^10 = $61,391

#### 4. `simulate_year(system, data)` ⭐ **MAIN FUNCTION**
**Purpose**: Simulate 8760 hours and calculate cost/emissions/reliability  
**Input**: 
- `system`: Configuration dict (N_PV, N_WT, etc.)
- `data`: DataFrame with hourly weather/load data

**Output**: Tuple of (C_total, E_total, LPSP)

---

## Function Flow

### High-Level Flow of `simulate_year()`

```
START
  │
  ├─ Extract system configuration (N_PV, N_WT, Cap_H2, etc.)
  ├─ Initialize cumulative variables (C_op=0, E_CO2=0, E_unmet=0, etc.)
  ├─ Initialize hydrogen storage array H[0:8761], H[0] = 50% of Cap_H2
  │
  ├─ FOR each hour t from 0 to 8759:
  │   │
  │   ├─ Get inputs: I[t] (irradiance), v[t] (wind), L[t] (load)
  │   │
  │   ├─ Calculate generation:
  │   │   ├─ E_PV = eta_PV × A_PV × I[t] × N_PV
  │   │   ├─ E_WT = wind_power_curve(v[t]) × N_WT
  │   │   └─ E_RE = E_PV + E_WT
  │   │
  │   ├─ Calculate net power: E_net = E_RE - L[t]
  │   │
  │   ├─ IF E_net < 0 (DEFICIT):
  │   │   └─ Call DEFICIT_HANDLING()
  │   │
  │   ├─ ELSE IF E_net > 0 (SURPLUS):
  │   │   └─ Call SURPLUS_HANDLING()
  │   │
  │   └─ ELSE (E_net == 0):
  │       └─ H[t+1] = H[t]
  │
  ├─ Calculate LPSP = E_unmet / L_year
  │
  ├─ Calculate costs:
  │   ├─ C_cap = sum of all capital costs
  │   ├─ C_om = sum of all O&M costs × T_life
  │   ├─ C_rep = calculate_replacement_cost()
  │   ├─ CRF = (r(1+r)^T) / ((1+r)^T - 1)
  │   └─ C_total = (C_cap + C_rep) × CRF + C_om + C_op
  │
  └─ RETURN (C_total, E_total, LPSP)
END
```

### Detailed Deficit Handling Logic

```
DEFICIT_HANDLING(E_deficit, H[t]):
  │
  ├─ IF H[t] > H_min (hydrogen available):
  │   │
  │   ├─ Calculate P_FC_limit = min(H[t] × eta_FC, Cap_FC)
  │   │
  │   ├─ IF E_deficit ≤ P_FC_limit:
  │   │   ├─ E_FC = E_deficit
  │   │   ├─ H_consumed = E_FC / eta_FC
  │   │   ├─ H[t+1] = H[t] - H_consumed
  │   │   ├─ C_op += c_FC × E_FC
  │   │   ├─ E_CO2 += e_FC × E_FC
  │   │   └─ DONE (deficit fully met)
  │   │
  │   ├─ ELSE (fuel cell at maximum, still need power):
  │   │   │
  │   │   ├─ E_FC = P_FC_limit
  │   │   ├─ H_consumed = E_FC / eta_FC
  │   │   ├─ E_remaining = E_deficit - E_FC
  │   │   │
  │   │   ├─ IF E_remaining in [P_DG_min × Cap_DG, Cap_DG]:
  │   │   │   ├─ E_DG = E_remaining
  │   │   │   ├─ H[t+1] = H[t] - H_consumed
  │   │   │   ├─ C_op += c_FC × E_FC + c_DG × E_DG
  │   │   │   ├─ E_CO2 += e_FC × E_FC + e_DG × E_DG
  │   │   │   │
  │   │   │   ├─ E_total = E_RE + E_FC + E_DG
  │   │   │   ├─ E_excess = E_total - L[t]
  │   │   │   │
  │   │   │   ├─ IF E_excess > 0:
  │   │   │   │   ├─ E_grid += E_excess
  │   │   │   │   └─ C_op -= p_grid × E_excess (revenue)
  │   │   │   │
  │   │   │   └─ ELSE:
  │   │   │       └─ E_unmet += abs(E_excess)
  │   │   │
  │   │   └─ ELSE (diesel can't help):
  │   │       ├─ H[t+1] = H[t] - H_consumed
  │   │       ├─ E_unmet += E_remaining
  │   │       ├─ C_op += c_FC × E_FC
  │   │       └─ E_CO2 += e_FC × E_FC
  │
  └─ ELSE (no hydrogen available):
      ├─ H[t+1] = H[t]
      └─ E_unmet += E_deficit
```

### Detailed Surplus Handling Logic

```
SURPLUS_HANDLING(E_surplus, H[t]):
  │
  ├─ IF E_surplus == 0:
  │   └─ H[t+1] = H[t]
  │
  ├─ ELSE IF H[t] < H_max (storage not full):
  │   │
  │   ├─ H_space = H_max - H[t]
  │   │
  │   ├─ E_EL_limit = min(E_surplus, Cap_EL, H_space / eta_EL)
  │   │
  │   ├─ E_EL = E_EL_limit
  │   ├─ H_produced = E_EL × eta_EL
  │   ├─ H[t+1] = H[t] + H_produced
  │   │
  │   ├─ C_op += c_EL × E_EL
  │   ├─ E_CO2 += e_EL × E_EL
  │   │
  │   ├─ E_leftover = E_surplus - E_EL
  │   │
  │   └─ IF E_leftover > 0:
  │       ├─ E_grid += E_leftover
  │       └─ C_op -= p_grid × E_leftover (revenue)
  │
  └─ ELSE (storage is full):
      ├─ H[t+1] = H[t]
      ├─ E_grid += E_surplus
      └─ C_op -= p_grid × E_surplus (sell all to grid)
```

---

## Output Specifications

### Return Values

```python
C_total, E_total, LPSP = system.simulate_year(config, data)
```

#### 1. `C_total` (float)
**Total Annualized Cost** in $/year

**Components**:
```
C_total = (C_cap + C_rep) × CRF + C_om + C_op
```

Where:
- **C_cap**: Initial capital cost
  ```
  C_cap = c_PV × N_PV 
        + c_WT × N_WT 
        + c_H2 × Cap_H2 
        + c_FC_cap × Cap_FC 
        + c_EL_cap × Cap_EL 
        + c_DG_cap × Cap_DG
  ```

- **C_rep**: Present value of all replacements over project lifetime

- **CRF**: Capital Recovery Factor (converts lump sum to annuity)
  ```
  CRF = [r × (1+r)^T_life] / [(1+r)^T_life - 1]
  ```

- **C_om**: Total O&M costs over lifetime
  ```
  C_om = (om_PV × N_PV 
        + om_WT × N_WT 
        + om_H2 × Cap_H2 
        + om_FC × Cap_FC 
        + om_EL × Cap_EL 
        + om_DG × Cap_DG) × T_life
  ```

- **C_op**: Annual operating cost (accumulated over 8760 hours)
  - Includes: fuel costs, electrolyzer operation
  - Minus: grid revenue from selling excess

**Example**: $285,432/year means this system costs $285k annually to own and operate

#### 2. `E_total` (float)
**Total Annual CO2 Emissions** in kg/year

```
E_total = E_CO2 (accumulated over 8760 hours)
```

**Sources**:
- Fuel cell operation: `e_FC × E_FC` (usually 0 if H2 from renewables)
- Diesel generator: `e_DG × E_DG`
- Electrolyzer: `e_EL × E_EL` (usually 0)

**Example**: 15,234 kg CO2/year

#### 3. `LPSP` (float)
**Loss of Power Supply Probability** (0 to 1)

```
LPSP = E_unmet / L_year
```

Where:
- **E_unmet**: Total unmet energy over the year (kWh)
- **L_year**: Total annual load demand (kWh)

**Interpretation**:
- `LPSP = 0.00`: Perfect reliability (100% of demand met)
- `LPSP = 0.01`: 99% reliable (1% unmet)
- `LPSP = 0.05`: 95% reliable (5% unmet)
- `LPSP = 0.10`: 90% reliable (10% unmet)

**Typical target**: LPSP ≤ 0.05 (95% reliability or better)

---

## Electrolyzer & Fuel Cell Logic Explained

### The Hydrogen Energy Storage System

Think of hydrogen storage as a **rechargeable battery**, but instead of storing electrons, you're storing hydrogen gas:

```
┌─────────────────────────────────────────────────────────┐
│                  HYDROGEN STORAGE SYSTEM                 │
│                                                          │
│  CHARGING (Surplus Energy):                             │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐     │
│  │Excess    │      │          │      │  H2 Gas  │     │
│  │Renewable │─────▶│Electro-  │─────▶│ Storage  │     │
│  │Energy    │ kWh  │ lyzer    │  kg  │  Tank    │     │
│  └──────────┘      └──────────┘      └──────────┘     │
│                                                          │
│  DISCHARGING (Deficit Energy):                          │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐     │
│  │  H2 Gas  │      │          │      │Electric  │     │
│  │ Storage  │─────▶│  Fuel    │─────▶│ Power    │     │
│  │  Tank    │  kg  │  Cell    │ kWh  │          │     │
│  └──────────┘      └──────────┘      └──────────┘     │
└─────────────────────────────────────────────────────────┘
```

---

### Part 1: Electrolyzer (Making Hydrogen)

**When does it run?** When you have MORE renewable energy than the load needs (surplus).

**What does it do?** Converts excess electricity into hydrogen gas for storage.

**The Chemical Process**:
```
Electricity + Water (H2O) → Hydrogen gas (H2) + Oxygen (O2)
```

**The Math**:
```python
# Input: E_EL kWh of electricity
# Output: H_produced kg of hydrogen

H_produced = E_EL × eta_EL

# Example with eta_EL = 0.020 kg/kWh:
# If E_EL = 100 kWh
# H_produced = 100 × 0.020 = 2 kg of H2
```

**What limits the electrolyzer?**

Three constraints (it picks the SMALLEST):

1. **Available surplus energy**: Can't use more than you have
   ```
   E_EL ≤ E_surplus
   ```

2. **Electrolyzer capacity**: Machine has maximum power rating
   ```
   E_EL ≤ Cap_EL
   ```

3. **Storage space**: Can't make more H2 than tank can hold
   ```
   H_produced ≤ (H_max - H[t])
   Therefore: E_EL ≤ (H_max - H[t]) / eta_EL
   ```

**Code Implementation**:
```python
if H[t] < H_max:  # Storage not full
    H_space = H_max - H[t]
    
    # Find limiting constraint
    E_EL_limit = min(E_surplus, Cap_EL, H_space / eta_EL)
    
    # Run electrolyzer
    E_EL = E_EL_limit
    H_produced = E_EL × eta_EL
    
    # Update storage
    H[t+1] = H[t] + H_produced
    
    # Track costs
    C_op += c_EL × E_EL  # Operating cost
    E_CO2 += e_EL × E_EL  # Emissions (usually 0)
```

**Real Example**:
```
Hour 1200: Sunny day, high solar generation
- Solar produces: 180 kW
- Load needs: 100 kW
- Surplus: 80 kW

Storage status:
- Current H2: H[1200] = 150 kg
- Maximum H2: H_max = 200 kg
- Space available: 50 kg

Electrolyzer constraints:
- Surplus available: 80 kW ✓
- Electrolyzer capacity: Cap_EL = 100 kW ✓
- Storage limit: 50 kg ÷ 0.020 kg/kWh = 2500 kW ✓

Limiting factor: 80 kW (surplus)

Result:
- E_EL = 80 kW consumed
- H_produced = 80 × 0.020 = 1.6 kg made
- H[1201] = 150 + 1.6 = 151.6 kg
- No leftover energy (all surplus used)
```

---

### Part 2: Fuel Cell (Using Hydrogen)

**When does it run?** When renewables can't meet the load (deficit).

**What does it do?** Converts stored hydrogen back into electricity.

**The Chemical Process**:
```
Hydrogen gas (H2) + Oxygen (O2) → Electricity + Water (H2O) + Heat
```

**The Math**:
```python
# Input: H_consumed kg of hydrogen
# Output: E_FC kWh of electricity

E_FC = H_consumed × eta_FC

# Example with eta_FC = 16.65 kWh/kg:
# If H_consumed = 2 kg
# E_FC = 2 × 16.65 = 33.3 kWh
```

**Understanding eta_FC = 16.65 kWh/kg**:

Hydrogen has energy content (Lower Heating Value) = 33.3 kWh/kg

But fuel cells aren't 100% efficient. Typical efficiency = 50%

So: eta_FC = 33.3 kWh/kg × 0.50 = 16.65 kWh/kg

This means:
- 1 kg of H2 → produces 16.65 kWh of electricity
- To get 100 kWh → need 100 ÷ 16.65 = 6 kg of H2

**What limits the fuel cell?**

Two constraints (it picks the SMALLEST):

1. **Available hydrogen**: Can't use more than you have stored
   ```
   E_FC ≤ H[t] × eta_FC
   ```
   (Also respect minimum level: H[t] > H_min)

2. **Fuel cell capacity**: Machine has maximum power rating
   ```
   E_FC ≤ Cap_FC
   ```

**Code Implementation**:
```python
if H[t] > H_min:  # Hydrogen available
    # Find maximum FC can provide
    P_FC_limit = min(H[t] × eta_FC, Cap_FC)
    
    if E_deficit <= P_FC_limit:
        # FC can cover entire deficit
        E_FC = E_deficit
        H_consumed = E_FC / eta_FC
        H[t+1] = H[t] - H_consumed
        
        # Track costs and emissions
        C_op += c_FC × E_FC
        E_CO2 += e_FC × E_FC
        
    else:
        # FC runs at maximum, but not enough
        E_FC = P_FC_limit
        H_consumed = E_FC / eta_FC
        E_remaining = E_deficit - E_FC
        
        # Try diesel generator next...
        # (see deficit handling logic above)
```

**Real Example**:
```
Hour 2300: Night, no solar, low wind
- Solar produces: 0 kW
- Wind produces: 20 kW
- Load needs: 100 kW
- Deficit: 80 kW

Storage status:
- Current H2: H[2300] = 151.6 kg
- Minimum H2: H_min = 20 kg (10% of 200 kg)

Fuel cell constraints:
- Hydrogen available: 151.6 kg × 16.65 kWh/kg = 2524 kWh worth
- Fuel cell capacity: Cap_FC = 80 kW

Limiting factor: 80 kW (capacity)

Check if FC can meet deficit:
- Deficit = 80 kW
- P_FC_limit = 80 kW
- 80 ≤ 80 ✓ (can meet entire deficit!)

Result:
- E_FC = 80 kW produced
- H_consumed = 80 ÷ 16.65 = 4.8 kg used
- H[2301] = 151.6 - 4.8 = 146.8 kg
- Deficit fully met!
```

---

### Part 3: Round-Trip Efficiency (The Energy Loss)

**This is critical to understand**: You lose energy in the conversion process!

**Going around the loop**:
```
Start with 100 kWh of excess solar
  ↓
Electrolyzer (70% efficient)
  → Makes: 100 × 0.020 = 2 kg H2
  ↓
Store in tank (100% efficient, ignoring leakage)
  → Still have: 2 kg H2
  ↓
Fuel Cell (50% efficient)
  → Makes: 2 × 16.65 = 33.3 kWh
  ↓
End with 33.3 kWh of electricity
```

**Round-trip efficiency**: 33.3 kWh out ÷ 100 kWh in = **33.3%**

**You lost 66.7% of the energy!** This is why hydrogen storage is expensive from an energy perspective.

**The Math Behind Efficiencies**:

```python
# Electrolyzer efficiency (70%):
eta_EL = 0.70 / 33.3 kWh/kg = 0.021 kg/kWh
# "For every kWh I put in, I get 0.021 kg of H2"

# Fuel cell efficiency (50%):
eta_FC = 0.50 × 33.3 kWh/kg = 16.65 kWh/kg
# "For every kg of H2 I consume, I get 16.65 kWh out"

# Round-trip:
1 kWh → 0.021 kg H2 → 0.021 × 16.65 = 0.35 kWh
# Lost: 1 - 0.35 = 0.65 (65% loss)
```

---

### Part 4: Why This System Design?

**Q: Why not just use batteries?**

A: Batteries are better for short-term (hours), hydrogen for long-term (days/weeks):
- Batteries: 85-95% round-trip efficiency, but expensive for large capacity
- Hydrogen: 30-40% round-trip efficiency, but cheap for large capacity

**Q: When does the electrolyzer run most?**

A: Midday when solar is highest and load might be lower:
```
Hour 1200-1500: Peak solar production
- PV might produce 150-200 kW
- Load might be 80-120 kW
- Surplus of 50-100 kW → perfect for electrolyzer
```

**Q: When does the fuel cell run most?**

A: Night and early morning when no solar:
```
Hour 0100-0600: No solar, low wind
- PV produces 0 kW
- Wind might produce 20-40 kW
- Load might be 80-100 kW
- Deficit of 40-80 kW → need fuel cell
```

**Q: What happens if both electrolyzer AND fuel cell can't handle everything?**

A: Priority cascade:
1. **Surplus**:
   - First: Electrolyzer (store as H2)
   - Then: Sell to grid (get revenue)

2. **Deficit**:
   - First: Fuel cell (use stored H2)
   - Then: Diesel generator (expensive, polluting)
   - Finally: Unmet demand (LPSP goes up)

---

### Part 5: Storage State Tracking

The hydrogen tank level changes every hour:

```python
# Initialize (start of simulation)
H[0] = 0.5 × Cap_H2  # Start at 50% full

# Every hour:
FOR t = 0 to 8759:
    if SURPLUS:
        H[t+1] = H[t] + H_produced  # Add hydrogen
    
    elif DEFICIT:
        H[t+1] = H[t] - H_consumed  # Remove hydrogen
    
    else:
        H[t+1] = H[t]  # No change
    
    # Enforce limits
    H[t+1] = max(0, min(H[t+1], H_max))
```

**Important constraints**:
- **Never below H_min**: Keep 10% reserve (safety margin)
- **Never above H_max**: Physical tank limit
- **State dependent**: Can't use H2 if you don't have it!

**Example Timeline**:
```
Hour    Event               H2 Level    Change
0       Start               100.0 kg    (50% of 200 kg)
1       Surplus +2.0 kg     102.0 kg    +2.0
2       Surplus +1.5 kg     103.5 kg    +1.5
3       Balanced            103.5 kg     0.0
4       Deficit -3.2 kg     100.3 kg    -3.2
5       Deficit -4.8 kg     95.5 kg     -4.8
...
8760    End                 98.3 kg     (varies)
```

---

## Usage Examples

### Example 1: Basic Simulation

```python
from simulation import HybridEnergySystem
import pandas as pd

# Step 1: Define parameters
params = {
    'eta_PV': 0.15, 'eta_FC': 16.65, 'eta_EL': 0.020,
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

# Step 2: Create system
system = HybridEnergySystem(params)

# Step 3: Define configuration
config = {
    'N_PV': 150,
    'N_WT': 100,
    'Cap_H2': 200,
    'Cap_FC': 80,
    'Cap_EL': 80,
    'Cap_DG': 50,
}

# Step 4: Load data
data = pd.read_excel('data/Load.xlsx')

# Step 5: Run simulation
cost, emissions, lpsp = system.simulate_year(config, data)

# Step 6: Display results
print(f"Cost: ${cost:,.2f}/year")
print(f"Emissions: {emissions:,.2f} kg CO2/year")
print(f"Reliability: {(1-lpsp)*100:.2f}%")
```

### Example 2: Compare Multiple Configurations

```python
configs = [
    {'N_PV': 100, 'N_WT': 50, 'Cap_H2': 100, 'Cap_FC': 50, 'Cap_EL': 50, 'Cap_DG': 30},
    {'N_PV': 150, 'N_WT': 100, 'Cap_H2': 200, 'Cap_FC': 80, 'Cap_EL': 80, 'Cap_DG': 50},
    {'N_PV': 200, 'N_WT': 150, 'Cap_H2': 300, 'Cap_FC': 100, 'Cap_EL': 100, 'Cap_DG': 50},
]

for i, config in enumerate(configs):
    cost, emissions, lpsp = system.simulate_year(config, data)
    print(f"\nConfig {i+1}:")
    print(f"  Cost: ${cost:,.0f}/year")
    print(f"  Emissions: {emissions:,.0f} kg CO2/year")
    print(f"  LPSP: {lpsp*100:.3f}%")
```

### Example 3: Find Minimum Cost for Target Reliability

```python
import numpy as np

target_lpsp = 0.05  # 95% reliability

best_cost = float('inf')
best_config = None

# Grid search
for pv in range(50, 251, 50):
    for wt in range(50, 151, 50):
        for h2 in range(100, 301, 100):
            config = {
                'N_PV': pv,
                'N_WT': wt,
                'Cap_H2': h2,
                'Cap_FC': int(0.4 * h2),
                'Cap_EL': int(0.4 * h2),
                'Cap_DG': 50,
            }
            
            cost, emissions, lpsp = system.simulate_year(config, data)
            
            if lpsp <= target_lpsp and cost < best_cost:
                best_cost = cost
                best_config = config

print(f"Best configuration: {best_config}")
print(f"Cost: ${best_cost:,.2f}/year")
```

---

## Summary

This simulation provides a **complete techno-economic evaluation** of hybrid renewable energy systems with hydrogen storage. It:

1. Takes in system sizing and hourly weather/load data
2. Simulates every hour of the year following realistic operation logic
3. Returns cost, emissions, and reliability metrics
4. Can be integrated into optimization algorithms (NSGA-II) to find optimal designs

The key insight is the **electrolyzer-fuel cell-storage trio** acts as a long-duration energy storage system, converting surplus renewable energy into hydrogen for later use during deficit periods.
