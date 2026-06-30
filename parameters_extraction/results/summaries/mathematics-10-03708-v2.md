# Paper Summary: Sizing and Design of a PV-Wind-Fuel Cell Storage System Integrated into a Grid Considering the Uncertainty of Load Demand Using the Marine Predators Algorithm

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Sizing and Design of a PV-Wind-Fuel Cell Storage System Integrated into a Grid Considering the Uncertainty of Load Demand Using the Marine Predators Algorithm
- **Authors:** Fayza S. Mahmoud, Ashraf M. Abdelhamid, Ameena Al Sumaiti, Abou-Hashema M. El-Sayed, Ahmed A. Zaki Diab
- **Journal/Conference name:** Mathematics (MDPI)
- **Year of publication:** 2022
- **DOI:** 10.3390/math10193708
- **Study location:** Marsa Alam, South East Egypt (latitude 25.5°N, longitude 36.7°E, 60 m above sea level)
- **System type:** Grid-connected PV-Wind-Fuel Cell-Electrolyzer-H2 Tank hybrid renewable energy system
- **Whether the study is simulation-based, experimental, or both:** Simulation-based (MATLAB)
- **Software/tools used:** MATLAB
- **Optimization method used:** Marine Predators Algorithm (MPA), Seagull Optimization Algorithm (SOA), and Particle Swarm Optimization (PSO) for comparison

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Rated Capacity / Unit | Number of Units | Key Specifications |
|-----------|----------------------|-----------------|-------------------|
| PV Array | 136,912 US$/unit (capital cost) | 250 (optimal) | η_pv (cell efficiency), wiring efficiency η_wire, temperature coefficient λ_T |
| Wind Turbine | 118,412 US$/unit (capital cost) | 70 (optimal) | Efficiency η_w, friction coefficient β_WT = 0.143, power curve cut-in/rated/cut-off speeds |
| Electrolyzer | 52,311 US$/unit (capital cost) | 1 (rated power 300 kW) | η_electrolyzer (constant efficiency), produces H2 from excess renewable power |
| Hydrogen Tank | 17,004 US$/unit (capital cost) | 1 (max mass 150 kg) | η_st_t = 95% (tank efficiency), HHV_H2 = 39.7 kWh/m² |
| Fuel Cell | 71,219.2 US$/unit (capital power cost) | 1 (rated power 100 kW) | η_fc (FC efficiency), converts H2 to electricity |
| Inverter | 12,387 US$/unit | 1 (rated power 150 kW) | η_inv = 90% (constant), DC/AC conversion |

**Note on units:** The paper describes quantities of PV arrays ("n_PVs"), wind turbines ("n_WTs"), and component-level ratings for electrolyzer (kW), H2 tank mass (kg), FC (kW), and inverter (kW). The capital/replacement/O&M costs in Table 1 are given as "per unit" without specifying the per-unit basis (per kW, per kg, or per device). The optimization decision variables are: number of PV arrays, number of WTs, electrolyzer rated power, mass of H2 tanks, FC rated power, and inverter rated power.

### 2.2 Total System Capacity

- **Total PV capacity:** 250 units (rated power P_r_pv per unit not explicitly stated in kWp)
- **Total Wind capacity:** 70 turbines (rated power P_r_w per turbine not explicitly stated in kW)
- **Electrolyzer conversion capacity:** 300 kW
- **Fuel Cell generation capacity:** 100 kW
- **Inverter capacity:** 150 kW
- **Hydrogen storage capacity:** 150 kg

### 2.3 Component Costs (Capital, Replacement, O&M)

From Table 1 in the paper:

| Component | Capital Cost (US$/unit) | Replacement Cost (US$/unit) | O&M Cost (US$/unit-yr) | Lifetime (years) |
|-----------|------------------------|-----------------------------|------------------------|-----------------|
| Wind Turbine | 118,412 | 52,500 | 5,250 | 20 |
| PV Array | 136,912 | — | 5,000 | 25 |
| Electrolyzer | 52,311 | 22,500 | 7,500 | 20 |
| Hydrogen Tank | 17,004 | 9,000 | 2,250.4 | 20 |
| Fuel Cell | 71,219.2 | 50,000 | 17,500 | 5 |
| Inverter | 12,387 | 7,500 | 1,203.02 | 15 |

**Note:** Currency is USD. Cost year not explicitly stated (assumed 2022 USD based on publication year). FC lifetime is stated as 5 years in Section 6 (p. 16), though Section 2 mathematical modeling mentions FC lifetime of 15 years. The table also lists 15 years for inverter lifetime. The system lifetime is 25 years.

### 2.4 Economic Parameters

- **Project lifetime:** 25 years
- **Interest rate (discount rate):** 6%
- **Inflation rate:** Not reported in this paper
- **Fuel price:** Not applicable (hydrogen-fueled FC, no diesel generator)
- **Grid electricity purchase price (£p_pur):** 0.08 $/kWh
- **Grid electricity selling price (£P_sell):** 0.2 $/kWh
- **Currency and cost year:** USD (year not explicitly stated, assumed 2022)
- **FC lifetime:** 5 years (Section 6) / 15 years (Table 1) — discrepancy noted
- **Wind/PV/Electrolyzer/H2 Tank lifetime:** 20/25/20/20 years respectively
- **Inverter lifetime:** 15 years

### 2.5 Resource Data

- **Solar irradiance data source:** Not explicitly stated (likely meteorological data for Marsa Alam region)
- **Solar radiation measurements:** Solar radiation spectra shown in Figure 6 (Egypt solar radiation intensity map)
- **Wind speed data source:** Not explicitly stated (likely meteorological data for Marsa Alam)
- **Wind speed measurements:** Wind speed spectra shown in Figure 5 (Egypt wind energy map)
- **Data resolution:** Hourly data over one year (8760 hours)
- **Temperature data:** Mentioned as needed for PV output calculation via NOCT model; average annual variation shown in Figure 7
- **Derived hub height wind speed:** V2 = V1 × (H2/H1)^β_WT, where β_WT = 0.143

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

**Case 1 (No load uncertainty, optimal case):**

| Metric | MPA | SOA | PSO |
|--------|-----|-----|-----|
| COE | **0.3044 $/kWh** | 0.3115 $/kWh | 0.5176 $/kWh |
| NPC | **7.350895 × 10⁶ $** | 7.523017 × 10⁶ $ | 1.2498 × 10⁷ $ |

**Case 2 (With load uncertainty):**

| Metric | +5% Uncertainty | +10% Uncertainty | +15% Uncertainty |
|--------|-----------------|------------------|------------------|
| COE | 0.2918 $/kWh | 0.2821 $/kWh | 0.2731 $/kWh |
| NPC | 7.399616 × 10⁶ $ | 7.495652 × 10⁶ $ | 7.586028 × 10⁶ $ |

- **Initial capital cost:** Not explicitly stated as a single value
- **Operating cost (per year):** Not explicitly stated separately from total annual cost
- **Payback period:** Not reported in this paper
- **IRR or ROI:** Not reported in this paper

### 3.2 Reliability Metrics

| Metric | MPA (No uncertainty) | SOA (No uncertainty) | PSO | +5% Unc. | +10% Unc. | +15% Unc. |
|--------|---------------------|---------------------|-----|----------|-----------|-----------|
| **LPSP** | −4.883 × 10⁻¹⁸ | −9.7063 × 10⁻¹⁹ | −3.461 × 10⁻¹⁵ | −4.285 × 10⁻¹⁸ | −5.328 × 10⁻¹⁸ | −5.6198 × 10⁻¹⁸ |

- LPSP constraint: ε_LP = 5%
- All reported LPSP values are essentially zero (negative values are numerical artifacts)
- LOLP: Not reported in this paper
- Unmet load: Not explicitly stated
- System availability: Effectively 100% (LPSP ≈ 0)

### 3.3 Generation Metrics

| Metric | No Uncertainty (MPA) | +5% Unc. | +10% Unc. | +15% Unc. |
|--------|---------------------|----------|-----------|-----------|
| **Sold power to grid (PgS)** | 27.82 × 10³ kWh | 25.321 × 10³ kWh | 23.005 × 10³ kWh | 20.893 × 10³ kWh |
| **Purchased power from grid (Pgp)** | 14.22 × 10³ kWh | 15.585 × 10³ kWh | 20.729 × 10³ kWh | 25.568 × 10³ kWh |

- Renewable fraction: Not explicitly stated
- Excess electricity: Not explicitly stated as a metric
- Hydrogen production/consumption (annual): Not explicitly stated
- Diesel consumption: Not applicable (no diesel generator)
- Load profile type: Not explicitly stated (community/residential load for Marsa Alam, pop. ~11,497)

### 3.4 Load Metrics

- **Total annual load demand (kWh/year):** Not explicitly stated as a single value
- **Average daily load (kWh/day):** Not explicitly stated
- **Peak load:** Not explicitly stated
- **Average load:** Not explicitly stated
- **Load profile type:** Not explicitly stated; inferred as community load for Marsa Alam (~11,497 population)

### 3.5 Optimal Configuration (if optimization was performed)

**Optimal sizing (MPA, no uncertainty):**
- Number of PV arrays: **250**
- Number of Wind Turbines: **70**
- Electrolyzer rated power: **300 kW**
- Mass of H₂ tanks: **150 kg**
- FC rated power: **100 kW**
- Inverter rated power: **150 kW**

**Objective function:** min (j₁ × COE + j₂ × LPSP) — a weighted sum of COE and LPSP (Equation 29)

**Constraints applied:**
- Power balance: P_ld = P_pv + P_w + P_fc ± P_g (Equation 27)
- LPSP ≤ ε_LP = 5%
- H₂ tank capacity limits: MH2t_min ≤ MH2t(t) ≤ MH2t_max (Equation 28)
- Fluctuation rate of power sold to grid bounded by ε_fl
- Simulation settings: max iterations = 50, searching agents = 30

**Sensitivity analysis:** Performed via load uncertainty scenarios at +5%, +10%, and +115% above nominal load.

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

The dispatch strategy is defined by the energy balance equation:

**E_b = P_ren − P_ld**, where P_ren = P_PV + P_WT

**Three operational cases:**

1. **E_b = 0 (Balance):** RES generation exactly equals load demand. No grid interaction, no electrolyzer or FC operation.

2. **E_b > 0 (Surplus):** RES exceeds load. The extra power feeds the electrolyzer to produce hydrogen stored in tanks. After the hydrogen tank reaches maximum capacity (MH2t_max), the remaining excess power is sold to the utility grid.

3. **E_b < 0 (Deficit):** RES cannot meet load. The fuel cell generates electricity from stored hydrogen. If the FC output is insufficient (hydrogen depleted), the remaining deficit is covered by purchasing power from the grid.

**Priority order of generation sources:**
1. PV + Wind (primary)
2. Fuel Cell (backup storage, dispatched when RES insufficient)
3. Utility Grid (secondary/auxiliary backup)

### 4.2 Power Flow Logic

**Excess renewable energy handling:**
- If H₂ tank not at maximum → electrolyzer produces hydrogen
- If H₂ tank at maximum → sell surplus to grid

**Deficit handling:**
- Fuel cell operates using stored H₂
- If FC insufficient or H₂ depleted → purchase from grid

**Production and consumption logic:**
- Electrolyzer: converts excess electrical energy to chemical energy (H₂)
- Conversion: H₂ stored at high pressure in tanks
- FC: converts stored H₂ back to electricity via electrochemical reaction
- Inverter: converts DC from PV, WT, and FC to AC for load/grid

### 4.3 Control Parameters

- **Inverter efficiency η_inv:** 90% (constant)
- **Hydrogen tank efficiency η_st_t:** 95%
- **Higher heating value of hydrogen HHV_H2:** 39.7 kWh/m²
- **Wind friction coefficient β_WT:** 0.143
- **Maximum iterations:** 50
- **Searching agents:** 30
- **LPSP constraint ε_LP:** 5%
- **H₂ tank minimum/maximum:** bounds enforced (MH2t_min ≤ MH2t(t) ≤ MH2t_max) — specific numerical values not stated
- **Grid purchase price:** 0.08 $/kWh
- **Grid sell price:** 0.2 $/kWh

### 4.4 Algorithm Flow

The energy management strategy is described by the following step-by-step logic (Section 3):

1. Calculate hourly power from PV (P_pv) and wind (P_w) using Equations (1)–(5)
2. Calculate energy balance E_b = (P_PV + P_W) − P_ld
3. If E_b = 0: no action needed
4. If E_b > 0:
   a. Direct surplus to electrolyzer to produce H₂ (Equation 8–9)
   b. Store H₂ in tanks (Equations 10–11)
   c. If H₂ tank reaches MH2t_max, sell remaining surplus to grid (Equation 7)
5. If E_b < 0:
   a. Supply deficit from FC using stored H₂ (Equations 12–13)
   b. If FC cannot satisfy deficit (insufficient H₂ or capacity), purchase from grid (Equation 6)
6. Calculate total annual cost including capital, replacement, O&M, grid purchase cost, minus grid sales revenue (Equations 16–23)
7. Evaluate objective function: min(j₁·COE + j₂·LPSP) (Equation 29)
8. Optimization algorithm (MPA/SOA) iterates to find best component sizes

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

The system is designed for Marsa Alam — a hot desert coastal region with abundant solar radiation and strong winds. The optimal configuration features 250 PV arrays and 70 wind turbines as primary generation, backed by a 300 kW electrolyzer, 150 kg hydrogen storage, 100 kW fuel cell, and 150 kW inverter.

**Typical day (summer, based on Figure 12):**

*Morning (pre-dawn to ~04:00):* PV output is zero or near-zero. Wind speed is at its peak (per Figure 7 showing nighttime wind peaks in the region). The wind turbines generate significant power, but if combined wind output falls below load demand, the fuel cell compensates using overnight-stored hydrogen. With 70 turbines, substantial nighttime wind energy is harvested — this is characteristic of desert coastal regions where land-sea breezes create strong nighttime winds.

*Mid-morning (~04:00–07:00):* Wind power begins changing (potentially decreasing as daytime approaches), while PV ramps up with sunrise. The transition period may require continued FC support if wind drops faster than PV ramps.

*Daytime (08:00–16:00):* Solar radiation peaks. From Figure 7, Marsa Alam receives strong irradiance reaching levels typical of the Red Sea coast (often >6-7 kWh/m²/day). The 250 PV arrays produce substantial power. Combined with continuing wind generation, total RES output likely exceeds the load. The surplus charges the electrolyzer (300 kW capacity), producing hydrogen that is stored for nighttime use. Once the 150 kg hydrogen tank reaches maximum capacity, excess power is sold to the grid at 0.2 $/kWh — nearly 2.5× the purchase price of 0.08 $/kWh, creating favorable arbitrage.

*Evening (17:00–20:00):* Solar drops as the sun sets, but load often peaks in the evening (residential/ commercial lighting, cooling). The deficit is covered first by the 100 kW fuel cell drawing from hydrogen storage. If hydrogen is depleted, the deficit triggers grid purchases at 0.08 $/kWh.

*Night (20:00–04:00):* Wind picks up again (per Figure 7 patterns), supplementing the FC. The system relies on the combination of wind and hydrogen-to-electricity conversion.

**Seasonal variations:** Marsa Alam has hot summers and mild winters. Solar output would be higher in summer (longer days, stronger irradiance), while wind patterns may shift seasonally. The 8760-hour simulation captures these dynamics, and the optimization ensures year-round LPSP stays at essentially zero.

### 5.2 System Behavior Analysis

**Why this configuration?** The authors found that 250 PV arrays and 70 wind turbines combined with hydrogen storage and grid interaction provides the optimal economic balance. The system sells to the grid at 2.5× the purchase price — this economic asymmetry incentivizes maximizing renewable generation and hydrogen storage to enable high-value sales.

**The hydrogen storage arbitrage:** The paper's energy management is fundamentally driven by price arbitrage. At 0.2 $/kWh selling vs. 0.08 $/kWh buying, there is a strong economic incentive to:
1. Maximize renewable generation
2. Store surplus as hydrogen (when tank not full)
3. Sell maximum to grid (when tank full)

This explains why purchased power (14,220 MWh/year sold) actually exceeds purchased power (same magnitude reported as 14.22 × 10³ kWh/year bought from grid — likely a unit issue since total system scale suggests MWh) — actually rechecking, the values are 27.82 × 10³ kWh sold and 14.22 × 10³ kWh purchased, which are relatively small annual figures for a 250-panel, 70-turbine system, suggesting these might represent specific normalized or hourly-average values.

**Load uncertainty effect:** Counter-intuitively, COE *decreases* with load uncertainty (+5%, +10%, +15%). The COE drops from 0.3044 to 0.2731 $/kWh. This likely reflects the mathematical formulation where increasing load increases the denominator in COE calculation (COE = total annual cost / total energy served) — the system's fixed costs are spread over a larger energy base. However, NPC increases from 7.35M to 7.59M, reflecting the real additional cost of serving more load.

### 5.3 Critical Evaluation

**Strengths:**
- Novel application of MPA to hybrid renewable system sizing
- Realistic case study with actual regional data for Marsa Alam
- Grid interaction with asymmetric pricing (sell 2.5× buy) reflects real feed-in tariff structures
- Load uncertainty analysis adds practical robustness

**Limitations:**
- The paper does not state the individual PV module rated power (kWp per panel) or individual turbine rated power — making the total generation capacity ambiguous
- LPSP values are reported as negative numbers (×10⁻¹⁸), which are mathematically impossible (LPSP is a probability between 0 and 1). These are numerical artifacts from the solver, not real values
- The "optimal" configuration is identical across all load uncertainty cases (same sizes), suggesting the optimizer consistently converges to the same solution — this is surprising and may indicate limited search space exploration
- No battery storage is included — only hydrogen-based storage, which has lower round-trip efficiency
- The electrolyzer/FC round-trip efficiency (η_ele × η_fc) is not fully specified since η_ele and η_fc numerical values are not provided in the parametric data section
- Total energy served (annual load in kWh) is not explicitly stated, making it impossible to verify the COE calculation

**Assumptions:**
- Hourly resolution (8760 time steps)
- H2 storage round-trip is the sole storage mechanism
- Grid is always available (no grid outage modeling)
- Constant electrolyzer and FC efficiencies (simplification)
- Inverter efficiency constant at 90%

### 5.4 Derived/Inferred Values

1. **COE denominator (total annual served energy):** From COE = Can_tot / Σ P_ld(t), we can infer annual load:
   - COE = Can_tot / (Total annual energy)
   - With COE = 0.3044 $/kWh and total system cost/CRF structures, the implied annual load can be partially reconciled from the relation: NPC = CRF × Can_tot, and COE = NPC / (Σ P_ld × CRF), giving Σ P_ld = NPC / (COE × CRF)
   - CRF(6%,25) = 0.0782 → implied annual load = 7.350895×10⁶ / (0.3044 × 0.0782 / 0.0782) — this requires more information. From COE formula (Eq. 24): COE = NPC / (Σ P_ld × CRF), so Σ P_ld = NPC / (COE × CRF) = 7.350895×10⁶ / (0.3044 × 0.0782) ≈ 30,857,000 kWh/year ≈ 30.86 GWh/year. This would imply average daily load ≈ 84,500 kWh/day and average load ≈ 3,523 kW.

2. **Grid interaction magnitude:** Sold power (27,820 MWh/year) > Purchased (14,220 MWh/year) at the optimal case, suggesting the system is a net exporter to the grid.

3. **Load growth impact:** Under +15% load uncertainty, purchased power nearly doubles (14.22 → 25.57 × 10³) while sold power decreases (27.82 → 20.89 × 10³), indicating the system transitions from net exporter to more balanced importer.

### 5.5 Key Takeaways

1. **MPA outperforms SOA and PSO:** The Marine Predators Algorithm achieves COE of 0.3044 $/kWh vs. SOA's 0.3115 $/kWh — a modest but meaningful improvement in the context of optimizing component sizing.

2. **Hydrogen storage enables grid arbitrage:** The asymmetric grid prices (sell at 0.2 $/kWh, buy at 0.08 $/kWh) create strong economic incentive for hydrogen-based energy storage that time-shifts surplus renewable energy.

3. **Grid-connected systems are economically superior:** The grid acts as both backup (when RES+FC insufficient) and revenue source (when surplus exceeds hydrogen storage capacity), enabling near-zero LPSP while maintaining economic viability.

4. **Load uncertainty reduces COE but increases NPC:** Serving more load with the same asset base improves unit economics (lower COE) but increases total system cost due to more grid purchases and potentially faster component cycling.

5. **Marsa Alam is ideal for hybrid renewables:** The combination of high solar radiation and strong coastal winds in south Egypt makes it an excellent location for PV-wind-hydrogen hybrid systems.

---

*Note: Some numerical values in this paper (particularly grid exchange powers in Table 2) appear to use ambiguous units — reported as "×10³" without explicit kWh clarification. The annual load value and individual component power ratings (kWp per PV panel, kW per wind turbine) are not explicitly stated in the paper, which limits reproducibility of the results.*
