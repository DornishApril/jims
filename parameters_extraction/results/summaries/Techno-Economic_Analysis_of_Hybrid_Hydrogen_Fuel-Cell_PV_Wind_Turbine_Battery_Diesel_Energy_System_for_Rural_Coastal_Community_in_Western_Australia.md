# Paper Summary: Techno-Economic Analysis of Hybrid Hydrogen Fuel-Cell/PV/Wind Turbine/Battery/Diesel Energy System for Rural Coastal Community in Western Australia

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Techno-Economic Analysis of Hybrid Hydrogen Fuel-Cell/PV/Wind Turbine/Battery/Diesel Energy System for Rural Coastal Community in Western Australia
- **Authors:** Bassam Al-Hanahi, Jianan Wen, Daryoush Habibi, Asma Aziz
- **Affiliation:** School of Engineering, Edith Cowan University, Perth, Australia
- **Journal/Conference:** 2023 International Conference on Sustainable Technology and Engineering (i-COSTE)
- **Year of publication:** 2023
- **DOI:** 10.1109/I-COSTE60462.2023.10500789
- **Publisher:** IEEE
- **Study location:** Rural coastal community in Western Australia (coordinates: 25.9299° S latitude, 113.5381° E longitude)
- **System type:** Off-grid Fuel Cell/PV/Wind Turbine/Battery/Diesel HRES (Hybrid Renewable Energy System)
- **Study type:** Simulation-based (computational modeling and optimization)
- **Software/tools used:** HOMER Pro (version 3.14)
- **Optimization method:** HOMER Pro built-in optimization algorithm (searches for minimum NPC configuration); cycle charging dispatch strategy for system control

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Rated Capacity | Number of Units | Key Specifications |
|-----------|---------------|-----------------|-------------------|
| Solar PV Array | 700 kW | 1 | Derating factor: 80%; Lifetime: 20 years (table) / 25 years (text — discrepancy noted); Overall PV efficiency per Eq. (5) |
| Wind Turbine | 230 kW | 1 | Hub height wind speed conversion per Eq. (6); surface roughness length Z0 used for height adjustment |
| Fuel Cell | 100 kW | 1 | Part of hydrogen energy storage subsystem |
| Electrolyzer | 348 kW | 1 | Converts excess electricity to hydrogen |
| Hydrogen Tank | 312 kg | 1 | Stores hydrogen for fuel cell consumption |
| Diesel Generator | 365 kW | 1 | Backup/conventional generation |
| Battery | 224 strings | 224 | Throughput: 800 kWh per string; roundtrip efficiency ηb per Eq. (7) |
| Converter | 98.4 kW | 1 | DC/AC conversion for interconnecting components |

**Dispatch strategy:** Cycle charging (stated in PV system description)

### 2.2 Total System Capacity

- **Total generation capacity:** 700 kW (PV) + 230 kW (Wind) + 100 kW (FC) + 365 kW (DG) = **1,395 kW**
- **Total storage capacity:** 224 battery strings (800 kWh throughput each) + 312 kg hydrogen tank
- **Total conversion capacity:** 348 kW (electrolyzer) + 98.4 kW (converter) = **446.4 kW**

### 2.3 Component Costs (Capital, Replacement, O&M)

**Solar PV System:**
| Parameter | Value |
|-----------|-------|
| Capital | $1,575,000 |
| Replacement | $1,575,000 |
| O&M | $625/year |
| Derating factor | 80% |
| Lifetime | 20 years (table) / 25 years (text) |

**Wind Turbine System:**
| Parameter | Value |
|-----------|-------|
| Capital | $95,000 |
| Replacement | $81,000 |
| O&M | $202,500 |

**Hydrogen Energy Storage System:**

*Fuel Cell:*
| Parameter | Value |
|-----------|-------|
| Capacity | 100 kW |
| Capital | $3,000,000 |
| Replacement | $3,000,000 |
| O&M | $17,520/year |

*Electrolyzer:*
| Parameter | Value |
|-----------|-------|
| Capacity | 348 kW |
| Capital | $696,000 |
| Replacement | $696,000 |
| O&M | $450/year |

*Hydrogen Tank:*
| Parameter | Value |
|-----------|-------|
| Capacity | 312 kg |
| Capital | $1,000 |
| Replacement | $800 |
| O&M | $250/year |

**Diesel Generator:**
| Parameter | Value |
|-----------|-------|
| Capacity | 365 kW |
| Capital | $56,000 |
| Replacement | $40,000 |
| O&M | $61,320/year |

**Converter:**
| Parameter | Value |
|-----------|-------|
| Capacity | 98.4 kW |
| Capital | $29,520 |
| Replacement | $29,520 |

**Battery:**
| Parameter | Value |
|-----------|-------|
| Capacity (strings) | 224 |
| Capital | $71,680 |
| Replacement | $71,680 |
| O&M | $200/year |
| Throughput | 800 kWh per string |

**Currency:** US dollars ($). Cost year not explicitly stated but consistent with 2023 publication.

### 2.4 Economic Parameters

| Parameter | Value |
|-----------|-------|
| Project lifetime | Not explicitly stated (HOMER default typically 25 years) |
| Discount/interest rate | Not explicitly stated in the paper |
| Inflation rate | Not mentioned |
| Fuel price (diesel) | Not explicitly stated |
| Grid electricity price | N/A (off-grid system) |
| Currency | US dollars ($) |
| Salvage cost | Included in NPC calculation (Eq. 1) |

### 2.5 Resource Data

| Resource | Value |
|----------|-------|
| Solar irradiance (scaled annual average) | **6.19 kWh/m²/day** |
| Solar data source | NASA Atmospheric Science Data Center (via HOMER database) |
| Highest solar radiation month | June (winter) |
| Lowest solar radiation month | December (summer) |
| Wind speed (scaled annual average) | **8.12 m/s** |
| Wind data source | NASA (via HOMER database) |
| Highest average wind speed month | January (summer) |
| Lowest average wind speed month | May (winter) |
| Temperature data | Not explicitly reported |
| Data source | NASA POWER (Prediction of Worldwide Energy Resources) |

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACTION (STRICT EXTRACTION)

### 3.1 Cost Metrics

**Optimal Fuel Cell HRES (the study's recommended configuration):**
| Metric | Value |
|--------|-------|
| NPC | **$4.580 million** |
| LCOE | **$0.5238/kWh** |
| Operating cost | $0.090 million/year |

**High Penetration Fuel Cell HRES:**
| Metric | Value |
|--------|-------|
| NPC | $6.462 million |
| LCOE | $0.7396/kWh |
| Operating cost | $0.207 million/year |

**PV/Wind/Diesel/Battery HRES (no hydrogen):**
| Metric | Value |
|--------|-------|
| NPC | $3.407 million |
| LCOE | $0.3935/kWh |
| Operating cost | $0.086 million/year |

- **Payback period:** Not mentioned
- **IRR/ROI:** Not mentioned
- **Initial capital cost:** Not explicitly broken out separately from NPC

### 3.2 Reliability Metrics

- **LPSP:** Not explicitly reported for any configuration
- **LOLP:** Not mentioned
- **Unmet load:** Not explicitly reported
- **System availability:** Not explicitly reported
- **Renewable fraction (RF):**
  - Optimal Fuel Cell HRES: **98.7%**
  - High Penetration Fuel Cell HRES: **99.8%**
  - PV/Wind/Diesel/Battery HRES: **97.0%**

### 3.3 Generation Metrics

**Optimal Fuel Cell HRES:**
| Metric | Value |
|--------|-------|
| Total annual generation | **1,828,194 kWh/year** |
| Primary generation source | Solar PV (700 kW, primary role) |
| Secondary generation source | Wind turbine (second-highest) |
| Renewable fraction | 98.7% |

**High Penetration Fuel Cell HRES:**
| Metric | Value |
|--------|-------|
| Total annual generation | **2,112,459 kWh/year** |
| Fuel cell generation | **384,493 kWh/year (18.2%)** |
| Renewable fraction | 99.8% |

**PV/Wind/Diesel/Battery HRES:**
| Metric | Value |
|--------|-------|
| Total annual generation | **1,742,674 kWh/year** |
| Renewable fraction | 97.0% |

- **Excess electricity:** Not explicitly reported
- **Battery throughput:** Not explicitly reported (only per-string throughput of 800 kWh given as parameter)
- **Hydrogen production/consumption:** Not explicitly reported in kg/year
- **Diesel consumption:** Not explicitly reported in L/year
- **Grid import/export:** N/A (off-grid)

### 3.4 Load Metrics

| Metric | Value |
|--------|-------|
| Total daily load demand | **1,441 kWh/day** |
| Total annual load demand | **525,965 kWh/year** (1,441 × 365 — derived) |
| Peak load period | 18:00–21:00 (evening, commercial/tourism) |
| Low demand period | 00:00–05:00 |
| Load profile type | Commercial + community (tourism-influenced) |
| Peak load (kW) | Not explicitly stated |
| Average load (kW) | Not explicitly stated (derived: ~60 kW from 1,441 kWh/day ÷ 24h) |

### 3.5 Optimal Configuration

- **Winning configuration:** Optimal Fuel Cell/PV/Wind Turbine/Diesel/Battery HRES
- **Component sizes:** PV = 700 kW, Wind = 230 kW, Fuel Cell = 100 kW, Electrolyzer = 348 kW, H2 Tank = 312 kg, DG = 365 kW, Battery = 224 strings, Converter = 98.4 kW
- **Objective function:** Minimum NPC (Net Present Cost) via HOMER optimization
- **Selection rationale:** Balance between cost and decarbonization — not the absolute lowest LCOE but the best compromise including hydrogen technology
- **Constraints:** High penetration FC scenario constrained to operate 8,760 hours/year (continuous)
- **Sensitivity analysis:** Not explicitly reported (mentioned as future work direction)

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

- **Type:** Cycle charging dispatch strategy (explicitly stated for PV system)
- **Priority order:** Not explicitly described in detail; HOMER's cycle charging algorithm generally prioritizes renewable sources (PV, wind) first, then dispatches controllable sources (diesel, fuel cell) to meet remaining demand
- **Decision logic:** HOMER Pro internal optimization determines dispatch based on minimizing total NPC while meeting load and constraints
- **Constraints on component operation:** High penetration fuel cell case forced to run 8,760 hours/year (continuous operation)

### 4.2 Power Flow Logic

- **Excess renewable energy handling:** Directed to electrolyzer (348 kW) for hydrogen production, stored in 312 kg tank; battery charging (224 strings)
- **Deficit handling:** Battery discharge, fuel cell operation (from stored hydrogen), diesel generator backup
- **Battery charging/discharging logic:** SOC calculated per Eq. (7) using roundtrip efficiency ηb, nominal capacity Cb, available power Ps, demand power Pd, time interval Δt
- **Hydrogen production:** Electrolyzer converts excess electricity to hydrogen when surplus exists
- **Hydrogen consumption:** Fuel cell converts stored hydrogen to electricity during deficits
- **Diesel generator start/stop:** Not explicitly described; dispatched by HOMER when renewable + storage insufficient
- **Grid interaction:** N/A (off-grid system)

### 4.3 Control Parameters

| Parameter | Value |
|-----------|-------|
| Battery roundtrip efficiency (ηb) | Not explicitly stated (used in Eq. 7) |
| Battery nominal capacity (Cb) | Not explicitly stated per string |
| Battery SOC minimum/maximum | Not explicitly stated |
| Diesel generator minimum load ratio | Not explicitly stated |
| Fuel cell operating range | 100 kW rated; high penetration case runs 8,760 h/year |
| Inverter efficiency | Not explicitly stated |
| Converter capacity | 98.4 kW |
| Charge controller | Not explicitly described |
| PV derating factor | 80% |

### 4.4 Algorithm Flow

The paper provides the governing equations but does not present a detailed step-by-step flowchart:

1. **Power balance:** Total available power (Ps) from PV + wind + FC + DG vs. demand (Pd)
2. **PV output:** P_PV = η_PV × R_t × A_PV (Eq. 5)
3. **Wind speed conversion:** V_h(t) = V_ref(t) × ln(H/Z0) / ln(H_ref/Z0) (Eq. 6)
4. **Battery SOC:** SOC(t) = SOC(t-1) + η_b × Δt × (Ps - Pd) / Cb (charging) or SOC(t-1) + η_b × Δt × (Pd - Ps) / Cb (discharging) (Eq. 7)
5. **NPC calculation:** NPC = Σ R_i × (C_salvage + C_capital + C_replacement + C_OM + C_fuel) (Eq. 1)
6. **LCOE calculation:** LCOE = (C_annual - c_boiler × L_thermal) / L_electrical (Eq. 4)
7. **HOMER optimization:** Searches all feasible component combinations, selects minimum NPC configuration satisfying constraints

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

This system serves a small rural coastal community in Western Australia with a daily electricity demand of **1,441 kWh/day** (approximately 526 MWh/year). The community's economy is tourism-driven, which shapes the load profile distinctly: demand peaks in the evening (18:00–21:00) when commercial and tourism activities are most intensive, and bottoms out between midnight and 5:00 AM.

**Morning (6:00–12:00):** Solar radiation begins ramping up in a region that receives an annual average of 6.19 kWh/m²/day — excellent solar resource. The 700 kW PV array, derated to 80% (effective 560 kW peak), begins generating. Morning load is moderate as the community wakes up. Any surplus PV output beyond immediate demand first charges the 224-string battery bank, then powers the 348 kW electrolyzer to produce hydrogen. The diesel generator remains off during this period if PV + battery can cover the load.

**Midday (12:00–15:00):** Peak solar production. With 700 kW of PV capacity and good irradiance, the system likely generates 400–560 kW during peak hours. The daily load average is only ~60 kW (1,441 kWh ÷ 24h), meaning midday solar alone can meet the entire community load with substantial surplus. This excess — potentially 300–500 kW — is directed to: (1) battery charging (topping up after overnight discharge), (2) electrolyzer operation producing hydrogen for the 312 kg storage tank. The electrolyzer at 348 kW can consume significant surplus, converting it to approximately 15–20 kg of hydrogen per day (assuming ~50 kWh/kg electrolyzer energy consumption).

**Evening (15:00–21:00):** Solar output declines as the sun sets, but this is precisely when the load peaks (18:00–21:00) due to commercial/tourism activity. The deficit is covered by: (1) battery discharge from the 224-string bank, (2) fuel cell operation drawing from stored hydrogen. The 100 kW fuel cell provides steady baseload during this critical period. If the combined battery + fuel cell cannot meet the peak, the 365 kW diesel generator kicks in as last resort.

**Night (21:00–06:00):** Load drops to its lowest levels. Wind resource is significant in this coastal location (annual average 8.12 m/s — very strong wind), and interestingly, wind peaks in summer months (January) while solar peaks in winter (June), providing complementary seasonal generation. The 230 kW wind turbine likely produces substantial power at night, especially during summer. Battery discharge continues to cover base load. The fuel cell may continue operating if hydrogen reserves are adequate.

**Seasonal variations:** The paper explicitly notes the complementary nature of solar and wind resources — solar peaks in winter (June), wind peaks in summer (January). This natural complementarity is a key advantage of this location, ensuring relatively stable renewable generation year-round. Winter has less sun hours but more intense radiation per day; summer has more sun but lower daily radiation, compensated by stronger winds.

### 5.2 System Behavior Analysis

**Why this configuration was chosen as optimal:** The authors explicitly state the optimal Fuel Cell HRES was NOT chosen for having the lowest LCOE. The PV/Wind/Diesel/Battery system without hydrogen has a lower LCOE ($0.3935/kWh vs $0.5238/kWh). Instead, the "optimal" label reflects a balance between economic viability and decarbonization goals. The optimal FC HRES achieves CO2 emissions of 5,232 kg/year — less than half the 11,660 kg/year from the non-hydrogen system — while keeping costs moderate compared to the high-penetration FC scenario.

**The hydrogen cost premium:** The fuel cell system adds $3,000,000 in capital cost for the fuel cell alone, plus $696,000 for the electrolyzer. These costs drive the LCOE up by 33% compared to the non-hydrogen system ($0.5238 vs $0.3935/kWh). The fundamental trade-off is clear: every percentage point of CO2 reduction costs significantly more with current hydrogen technology.

**Renewable penetration vs. storage sizing:** The system achieves 98.7% renewable fraction with hydrogen storage, compared to 97.0% without. The marginal 1.7% improvement in renewable fraction comes at a substantial cost premium ($1.173 million additional NPC). The 348 kW electrolyzer and 312 kg hydrogen tank provide long-duration storage complementing the battery's short-duration role.

**Dispatch strategy impact:** Cycle charging means the diesel generator (or fuel cell) runs at full charge to meet deficit while renewables handle base load. This minimizes partial-load operation of the diesel generator, improving efficiency and reducing wear. However, it may result in more diesel starts/stops compared to load-following.

**Edge cases:** The paper does not explicitly analyze extended cloudy/low-wind periods. However, the 365 kW diesel generator (largest single component after PV) provides firm backup capacity. The 312 kg hydrogen tank, if fully charged, could theoretically fuel the 100 kW fuel cell for approximately 375 hours (assuming ~0.83 kg/kWh H2 consumption rate), providing about 15 days of fuel cell-only operation at rated power — substantial resilience.

### 5.3 Critical Evaluation

**Reasonableness of assumptions:**
- Solar resource (6.19 kWh/m²/day) is realistic for Western Australia's coastal region — this is genuinely excellent solar territory.
- Wind resource (8.12 m/s annual average) is exceptionally strong — this is in the top tier of global wind resources. This may be optimistic for the specific location.
- The daily load of 1,441 kWh suggests a community of perhaps 100–200 households equivalent, reasonable for a small rural tourism community.
- Component costs appear high — the fuel cell at $3,000/kW ($3M for 100kW) is consistent with 2023 prices but reflects the immaturity of the technology.
- The electrolyzer capital cost of $2,000/kW ($696k/348kW) is reasonable for 2023 PEM electrolyzer pricing.

**Limitations of this study:**
1. Only three configurations were compared — a more thorough parametric sweep would strengthen conclusions.
2. No sensitivity analysis on key parameters (fuel price, component costs, discount rate) is presented.
3. The load profile is fixed — no load growth scenarios are modeled.
4. Battery lifetime degradation modeling is not discussed in detail.
5. The high-penetration FC scenario (8,760 hours/year continuous operation) is unrealistic for fuel cell durability — most fuel cells cannot run continuously without degradation.
6. No comparison with grid extension as an alternative.
7. Single location only — results may not generalize to less resource-rich sites.

**Generalizability:** The specific cost numbers are location-dependent (excellent solar + wind), but the general finding — that hydrogen storage improves decarbonization at a cost premium — is broadly applicable. The cost gap will narrow as fuel cell and electrolyzer prices continue declining.

**What would change with different parameters:**
- If fuel cell costs drop to $1,000/kW (projected for 2030), the optimal FC HRES LCOE would drop to approximately $0.35–0.40/kWh, potentially beating the non-hydrogen system.
- If carbon pricing were introduced at $50/tonne CO2, the non-hydrogen system would pay ~$580/year in carbon costs, narrowing the economic gap.
- If diesel prices doubled, the economics would shift further toward hydrogen.

### 5.4 Derived/Inferred Values

| Derived Value | Calculation | Result |
|---------------|-------------|--------|
| Annual load demand | 1,441 kWh/day × 365 days | **525,965 kWh/year** |
| Average load | 1,441 kWh ÷ 24 h | **60.0 kW** |
| System capacity factor (PV) | Not calculable without hourly data | ~20–25% estimated |
| System capacity factor (Wind) | Not calculable without hourly data | ~35–45% estimated (strong wind resource) |
| Diesel generation (optimal FC HRES) | Total gen − PV − Wind − FC (approximate) | Small fraction (~1.3% based on RF) |
| Diesel generation (no-H2 HRES) | 1,742,674 × (1 − 0.97) | ~52,280 kWh/year |
| Diesel generation (optimal FC HRES) | 1,828,194 × (1 − 0.987) | ~23,766 kWh/year |
| Diesel generation (high FC HRES) | 2,112,459 × (1 − 0.998) | ~4,225 kWh/year |
| Cost per kg CO2 avoided (optimal vs no-H2) | ($4.580M − $3.407M) / (11,660 − 5,232) kg | **$182.7/kg CO2 avoided** |
| Cost per kg CO2 avoided (high FC vs optimal) | ($6.462M − $4.580M) / (5,232 − 653) kg | **$411.5/kg CO2 avoided** |
| Battery energy capacity (estimated) | 224 strings × 800 kWh throughput | Not directly convertible to kWh capacity without DoD |
| PV capacity factor (rough estimate) | Annual PV gen / (700 kW × 8,760 h) | ~25–29% (estimated from total gen split) |
| Excess electricity (optimal FC HRES) | 1,828,194 − 525,965 | **1,302,229 kWh/year** (71% of generation — very high, suggests significant curting or hydrogen production) |

**Note on excess electricity:** The total generation (1,828,194 kWh) far exceeds the load (525,965 kWh). This 3.5:1 ratio seems very high. This likely reflects: (1) the optimization over-sizes generation to ensure reliability with hydrogen production as a "sink" for excess, (2) significant conversion losses in the electrolyzer-fuel cell cycle (round-trip efficiency ~30–40%), and (3) the system may be producing hydrogen that is not fully consumed, effectively using hydrogen production as an energy dump. This is a significant inefficiency in the system design.

### 5.5 Key Takeaways

1. **Hydrogen storage dramatically reduces CO2 emissions but at a significant cost premium.** The high-penetration fuel cell system achieves 94.4% CO2 reduction (653 vs 11,660 kg/year) but at 90% higher LCOE ($0.7396 vs $0.3935/kWh). The optimal compromise system achieves 55% emission reduction at 33% higher cost.

2. **The Western Australian coastal location has exceptional complementary renewable resources.** Solar (6.19 kWh/m²/day) and wind (8.12 m/s) peak in different seasons, providing natural resource complementarity that makes HRES particularly viable here. This is not replicable everywhere.

3. **Current fuel cell technology is the primary economic barrier.** At $3,000/kW capital cost, the fuel cell dominates system economics. The electrolyzer ($2,000/kW) also contributes significantly. Until these costs drop by 50–70%, hydrogen-integrated HRES will struggle to compete economically with battery-only or diesel-backup systems.

4. **The system generates far more electricity than the load requires.** Total generation is 3.5× the load in the optimal case, suggesting significant over-sizing to ensure reliability and provide hydrogen production headroom. This indicates the optimization may benefit from tighter constraints or multi-objective optimization including efficiency metrics.

5. **The "optimal" system is a political/economic compromise, not a pure cost optimization.** The authors explicitly acknowledge the PV/Wind/Diesel/Battery system has the lowest LCOE. The fuel cell system is labeled "optimal" only when decarbonization is weighted equally with cost — a value judgment that should be made transparently by policymakers, not embedded in the optimization algorithm.

---

*Document generated from 6-page IEEE conference paper (2023). All numerical values in Sections 1–4 are directly traceable to the source paper. Section 5 contains analytical derivations and interpretations clearly marked as such.*
