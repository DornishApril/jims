# Paper Summary: Techno-economic feasibility and performance analysis of an islanded hybrid renewable energy system with hydrogen storage in Morocco

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Techno-economic feasibility and performance analysis of an islanded hybrid renewable energy system with hydrogen storage in Morocco
- **Authors:** Sara El Hassani, Fakher Oueslati, Othmane Horma, Domingo Santana, Mohammed Amine Moussaoui, Ahmed Mezrhab
- **Journal/Conference name:** Journal of Energy Storage
- **Year of publication:** 2023
- **DOI:** https://doi.org/10.1016/j.est.2023.107853
- **Study location:** Dakhla city, Morocco (23.6848°N, 15.9579°W)
- **System type:** Islanded (off-grid) hybrid renewable energy system — Wind/Fuel Cell/Diesel with hydrogen storage (electrolyzer + H2 tank + alkaline fuel cell)
- **Study type:** Simulation-based (TRNSYS software, Version 18)
- **Software/tools used:** TRNSYS (Version 18), Meteonorm/Energy Weather files (EPW format), NASA Surface and Solar Energy database, Excel calculation tool for economic analysis
- **Optimization method used:** Power Dispatch Management Strategy (PDMS) combining Load Following Mode (LFM) and Cycle Charging Mode (CCM)

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Model/Type | Rated Capacity | Number of Units | Key Specifications |
|-----------|-----------|---------------|-----------------|-------------------|
| Wind Turbine | Enercon E40 600/46 | 600 kW (rated power 605 kW) | 1 | Rotor height: 46 m; Rotor diameter: 43.7 m; Cut-in/cut-out: site shear exponent 0.14; Power curve: 13.5 m/s rated speed |
| Diesel Engine Generator Set (DEGS) | Generic (Type 120) | 300 kW per unit | 5 units (max 5 simultaneously) | Total DEGS capacity: 1500 kW; Operating range: 0–360 kW per unit; Lifetime: 15,000 hours |
| Fuel Cell | Alkaline Fuel Cell (AFC) | 300 kW | 1 | Idling power: 60 kW; Operating range: 60–300 kW; Efficiency: 56.6%; Lifetime: 10 years |
| Electrolyzer | Alkaline Water Electrolysis (AWE) | 500 kW | 1 | Idling power: 120 kW; Power range: 115–430 kW; H2 production: 30–100 m³/h; O2 production: 15–50 m³/h; Auxiliary cooling: 65 kW; Lifetime: 20 years |
| Hydrogen Storage Tank | Compressed gas (Type 167) | 750.5 kg capacity | 1 | Outlet pressure: 200 bar; Max pressure: 400 bar; Tank volume: 50 m³; Temperature: 20°C; Lifetime: 20 years |
| AC/DC Converter | For electrolyzer | 472.579 kW (peak) | 1 | Efficiency: 95.91%; Lifetime: 15 years |
| DC/AC Converter | For fuel cell | 295.793 kW (peak) | 1 | Efficiency: 96.53%; Lifetime: 15 years |

### 2.2 Total System Capacity

- **Total generation capacity:** 600 kW (wind) + 1500 kW (diesel, 5×300 kW) + 300 kW (fuel cell) = **2,400 kW**
- **Total storage capacity:** 750.5 kg hydrogen (compressed at 200 bar, 50 m³ tank)
- **Total conversion capacity:** 500 kW (electrolyzer) + 472.579 kW (AC/DC) + 295.793 kW (DC/AC) = **1,268.372 kW**

### 2.3 Component Costs (Capital, Replacement, O&M)

| Component | Capital Cost | Replacement Cost | O&M Cost | Fuel Cost | Lifespan |
|-----------|-------------|-----------------|----------|-----------|----------|
| Wind turbine | $1,300/kW | $1,300/kW | $26.7/kW/year | – | 20 years |
| Fuel cell | $600/kW | $600/kW | $0.01/h/kW = $3.65/kW/year | – | 10 years |
| Hydrogen storage | $100/m³ | $100/m³ | $0.5/m³/year | – | 20 years |
| Electrolyzer | $151/kW | $151/kW | $8/year/kW | – | 20 years |
| Diesel generator (5 units) | $230/kW | $210/kW | $0.007/kWh | $0.1/m³ | 15,000 hours |
| AC/DC Converter | $550/kW | $450/kW | $5/kW/year | – | 15 years |
| DC/AC Converter | $550/kW | $450/kW | $5/kW/year | – | 15 years |

### 2.4 Economic Parameters

| Parameter | Value |
|-----------|-------|
| Project lifetime | 20 years |
| Discount rate (r) | 9.3% |
| O&M growth rate | 2% per year |
| Fuel cost (diesel/natural gas) | $0.1/m³ |
| Currency and cost year | USD (year not explicitly stated, assumed 2023) |
| Salvage value (payback) | $356,772.85 |

### 2.5 Resource Data

| Parameter | Value |
|-----------|-------|
| Location | Dakhla, Morocco (23.6848°N, 15.9579°W) |
| Wind data source | NASA Surface and Solar Energy webpage + Meteonorm/Energy Weather files (EPW format) |
| Wind data period | 10 years (2010–2020) |
| Average wind speed at 10 m | Varies monthly: 3.85–7.81 m/s (highest in July: 7.8 m/s) |
| Average wind speed at 50 m hub height | 4.5–9.75 m/s |
| Site shear exponent | 0.14 |
| Solar irradiance | Not a primary resource (no PV in this system); meteorological temperature and pressure data from Meteonorm |
| CO2 emission factor (Morocco) | 0.748 tCO2/MWh |

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

| Metric | Value |
|--------|-------|
| NPV Cost (NPVCost) | **$2,650,843** |
| NPV Production (NPVProduction) | **37,819,172 kWh** |
| Levelized Cost of Energy (LCOE) | **$0.0701/kWh** |
| Total initial capital cost | $1,674,563.70 |
| Total replacement cost | $446,050.40 |
| Total O&M cost (annual) | $57,484 |
| Total fuel cost | $195 |
| Salvage value (payback) | $356,772.85 |
| Payback period | Not explicitly stated (positive salvage value indicates ROI) |
| IRR/ROI | Not explicitly reported |

### 3.2 Reliability Metrics

| Metric | Value |
|--------|-------|
| Renewable Fraction (RF) | **44.57%** |
| LPSP (Loss of Power Supply Probability) | Not explicitly reported |
| Unmet load | Not explicitly reported as a separate value |
| System availability | Not explicitly reported (system designed to meet all load) |

### 3.3 Generation Metrics

| Metric | Value |
|--------|-------|
| Total annual electricity generation | **4,714,559 kWh/year** |
| Wind generation | **2,313,504 kWh/year (49.07%)** |
| Fuel cell generation | **812,399 kWh/year (16.75%)** — paper also states 789.568 MWh/year |
| Diesel generation | **1,611,488 kWh/year (34.18%)** |
| Renewable fraction | **44.57%** |
| Excess electricity | Not explicitly reported |
| Electrolyzer consumption | **1,763,059 kWh/year (37.40% of total production)** |
| Converter losses | **92,243 kWh/year (1.95% of total output)** |
| Hydrogen production | Not explicitly stated in kg/year (electrolyzer consumes 1,763,059 kWh/year) |
| Diesel fuel consumption | 639.83 m³ natural gas per year |

### 3.4 Load Metrics

| Metric | Value |
|--------|-------|
| Total annual load demand | Not explicitly stated (derived: ~4,714,559 kWh/year minus losses/unmet) |
| Average daily load | **7,680 kWh/day** |
| Peak load | **639 kW** |
| Average load | **320 kW** |
| Load profile type | Residential community (250 houses, 5 small supermarkets, 200 LED streetlights) |
| Day-to-day random variability | 5% |

**Load breakdown:**
- 250 houses: 312,500 W total (1,250 W per house = 30 kWh/day per house)
- 5 small supermarkets: 7,000 W total (1,400 W per supermarket)
- 200 LED streetlights: 500 W total (2.5 W per light)

### 3.5 Optimal Configuration

| Parameter | Value |
|-----------|-------|
| Winning configuration | 600 kW wind turbine (1× Enercon E40) + 5×300 kW diesel generators + 300 kW AFC + 500 kW electrolyzer + 50 m³ H2 tank (200 bar) + AC/DC and DC/AC converters |
| Objective function | Minimize LCOE via PDMS dispatch strategy |
| Constraints | Max 5 DEGS units; H2 SOC limits (10%–90%); fuel cell idle at 60 kW; electrolyzer idle at 120 kW |
| Sensitivity analysis | Not formally conducted; validation against reference [30] with <1% relative error |
| Capacity factor (wind turbine) | **44.02%** |
| Capacity factor (fuel cell) | Not explicitly stated (average output 92.729 kW vs 300 kW rated = ~30.9%) |
| Capacity factor (diesel) | Not explicitly stated (average ~107.4 kW per unit vs 300 kW rated = ~35.8%) |

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

- **Type of dispatch:** Power Dispatch Management Strategy (PDMS) combining Load Following Mode (LFM) and Cycle Charging Mode (CCM)
- **Priority order of generation sources:**
  1. Wind turbine (primary — runs whenever wind available)
  2. Fuel cell (secondary — activates when wind insufficient)
  3. Diesel generators (tertiary — backup when wind + H2 insufficient)
- **Decision logic:**
  - If wind energy > load demand → excess goes to electrolyzer for H2 production
  - If wind energy < load demand → fuel cell activates using stored H2
  - If wind insufficient AND H2 tank SOC low → diesel generators start
- **Constraints on component operation:**
  - Max 5 DEGS units simultaneously
  - DEGS operating range: 0–360 kW per unit
  - Fuel cell operating range: 60–300 kW
  - Electrolyzer operating range: 115–430 kW (rated 500 kW)

### 4.2 Power Flow Logic

- **Excess renewable energy handling:** Surplus wind power (wind output minus load) is directed to the electrolyzer to produce hydrogen, stored in compressed tank at 200 bar
- **Deficit handling:** When wind is insufficient, fuel cell generates power from stored hydrogen; if H2 SOC drops to 10%, fuel cell shuts off and diesel generators start
- **Battery charging/discharging logic:** No battery in this system (hydrogen is the sole storage medium)
- **Hydrogen production logic:** Electrolyzer activates when wind > load; deactivates when surplus power falls below threshold or H2 tank SOC reaches 90%
- **Hydrogen consumption logic:** Fuel cell consumes H2 when wind < load; shuts off when H2 SOC drops to 10%
- **Diesel generator start/stop conditions:** Start when wind insufficient AND H2 SOC ≤ 10%; stop when wind sufficient OR H2 SOC recovers above 20%
- **Grid interaction:** None — islanded/off-grid system

### 4.3 Control Parameters

| Parameter | Value |
|-----------|-------|
| Upper SOC limit (H2 tank), electrolyzer OFF | 90% |
| Lower SOC limit (H2 tank), electrolyzer ON | 80% |
| Upper SOC limit (H2 tank), fuel cell ON | 20% |
| Lower SOC limit (H2 tank), fuel cell OFF | 10% |
| Fuel cell idling power | 60 kW |
| Electrolyzer idling power | 120 kW |
| Max DEGS units | 5 |
| DEGS rated power per unit | 300 kW |
| AC/DC converter efficiency | 95.91% |
| DC/AC converter efficiency | 96.53% |
| Electrolyzer auxiliary cooling | 65 kW |
| H2 storage pressure setpoint | 200 bar |
| H2 storage max pressure | 400 bar |
| H2 storage temperature | 20°C |

### 4.4 Algorithm Flow

The PDMS operates as follows:

1. **At each time step (hourly):** Measure wind power output and load demand
2. **Calculate net load:** Net Load = Load Demand − Wind Power Output
3. **If Net Load ≤ 0 (excess wind):**
   - Route surplus to electrolyzer
   - Electrolyzer produces H2 at rate proportional to surplus power
   - H2 compressed to 200 bar and stored
   - If H2 SOC reaches 90%, electrolyzer goes idle
4. **If Net Load > 0 (deficit):**
   - Activate fuel cell to cover deficit (up to 300 kW rated)
   - Fuel cell consumes H2 from tank
   - If H2 SOC drops to 10%, fuel cell shuts off
   - Activate diesel generators (1–5 units) to cover remaining deficit
5. **LFM vs CCM:**
   - **LFM:** DEGS operates only when needed at variable output to match net load
   - **CCM:** When DEGS is on, it runs at full rated power; excess used for electrolysis
6. **Seasonal behavior:** Summer = high wind, minimal diesel; Winter = low wind, frequent diesel + fuel cell operation

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

This system serves a small settlement of 250 houses, 5 supermarkets, and 200 LED streetlights in Dakhla, Morocco — one of the windiest locations in the country. The average daily load is 7,680 kWh/day with a peak of 639 kW.

**Morning (6:00–9:00):** Wind speeds in Dakhla tend to be moderate in early morning. The wind turbine (Enercon E40, 600 kW rated) may produce anywhere from 100–400 kW depending on the season. As residential load ramps up (refrigerators, water heaters, air conditioners), the system may need fuel cell supplementation. If the hydrogen tank SOC is above 20%, the fuel cell kicks in to cover the gap. If SOC is below 10%, one or more diesel generators start.

**Midday (10:00–15:00):** Solar heating increases wind convection, and Dakhla's wind pattern typically strengthens. The wind turbine may approach its rated output of 572–600 kW, exceeding the average load of 320 kW. The surplus of ~200–280 kW is routed to the 500 kW electrolyzer, which splits water into hydrogen (at up to 100 m³/h) and oxygen. The hydrogen is compressed to 200 bar into the 500 m³ storage tank. During summer months, this midday surplus is substantial, and the electrolyzer may operate near full capacity.

**Evening (16:00–20:00):** Load peaks as residents return home (air conditioners, lighting, appliances). Wind may still be strong in Dakhla during summer evenings. If wind drops, the fuel cell (rated 300 kW) activates, consuming stored hydrogen. The fuel cell output ranges from 60 kW (idle) to 300 kW (rated), with hydrogen consumption up to 181.82 Nm³/h.

**Night (21:00–5:00):** Load decreases but remains significant (refrigerators, streetlights). Wind in Dakhla at the 50 m hub height averages 4.5–9.75 m/s depending on season. The turbine continues generating. If wind is insufficient, the fuel cell covers the deficit. Diesel generators serve as last resort when hydrogen is depleted.

**Seasonal variations:** Summer (June–August) brings the strongest winds (monthly average up to 9.75 m/s at 50 m hub height), resulting in minimal diesel usage and maximum hydrogen production. Winter (November–March) sees lower wind speeds (4.5–6 m/s), requiring more diesel generator engagement (1–3 units running) and drawing down hydrogen reserves. The hydrogen tank SOC fluctuates from ~0.52 in summer to ~0.18 in winter, reflecting this seasonal cycle.

### 5.2 System Behavior Analysis

**Why this configuration is optimal:** The 600 kW wind turbine was selected because Dakhla has exceptional wind resources (44% capacity factor). The 500 kW electrolyzer is sized to absorb the typical surplus when wind exceeds the 320 kW average load. The 300 kW fuel cell covers the average deficit when wind is low. The 5×300 kW diesel generators provide 1,500 kW of backup capacity — more than twice the peak load — ensuring reliability even during extended low-wind periods.

**Relationship between renewable penetration and storage sizing:** At 44.57% renewable fraction, the system relies on hydrogen storage to time-shift wind energy. The 750.5 kg H2 tank (50 m³ at 200 bar) provides approximately 2.5 days of average load coverage if fully charged (750.5 kg × 33.3 kWh/kg HHV ≈ 25,000 kWh theoretical; at 56.6% FC efficiency ≈ 14,150 kWh usable ≈ 1.8 days of 7,680 kWh/day load). This is a critical design tradeoff — larger tanks would increase renewable fraction but at higher capital cost.

**Dispatch strategy impact on component lifetimes:** The fuel cell (10-year lifespan) is the most vulnerable component. By using it only when necessary (wind deficit + adequate H2 SOC), the system minimizes operating hours. The diesel generators (15,000-hour lifespan) are preserved as backup only. The wind turbine and electrolyzer (20-year lifespans) run continuously.

**Trade-offs identified by authors:**
- Higher renewable fraction requires larger electrolyzer + H2 tank → higher capital cost
- Lower diesel usage → lower CO2 emissions but requires more hydrogen storage
- The LCOE of $0.0701/kWh is competitive with Moroccan grid electricity, especially as renewable technology costs continue declining

**Edge cases:** During extended low-wind periods (winter), the system relies heavily on diesel (up to 3–5 generators running). The hydrogen tank SOC can drop to 10%, at which point the fuel cell shuts off entirely and diesel covers 100% of the deficit. The system is designed to handle this — the 1,500 kW diesel capacity far exceeds the 639 kW peak load.

### 5.3 Critical Evaluation

**Reasonableness of assumptions:**
- The 9.3% discount rate is appropriate for Morocco's economic context
- The 20-year project lifetime matches the wind turbine and electrolyzer lifespan
- The 44% wind capacity factor is realistic for Dakhla (one of the windiest sites globally)
- The assumption of $0.1/m³ natural gas fuel cost is reasonable for Morocco
- The CO2 emission factor of 0.748 tCO2/MWh is based on IEA/IRENA data for Morocco

**Limitations:**
- No battery storage — hydrogen is the only storage medium, which has lower round-trip efficiency (~40% for electrolysis + fuel cell vs ~85% for batteries)
- The system has no PV component despite Dakhla having good solar resources
- Load profile is estimated from appliance counts, not measured data
- The study does not perform formal sensitivity analysis on key parameters
- The economic analysis assumes constant fuel prices over 20 years
- The TRNSYS model validation is against one reference study only

**Generalizability:** The PDMS approach is adaptable to other locations, but the specific component sizing is tailored to Dakhla's wind profile and the settlement's load. The framework (wind + electrolyzer + H2 + FC + diesel backup) is generalizable to any off-grid community with good wind resources.

**What would change with different parameters:**
- Higher wind speeds → higher renewable fraction, lower LCOE
- Lower discount rate → lower LCOE, more attractive economics
- Higher fuel costs → hydrogen storage becomes more economically advantageous
- Adding PV → could increase renewable fraction but at additional capital cost

**Comparison to similar systems:** The LCOE of $0.0701/kWh is competitive with other hybrid systems in the literature. Ghenai et al. achieved $0.145/kWh for a PV/FC system in Sharjah. Oueslati reported $0.0492/kWh for a wind/PV/FC system in Tunisia. The present system's higher LCOE reflects its wind-only renewable source (no PV contribution) and the relatively small scale (600 kW wind for a 320 kW average load).

### 5.4 Derived/Inferred Values

| Derived Value | Calculation | Result |
|---------------|-------------|--------|
| Average daily generation per source (wind) | 2,313,504 kWh / 365 | **6,338 kWh/day** |
| Average daily generation per source (fuel cell) | 812,399 kWh / 365 | **2,225 kWh/day** |
| Average daily generation per source (diesel) | 1,611,488 kWh / 365 | **4,415 kWh/day** |
| Wind capacity factor | 2,313,504 / (600 × 8,760) | **44.02%** (matches paper) |
| Fuel cell capacity factor | 812,399 / (300 × 8,760) | **30.91%** |
| Diesel capacity factor (per unit) | (1,611,488/5) / (300 × 8,760) | **12.30%** |
| Storage autonomy (H2 tank) | 750.5 kg × 33.3 kWh/kg × 0.566 / 7,680 kWh/day | **1.84 days** |
| Round-trip H2 storage efficiency | η_electrolyzer × η_fuel_cell | ~40% (estimated: 70% × 56.6%) |
| Cost breakdown by component (% of NPV cost) | Wind: $743,938/$2,650,843 | **28.1%** |
| Cost breakdown — Diesel | ($345,000 + $34,128 + replacement) / $2,650,843 | **~14.3%** |
| Cost breakdown — Fuel cell | ($179,837 + $1,094 + $179,837) / $2,650,843 | **~13.6%** |
| Cost breakdown — Electrolyzer | ($75,500 + $4,000) / $2,650,843 | **~3.0%** |
| Cost breakdown — Converters | ($325,372 + $3,842 + $266,214) / $2,650,843 | **~22.4%** |
| Annual CO2 reduction per year | 70,529.80 t / 20 years | **3,526 tCO2/year** |
| Implied total load served annually | 2,313,504 + 812,399 + 1,611,488 − 92,243 | **4,645,148 kWh/year** |
| Implied annual load (from daily) | 7,680 × 365 | **2,803,200 kWh/year** |

**Note on discrepancy:** The paper states total generation is 4,714,559 kWh/year but the implied load from daily consumption (7,680 kWh/day × 365) is only 2,803,200 kWh/year. The difference is explained by: (1) electrolyzer consumption of 1,763,059 kWh/year (energy used to produce H2, not delivered to load), and (2) converter losses of 92,243 kWh/year. The actual load served is approximately 4,714,559 − 1,763,059 − 92,243 = 2,859,257 kWh/year, which is close to the stated daily load.

### 5.5 Key Takeaways

1. **Wind-hydrogen-diesel hybrid systems are economically viable for remote Moroccan communities.** At $0.0701/kWh LCOE, the system approaches grid parity and offers energy independence for off-grid settlements.

2. **Hydrogen storage enables high renewable penetration (44.57%) without batteries.** The electrolyzer-fuel cell combination provides long-duration seasonal storage that batteries cannot economically achieve at this scale.

3. **Diesel backup remains essential for reliability.** Despite the hydrogen storage, diesel generators provide 34% of annual energy, particularly during winter low-wind periods. Eliminating diesel entirely would require significantly oversizing the wind turbine and hydrogen system.

4. **The PDMS dispatch strategy is the key innovation.** By combining Load Following and Cycle Charging modes with hydrogen SOC-based switching, the system optimizes the tradeoff between renewable utilization and diesel consumption.

5. **Morocco's Dakhla region is exceptional for wind-hydrogen systems.** The 44% wind capacity factor and consistent wind patterns make it one of the most attractive locations globally for wind-powered green hydrogen production, with potential to meet 4% of global green hydrogen demand by 2030.
