# Paper Summary: Assessing the 3E performance of multiple energy supply scenarios based on photovoltaic, wind turbine, battery and hydrogen systems

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Assessing the 3E performance of multiple energy supply scenarios based on photovoltaic, wind turbine, battery and hydrogen systems
- **Authors:** Y. Elaouzy, A. El Fadar (corresponding author), O.B. Achkari
- **Affiliation:** Laboratory of Innovative Technologies, National School of Applied Sciences of Tangier, Abdelmalek Essaadi University, Tetouan, Morocco
- **Journal/Conference name:** Journal of Energy Storage (Elsevier)
- **Year of publication:** 2024
- **DOI:** https://doi.org/10.1016/j.est.2024.113378
- **Article number:** 113378, Volume 99
- **Received:** 1 April 2024; Revised: 28 July 2024; Accepted: 13 August 2024; Available online: 17 August 2024
- **Study location:** Tangier, Morocco (Mediterranean climate)
- **System type:** Grid-connected residential building powered by PV-Wind hybrid, with three energy supply scenarios: (1) direct supply + grid injection, (2) PV-Wind + battery storage, (3) PV-Wind + hydrogen storage (PEM electrolyzer + PEM fuel cell + compressed H2 tank)
- **Study type:** Simulation-based (no experimental component)
- **Software/tools used:** EnergyPlus (building energy simulation, HVAC, wind turbine modeling), PVsyst (PV system simulation), SketchUp (building geometry), OpenStudio plugin, numerical models for hydrogen/battery storage
- **Optimization method:** No formal optimization algorithm; comparative scenario analysis with three pre-defined energy supply scenarios (ESSs). Component sizing was based on consultations with local market and prior literature.

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

**PV System:**
- Number of PV panels: 24 panels (12 series x 2 parallel)
- Panel dimensions: 2278 x 1134 x 35 mm
- Maximum panel efficiency: 21.32%
- Total PV capacity: 13.2 kWp
- Array slope: 31 degrees
- Array azimuth: 0 degrees (south-facing)
- Installation: Entire building roof
- Inverter nominal power: 10 kW
- Maximum PV power allowed by inverter: 15 kW
- Maximum inverter efficiency: 97.8%

**Wind Turbine (WT) System:**
- Type: Horizontal axis, 3 blades
- Rated power: 7.5 kW
- Rotor diameter: 6.3 m
- Rated rotor speed: 200 rev/min
- Rated wind speed: 12 m/s
- Cut-in wind speed: 3 m/s
- Cut-out wind speed: 20 m/s
- Annual local wind speed: 4.9 m/s

**Battery System (ESS 2 only):**
- Type: Li-ion
- Rated capacity: 45 kWh
- Charging/discharging efficiency: 90%

**Hydrogen System (ESS 3 only):**
- Electrolyzer type: PEM (Proton Exchange Membrane)
- Electrolyzer rated capacity: 14 kW
- Electrolyzer mean electrical conversion efficiency: 70%
- Hydrogen storage type: Compressed gas
- Hydrogen storage tank capacity: 2.7 kg
- Density of stored hydrogen: 7.7 kg/m^3
- Lower heating value of hydrogen (LHV): 33.33 kWh/kg
- Fuel cell type: PEM
- Fuel cell rated capacity: 14 kW
- Fuel cell mean electrical conversion efficiency: 40%
- Heat exchanger capacity: 10 kW

**Building Energy Systems:**
- Heat pump with direct expansion coils for space heating and cooling
- Electric stratified water heater with hot water storage tank
- Cooling/heating setpoint: 26/20 degrees C

### 2.2 Total System Capacity

- **Total generation capacity:** 13.2 kWp (PV) + 7.5 kW (WT) = 20.7 kW
- **Total storage capacity:** 45 kWh (battery, ESS 2) OR 2.7 kg H2 (ESS 3)
- **Total conversion capacity:** 14 kW (electrolyzer) + 14 kW (fuel cell) + 10 kW (inverter) = 38 kW (ESS 3); 10 kW inverter (ESS 1 and 2)

### 2.3 Component Costs (Capital, Replacement, O&M)

| Component | CAPEX | Lifetime | Source |
|-----------|-------|----------|--------|
| PV system | $800/kW | 25 years | Local market |
| Battery | $150/kWh | 10 years | [45] |
| Wind Turbine | $1325/kW | 25 years | [24] |
| Electrolyzer | $1200/kW | 20 years | [53] |
| Hydrogen tank | $378/kgH2 | 25 years | [54] |
| Fuel cells | $1000/kW | 10 years | [55] |
| Heat exchanger | $500 (total) | 15 years | Local market |

- **Annual OPEX:** 2% of CAPEX for all systems [58]

### 2.4 Economic Parameters

- **Discount rate:** 3% [56]
- **Electricity purchase price:** $0.116/kWh [57]
- **Electricity sell-to-grid price:** 80% of purchase price = $0.0928/kWh [47]
- **Project lifetime:** Not explicitly stated as a single value; component lifetimes range 10-25 years
- **Currency:** USD (no year specified, assumed 2023-2024)
- **Inflation rate:** Not mentioned
- **Fuel price:** Not applicable (no diesel generator in this study)

### 2.5 Resource Data

- **Location:** Tangier, Morocco (Mediterranean climate)
- **Solar irradiance:** Average daily productivity of 5.44 Wh/Wp/day (from PVsyst simulation)
- **Wind speed:** Annual average 4.9 m/s at hub height
- **Climate characteristics:** Predominance of cooling over heating demand; Mediterranean climate with hot summers and mild winters
- **Data source:** EnergyPlus weather data for Tangier; PVsyst database

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

| Metric | ESS 1 (Direct+Grid) | ESS 2 (Battery) | ESS 3 (Hydrogen) |
|--------|---------------------|-----------------|------------------|
| **LCOE** | $0.05/kWh | $0.09/kWh | $0.21/kWh |
| **SPP (Simple Payback Period)** | 5.80 years | 7.89 years | 16.30 years |
| **DPP (Discounted Payback Period)** | 6.46 years | 9.13 years | 22.71 years |
| **SIR (Savings-to-Investment Ratio)** | 2.26 | 1.44 | 0.66 |

- **LCOH (Levelized Cost of Hydrogen):** Approximately $5.3/kg (for ESS 3)
- **NPC:** Not explicitly stated as a single dollar value
- **Initial capital cost:** Not explicitly stated as a single dollar value
- **Operating cost (per year):** Not explicitly stated
- **Payback period:** See SPP/DPP above
- **IRR/ROI:** Not reported

### 3.2 Reliability Metrics

| Metric | ESS 1 | ESS 2 | ESS 3 |
|--------|-------|-------|-------|
| **ECR (Energy Coverage Ratio)** | 52.56% | 100% | 100% |

- **LPSP:** Not explicitly reported
- **LOLP:** Not reported
- **Unmet load:** Not explicitly quantified in kWh/year
- **System availability:** Not explicitly reported

### 3.3 Generation Metrics

**Annual Electricity Generation by Source:**
- **PV system:** 26,238.44 kWh/year (productivity: 1988 Wh/Wp/year)
- **WT system:** 8,432.49 kWh/year (1,124.33 kWh per kW of rated power)
- **Total renewable generation:** 34,670.93 kWh/year

**Maximum Hourly Power Output:**
- PV system: 12.11 kW
- WT system: 6.26 kW

**Energy Fed into the Grid (annual):**
- ESS 1: 20,935 kWh/year
- ESS 2: 4,558 kWh/year
- ESS 3: 2,255 kWh/year

**Battery Throughput (ESS 2):**
- Charged: 18,842 kWh/year
- Discharged: 16,957 kWh/year

**Hydrogen System (ESS 3):**
- Hydrogen produced: 440 kg/year (equivalent to 14,655 kWh/year of energy)
- Fuel cell electricity output: 5,862 kWh/year
- Fuel cell heat output: 8,793 kWh/year

**Renewable Fraction:** Not explicitly stated as a single metric (but ECR values indicate coverage)

**Excess Electricity:** Not explicitly stated as a separate metric

### 3.4 Load Metrics

- **Total annual load demand:** Not explicitly stated as a single number, but can be derived (see Section 5)
- **Average daily load for household equipment (per floor):** 5.57 kWh/day
- **Number of floors:** 3
- **Total household equipment daily load:** 5.57 x 3 = 16.71 kWh/day
- **Peak load:** Not explicitly stated
- **Average load:** Not explicitly stated
- **Load profile type:** Residential building (3 floors, 4 occupants per floor = 12 total occupants)
- **Building total floor area:** 396 m^2
- **Building volume:** 1,108.8 m^3
- **Water consumption:** 102.28 m^3/year

### 3.5 Optimal Configuration

- **Optimization performed:** No formal optimization algorithm was used. The study compares three pre-defined scenarios.
- **Objective:** Comparative 3E (energy, environmental, economic) analysis
- **Sensitivity analysis:** Not reported
- **Constraints:** ECR target of 100% for ESS 2 and ESS 3

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

- **Type of dispatch:** Rule-based energy balance (no sophisticated control algorithm)
- **Priority order:**
  1. PV and WT systems generate electricity based on available solar radiation and wind
  2. Generated electricity is first used to directly supply building loads
  3. Surplus electricity is handled differently per scenario:
     - ESS 1: Injected into the grid
     - ESS 2: Stored in batteries
     - ESS 3: Supplied to PEM electrolyzer for hydrogen production
  4. Deficit (when generation < load) is handled:
     - ESS 1: Imported from the grid
     - ESS 2: Discharged from batteries
     - ESS 3: Fuel cell converts stored hydrogen back to electricity

### 4.2 Power Flow Logic

**Surplus handling:**
- ESS 1: Surplus electricity injected directly to grid
- ESS 2: Surplus charges battery (E_ch = E_gen - E_req)
- ESS 3: Surplus powers PEM electrolyzer to produce hydrogen (stored as compressed gas at 7.7 kg/m^3)

**Deficit handling:**
- ESS 1: Deficit covered by grid import
- ESS 2: Deficit covered by battery discharge (E_dis = E_req - E_gen)
- ESS 3: Deficit covered by PEM fuel cell converting stored hydrogen to electricity + waste heat

**Battery charging/discharging logic:**
- Charging: E_{t+dt}^{stor} = E_t^{stor} + E_ch x eta_B-ch x dt
- Discharging: E_{t+dt}^{stor} = E_t^{stor} - (E_disch x dt) / eta_B-disch
- Charging efficiency: 90%
- Discharging efficiency: 90%

**Hydrogen production and consumption logic:**
- Electrolyzer: E_ele = m_H2 x LHV_H2 / eta_ele
- Fuel cell power: E_FC = m_H2 x LHV_H2 x eta_FC
- Fuel cell heat: Q_FC = E_FC x ((1 - eta_FC) / eta_FC)

**Grid interaction:**
- Grid-connected in all three scenarios
- Electricity sold to grid at 80% of purchase price
- Grid serves as backup for deficits (ESS 1) and as sink for excess (all scenarios)

### 4.3 Control Parameters

- **Battery SOC minimum (SoCmin):** Defined in equations but exact value not stated in the text
- **Battery rated capacity:** 45 kWh
- **Battery charging/discharging efficiency:** 90%
- **Electrolyzer efficiency:** 70%
- **Fuel cell electrical efficiency:** 40%
- **Inverter maximum efficiency:** 97.8%
- **PV cell efficiency at STC:** 21.32%
- **PV temperature coefficient (beta):** Used in Eq. (5) but value not explicitly stated
- **Performance ratio of PV system:** 83.92%
- **Wind turbine capacity factor:** Calculated via Eq. (3) but value not explicitly stated
- **Battery autonomy (Baut):** Calculated via Eq. (14) but value not explicitly stated

### 4.4 Algorithm Flow

The simulation follows these steps (from Fig. 4):

1. **Building modeling:** Design reference building in SketchUp + OpenStudio
2. **Energy demand calculation:** Export to EnergyPlus; calculate HVAC + water heating + electrical equipment loads
3. **PV system simulation:** Model in PVsyst to get annual energy yield
4. **WT system simulation:** Model in EnergyPlus using Generator:WindTurbine object
5. **Energy balance:** Compare generation vs. load at each time step
6. **Storage modeling:** Apply mathematical models (Eqs. 7-14) for battery or hydrogen storage
7. **Grid interaction:** Calculate surplus injected or deficit imported
8. **Performance evaluation:** Compute ECR, CPBP, CER, SPP, DPP, SIR, LCOE metrics

**Power balance equation (implicit):**
E_gen (PV + WT) + E_storage_discharge + E_grid_import = E_load + E_storage_charge + E_grid_export + Losses

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

This study examines a typical three-story residential building in Tangier, Morocco, with a total floor area of 396 m^2, 12 occupants (4 per floor), and a total annual energy demand that can be derived from the reported data. The building is equipped with a 13.2 kWp PV system and a 7.5 kW wind turbine, giving a combined generation capacity of 20.7 kW.

**Typical day — Morning:**
As solar radiation begins around 6-7 AM, the PV system starts generating electricity. During early morning hours, solar output is modest (perhaps 2-4 kW depending on season), while the wind turbine contributes based on prevailing wind conditions (annual average 4.9 m/s). The building's morning load includes household equipment (16.71 kWh/day total across 3 floors, or about 0.7 kW average) plus any HVAC demand. In the Mediterranean climate of Tangier, heating demand is relatively low compared to cooling. If generation exceeds load, the surplus is either injected to the grid (ESS 1), stored in batteries (ESS 2), or used for electrolysis (ESS 3).

**Midday — Peak solar:**
The PV system reaches its maximum hourly output of 12.11 kW during peak sun hours. Combined with wind turbine output (up to 6.26 kW maximum), total generation can reach approximately 18 kW or more. This is well above the building's average load, creating significant surplus. In ESS 1, this surplus is injected directly into the grid (annual total: 20,935 kWh). In ESS 2, the battery absorbs the excess (18,842 kWh charged annually). In ESS 3, the electrolyzer converts surplus electricity to hydrogen (440 kg/year produced).

**Evening — Solar drops, load peaks:**
As solar radiation diminishes after 4-5 PM, PV output drops rapidly. Evening hours often coincide with peak residential loads (cooking, lighting, entertainment, HVAC). The wind turbine may continue generating if wind conditions are favorable. In ESS 1, any deficit is covered by grid import (annual shortage: 12,399.86 kWh). In ESS 2, the battery discharges to cover the shortfall (16,957 kWh discharged annually). In ESS 3, the fuel cell converts stored hydrogen back to electricity (5,862 kWh/year from FC).

**Night:**
PV generates zero output at night. The wind turbine may continue operating. Battery (ESS 2) or fuel cell (ESS 3) must cover nighttime deficits. The hydrogen system's fuel cell also produces 8,793 kWh/year of waste heat, which can be harnessed for water heating or space heating — a meaningful co-generation benefit that batteries cannot provide.

**Seasonal variations:**
The paper notes that HVAC demand is significantly higher in summer than winter (cooling-dominated climate). The energy shortage in ESS 1 increases significantly during hours 4425-6324 (summer period), attributed to elevated cooling demand. Solar generation is also highest in summer, partially offsetting the increased load. Winter sees lower cooling demand but also reduced solar generation.

### 5.2 System Behavior Analysis

**Why ESS 1 (direct supply + grid) performs best economically:**
The first scenario achieves the lowest LCOE ($0.05/kWh), shortest payback (5.80 years), and highest SIR (2.26) because it avoids the capital costs of energy storage equipment. By using the grid as a virtual battery — importing during deficits and exporting during surpluses — the system achieves high economic efficiency. The sell price (80% of purchase price) creates a small penalty for exported energy, but the avoided storage CAPEX more than compensates.

**Why ESS 2 (battery) achieves 100% ECR:**
The 45 kWh Li-ion battery with 90% round-trip efficiency is sufficient to store enough surplus renewable energy to cover all nighttime and low-generation periods. The annual charge/discharge cycle (18,842/16,957 kWh) indicates approximately 445 equivalent full cycles per year (16,957/45 = 377 cycles), which is just over 1 cycle per day — reasonable for a Li-ion system. The battery's high efficiency (90%) means only 10% energy loss during storage, compared to much higher losses in the hydrogen pathway.

**Why ESS 3 (hydrogen) is not economically viable:**
The hydrogen pathway suffers from three compounding inefficiencies: (1) the electrolyzer converts electricity to hydrogen at only 70% efficiency, (2) the fuel cell converts hydrogen back to electricity at only 40% efficiency, and (3) the overall round-trip efficiency is only 0.70 x 0.40 = 28%. This means 72% of the surplus electricity is lost in the storage process. Combined with high CAPEX for electrolyzer ($1200/kW), hydrogen tank ($378/kg), and fuel cells ($1000/kW), the LCOE reaches $0.21/kWh — more than double the battery scenario and more than 4x the direct-supply scenario.

**Trade-offs identified by the authors:**
- Energy independence (100% ECR) comes at a cost: ESS 2 and 3 achieve full coverage but with higher LCOE
- Environmental performance does not always align with economic performance: ESS 1 is best environmentally (CPBP = 1 year) AND economically, but only achieves 52.56% ECR
- Hydrogen storage offers the unique advantage of co-generation (heat + electricity from fuel cell), but this benefit does not offset the poor round-trip efficiency

### 5.3 Critical Evaluation

**Reasonableness of assumptions:**
- The assumption that electricity can be sold to the grid at 80% of purchase price is realistic for net metering or feed-in tariff schemes in Morocco
- Component costs are sourced from local market consultations and recent literature, enhancing realism
- The discount rate of 3% is conservative and appropriate for Morocco
- The carbon emission factor of 0.547 kgCO2e/kWh is specific to the Moroccan grid

**Limitations acknowledged by the authors:**
1. Simulation-based study — real-world uncertainties (actual weather, maintenance, embodied carbon) not fully captured
2. Economic analysis does not account for future energy price changes or policy incentives
3. Only three ESSs were compared; other configurations may perform differently
4. The study focused on Morocco; generalizability to other climates/contexts requires similar assessment

**Additional limitations not explicitly stated:**
- No degradation model for PV panels, batteries, or fuel cells over project lifetime
- Battery lifetime of 10 years means replacement is needed within a 25-year project; this is captured in the economic model but the exact replacement schedule is not detailed
- The hydrogen storage capacity (2.7 kg) is relatively small — equivalent to about 90 kWh of hydrogen energy (at LHV), but only ~36 kWh of electricity after fuel cell conversion. This provides roughly 2-3 hours of average building load coverage
- No sensitivity analysis on component sizing, discount rate, or electricity prices
- The building model is a "typical" residential building, not a specific real building with measured data

**Generalizability:**
The findings are most applicable to Mediterranean climates with similar solar/wind resources, grid electricity prices, and building types. The relative ranking of scenarios (ESS 1 > ESS 2 > ESS 3 economically) is likely robust for current technology costs, but could change with: (a) significant reductions in electrolyzer/fuel cell costs, (b) carbon pricing policies, (c) higher grid electricity prices, or (d) incentives for energy independence.

### 5.4 Derived/Inferred Values

**Total annual building energy demand:**
From ECR1 = (E_PV + E_WT) / E_req = 52.56%:
E_req = (26,238.44 + 8,432.49) / 0.5256 = 34,670.93 / 0.5256 = **65,964 kWh/year**

**Average daily load:** 65,964 / 365 = **180.7 kWh/day**

**Average load:** 65,964 / 8760 = **7.53 kW**

**Capacity factor of PV system:**
Annual generation / (rated power x hours) = 26,238.44 / (13.2 x 8760) = 26,238.44 / 115,632 = **22.69%**

**Capacity factor of WT system:**
8,432.49 / (7.5 x 8760) = 8,432.49 / 65,700 = **12.83%**

**Battery autonomy (approximate):**
45 kWh / 7.53 kW average load = **5.97 hours** (at average load, without considering SoC limits)

**Hydrogen storage energy equivalence:**
2.7 kg x 33.33 kWh/kg = 90 kWh (LHV energy content)
After fuel cell conversion: 90 x 0.40 = **36 kWh of electricity**
At average load: 36 / 7.53 = **4.78 hours of coverage**

**Round-trip efficiency of hydrogen storage:**
Electrolyzer (70%) x Fuel cell (40%) = **28%** (vs. 81% for battery: 90% x 90%)

**Cost breakdown (approximate CAPEX):**
- PV: 13.2 kW x $800/kW = $10,560
- WT: 7.5 kW x $1325/kW = $9,937.50
- Battery: 45 kWh x $150/kWh = $6,750
- Electrolyzer: 14 kW x $1200/kW = $16,800
- H2 tank: 2.7 kg x $378/kg = $1,020.60
- Fuel cell: 14 kW x $1000/kW = $14,000
- Heat exchanger: $500

**Approximate total CAPEX by scenario:**
- ESS 1: $10,560 + $9,937.50 = **$20,497.50**
- ESS 2: $20,497.50 + $6,750 = **$27,247.50**
- ESS 3: $20,497.50 + $16,800 + $1,020.60 + $14,000 + $500 = **$52,818.10**

**Annual unmet load (ESS 1):**
E_req - (E_PV + E_WT) = 65,964 - 34,670.93 = **31,293 kWh/year** (47.44% of demand)

**Annual energy shortage (ESS 1, from Fig. 6):** 12,399.86 kWh/year
Note: This differs from the above calculation because the 12,399.86 kWh represents the instantaneous deficit hours (when generation < load at a given hour), while the 31,293 kWh represents the annual net deficit. The difference is because during many hours, generation exceeds load even though annual generation is less than annual demand.

### 5.5 Key Takeaways

1. **Grid-connected direct supply is the most economically and environmentally efficient approach** under current conditions: ESS 1 achieves the lowest LCOE ($0.05/kWh), shortest payback (5.80 years), and best environmental performance (CPBP = 1 year, CER = 18.21 tCO2e/year). However, it only covers 52.56% of the building's energy demand from renewables.

2. **Battery storage enables 100% renewable coverage at moderate additional cost**: ESS 2 doubles the LCOE to $0.09/kWh but achieves full energy independence. The 45 kWh Li-ion battery with 90% efficiency provides an effective bridge between daytime solar surplus and nighttime/evening demand.

3. **Hydrogen storage is not yet economically viable for building-scale applications**: With an LCOE of $0.21/kWh and payback of 16.30 years, the hydrogen scenario is approximately 2.4x more expensive than batteries and 4.2x more expensive than direct supply. The fundamental issue is the poor round-trip efficiency (28% vs. 81% for batteries).

4. **Embodied carbon of storage systems matters environmentally**: Batteries have high embodied carbon (200 kgCO2e/kWh), giving ESS 2 a longer carbon payback period (1.66 years) than ESS 3 (1.14 years), despite ESS 2 delivering more energy to the building. This counterintuitive result highlights the importance of life cycle assessment.

5. **Morocco's Mediterranean climate is well-suited for PV-Wind hybrid systems**: The combination of 13.2 kWp PV and 7.5 WT generates 34,671 kWh/year, with PV contributing 75.7% and wind 24.3% of renewable generation. The complementary nature of solar and wind resources helps achieve higher combined capacity factors than either technology alone.

---

*Note: All numerical values in Sections 1-4 are directly extracted from the paper. Values in Section 5 labeled as "derived" or "approximate" are calculated from the paper's stated values using the formulas provided or simple arithmetic. Discrepancies between derived and stated values are noted where they occur.*
