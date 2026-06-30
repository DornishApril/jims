# Paper Summary: Design optimization of a multi-source renewable energy system using a novel method based on selective ensemble learning

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Design optimization of a multi-source renewable energy system using a novel method based on selective ensemble learning
- **Authors:** Anas Bouaouda, Yassine Sayouti
- **Journal/Conference:** Procedia Computer Science (Elsevier)
- **Year of publication:** 2024
- **DOI:** 10.1016/j.procs.2024.05.011
- **Conference:** International Symposium on Green Technologies and Applications (ISGTA'2023)
- **Study location:** Dakhla City, Southwest Morocco (latitude: 23.9337, longitude: -15.6694)
- **System type:** Stand-alone (off-grid) PV/Wind Turbine/Fuel Cell hybrid renewable energy system with hydrogen storage (PV/WT/FC)
- **Study type:** Simulation-based (numerical optimization study)
- **Software/tools used:** MATLAB
- **Optimization method used:** SEMPA (Selective Ensemble Marine Predators Algorithm) — a novel enhanced variant of the Marine Predators Algorithm (MPA) that integrates a selective ensemble learning strategy to prevent premature convergence and increase exploration. Also compared against conventional MPA, Harmony Search (HS), and Particle Swarm Optimization (PSO).
- **Affiliation:** LSIB Laboratory, FST Mohammedia, Hassan II University of Casablanca, Morocco
- **License:** CC BY-NC-ND 4.0 (open access)

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

The HRES consists of the following components (mathematical models from Section 2):

| Component | Description | Model/Specifications |
|---|---|---|
| PV Array | PV solar panels | Power output: P_PV = N_PV × P_r × η_PV × (G/G_ref) × [1 + β(T - T_ref)]. Rated per unit capacity: 1 kW (per panel/string unit) |
| Wind Turbines (WT) | Wind energy conversion | Piecewise cubic power curve: 0 below cut-in (V_in) and above cut-out (V_out); cubic region between V_in and V_r; rated power P_r between V_r and V_out. Number of units optimized |
| Electrolyzer | Water electrolysis for H2 production | P_el = P_ren_el × η_el (power consumed from renewable excess) |
| Hydrogen Tank | H2 storage | Energy balance: E_ht(t) = E_ht(t-1) + P_ren_el(t)×Δt - P_ht_fc(t)×Δt×η_ht |
| Fuel Cell (FC) | Electricity generation from stored hydrogen | P_fc_inv = P_ht_fc × η_fc |
| Inverter | DC/AC conversion | Rated capacity in kW (optimized) |

**Optimal configuration (SEMPA — the best performing algorithm per Table 3):**

| Component | Variable | Value |
|---|---|---|
| PV panels | N_pv | 47 kW |
| Wind turbines | N_wt | 55 kW |
| Electrolyzer | P_el | 35.39 kW |
| Fuel cell | P_fc | 27.90 kW |
| Hydrogen tank mass | M_HTS | 84.35 kg |
| Inverter | P_inv | 48.11 kW |

**Note on discrepancy:** The paper's prose (Section 5) states "SEMPA achieves a minimum TNPC of 0.9689 M$ and a COE of 0.3127 $/kWh" but Table 3 shows SEMPA TNPC = 0.9627 M$, COE = 0.3115 $/kWh. The prose appears to have swapped SEMPA and MPA values (MPA in Table 3 has TNPC = 0.9689 M$, COE = 0.3127 $/kWh).

**Alternative optimal configurations for comparison (LPSPmax = 5% constraint):**

| Algorithm | N_pv (kW) | N_wt (kW) | P_el (kW) | P_fc (kW) | M_HTS (kg) | P_inv (kW) | TNPC (M$) | LPSP | COE ($/kWh) |
|---|---|---|---|---|---|---|---|---|---|
| SEMPA | 47 | 55 | 35.39 | 27.90 | 84.35 | 48.11 | 0.9627 | 0.04647 | 0.3115 |
| MPA | 42 | 57 | 40.39 | 26.84 | 92.74 | 48.65 | 0.9689 | 0.04747 | 0.3127 |
| HS | 47 | 55 | 28.17 | 30.96 | 84.48 | 48.77 | 0.9904 | 0.04759 | 0.3215 |
| PSO | 54 | 52 | 36.82 | 28.20 | 79.73 | 48.25 | 0.9663 | 0.04861 | 0.3143 |

### 2.2 Total System Capacity

| Metric | Value (SEMPA) |
|---|---|
| Total generation capacity (PV + WT) | 47 + 55 = **102 kW** |
| Fuel cell capacity | 27.90 kW |
| Electrolyzer capacity | 35.39 kW |
| Total conversion capacity (inverter) | 48.11 kW |
| Hydrogen storage capacity | 84.35 kg |

- Total generation capacity: **102 kW** (renewable) + **27.90 kW** (fuel cell) = **129.9 kW** total dispatchable + non-dispatchable generation
- Total hydrogen storage: **84.35 kg** of H2

### 2.3 Component Costs (Capital, Replacement, O&M)

All costs from Table 1 (currency: US$, year not explicitly stated but likely 2023 USD based on references).

| Component | Capital Cost (US$/unit) | O&M Cost (US$/unit-yr) | Replacement Cost (US$/unit) | Rated Capacity | Lifetime (years) |
|---|---|---|---|---|---|
| Wind Turbine | 3,200 | 32 | 3,000 | 1 kW | 20 |
| PV panel | 2,000 | 20 | 1,800 | 1 kW | 20 |
| Inverter | 800 | 7 | 750 | 1 kW | 15 |
| Electrolyzer | 2,000 | 20 | 1,500 | 1 kW | 20 |
| Hydrogen tank | 1,300 | 15 | 1,200 | 1 kg | 20 |
| Fuel cell | 3,000 | 40 | 2,500 | 1 kW | 5 |

### 2.4 Economic Parameters

| Parameter | Value |
|---|---|
| Project lifetime (R) | 20 years |
| Real interest rate (ir) | 6% |
| Nominal interest rate | 9% |
| Inflation rate (f) | 3% |
| Currency | US$ (USD) |
| Cost year | Likely 2023 USD (not explicitly stated) |
| Max allowable equipment quantity (N_max) | 2,000 units |
| LPSP maximum (constraint) | 5% |

### 2.5 Resource Data

- **Solar irradiance:** Hourly data shown in Figure 2a (ranges from 0 to ~1000 W/m²). Annual average value NOT explicitly stated in the paper (only available from the figure, which cannot be read precisely).
- **Temperature:** Hourly data shown in Figure 2b (ranges from ~10°C to ~30°C). Average NOT explicitly stated.
- **Wind speed:** Hourly data shown in Figure 2c (ranges from ~2 m/s to ~10 m/s). Average NOT explicitly stated.
- **Data source:** NOT explicitly stated in the paper. (Likely NASA or meteorological station data, but not specified.)
- **Study location coordinates:** Latitude 23.9337, Longitude -15.6694 (Dakhla, Morocco)

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

| Metric | Value (SEMPA best) |
|---|---|
| COE (Cost of Energy) | **0.3115 $/kWh** |
| TNPC (Total Net Present Cost) | **0.9627 M$** (962,750 $) |

**Note on discrepancy:** The paper's prose (Section 5 and abstract) states COE = 0.3127 $/kWh and TNPC = 0.9689 M$ for SEMPA, but these values correspond to MPA in Table 3. Table 3 shows SEMPA COE = 0.3115 $/kWh and TNPC = 0.9627 M$.

- Initial capital cost: Not separately stated
- Operating cost per year: Not separately stated
- Payback period: Not reported
- IRR/ROI: Not reported

**Statistical results across 30 runs (PV/WT/FC system, Table 2):**

| Index | SEMPA | MPA | HS | PSO |
|---|---|---|---|---|
| Best (×10⁵ $) | 9.6275 | 9.6886 | 9.9043 | 9.6634 |
| Worst (×10⁵ $) | 9.7865 | 10.937 | 12.147 | 11.043 |
| Mean (×10⁵ $) | 9.6799 | 9.9447 | 10.664 | 10.102 |
| Std (×10³ $) | 4.0225 | 30.977 | 58.510 | 39.850 |
| Rank | 1 | 2 | 3 | 4 |

### 3.2 Reliability Metrics

| Metric | Value (SEMPA) |
|---|---|
| LPSP (Loss of Power Supply Probability) | **0.04647** (4.647%) |

- LOLP: Not reported separately (LPSP used as reliability metric)
- Unmet load (kWh/year): Not reported
- Hours of unmet load per year: Not reported
- System availability: Not reported

### 3.3 Generation Metrics

- Total annual electricity generation: **Not reported** in this paper
- Generation by source (PV, WT, FC): **Not reported**
- Renewable fraction: **Not reported**
- Excess electricity: **Not reported**
- Battery throughput: **Not applicable** (no battery in this system; hydrogen storage used instead)
- Hydrogen production (kg/year): **Not reported**
- Hydrogen consumption (kg/year): **Not reported**
- Diesel consumption: **Not applicable** (no diesel generator in this system)
- Grid import/export: **Not applicable** (stand-alone system)

### 3.4 Load Metrics

| Metric | Value |
|---|---|
| Total annual load demand | Not explicitly stated |
| Average daily load | Not explicitly stated |
| Peak load | **50 kW** ("IEEE RTS load with a 50 kW peak") |
| Average load | Not explicitly stated |
| Load profile type | IEEE RTS (Reliability Test System) load profile |

Load profile visible in Figure 2d ranges from ~20 kW to 50 kW.

### 3.5 Optimal Configuration

| Parameter | Value |
|---|---|
| Winning configuration | SEMPA: 47 kW PV + 55 kW WT + 35.39 kW Electrolyzer + 27.90 kW FC + 84.35 kg H2 + 48.11 kW Inverter |
| Objective function | Minimize TNPC |
| Constraints | LPSP ≤ 5%, 0 ≤ N_i ≤ 2000, E_tank(0) ≤ E_tank(8760) |
| Sensitivity analysis variables | Not performed in this paper |
| Optimization variables | N_WT, N_PV, P_el, P_fc, M_tank, P_inv |
| Population size | 50 |
| Max iterations | 100 |
| Independent runs | 30 |

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACT (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

The paper does NOT explicitly describe a detailed dispatch strategy or power management logic for the HRES. It provides mathematical models for each component but does not specify a priority-based dispatch order or control algorithm.

The system configuration suggests:
- PV and WT serve as primary generation sources
- Excess renewable energy powers the electrolyzer to produce hydrogen
- When renewable generation is insufficient, the fuel cell converts stored hydrogen to electricity
- The inverter converts DC power from PV, FC, and potentially WT rectified output to AC for the load
- The hydrogen tank acts as the primary energy storage medium (no batteries)

### 4.2 Power Flow Logic

Based on the mathematical models in Section 2:

- **Surplus renewable energy** (when P_PV + P_WT > Load): The excess power feeds the electrolyzer: P_el = P_ren_el × η_el, producing hydrogen stored in the tank.
- **Deficit** (when P_PV + P_WT < Load): The fuel cell draws hydrogen from the tank to supply power: P_fc_inv = P_ht_fc × η_fc
- **Hydrogen tank energy balance:** E_ht(t) = E_ht(t-1) + P_ren_el(t)×Δt - P_ht_fc(t)×Δt×η_ht
- **Grid interaction:** None (stand-alone system)
- **Dump load:** Mentioned indirectly (excess that cannot be utilized), but no specific logic described

**NOT described in the paper:**
- Battery charging/discharging (no battery in this system)
- Priority rules between FC and electrolyzer
- Minimum up-time or ramp rate constraints
- Setpoint thresholds for starting/stopping FC or electrolyzer

### 4.3 Control Parameters

| Parameter | Value | Source |
|---|---|---|
| η_PV (PV efficiency) | Variable (function of temperature) | Eq. (1): contains β (temperature coefficient), T_ref (reference temp) — specific values NOT given in the paper |
| η_el (electrolyzer efficiency) | Not stated as a single value in the paper | Modeled in Eq. (3) |
| η_ht (hydrogen tank efficiency) | Not stated | Modeled in Eq. (4) |
| η_fc (fuel cell efficiency) | Not stated | Modeled in Eq. (5) |
| G_ref (reference irradiance) | Implied standard 1000 W/m² | Standard convention |
| V_in, V_r, V_out (WT parameters) | Not stated | Mentioned in Eq. (2) but no numeric values |
| SOC limits for hydrogen tank | Implied by E_tank(0) ≤ E_tank(8760) constraint | Not given as numeric percentages |
| Diesel minimum load ratio | N/A | No diesel generator |
| Inverter efficiency | Not stated | |

### 4.4 Algorithm Flow

The paper does NOT describe a step-by-step energy management algorithm or decision tree for power dispatch. The optimization determines component SIZES (number of units), not the real-time OPERATION strategy. The mathematical model is a framework for sizing optimization, not a control algorithm.

The optimization framework flow (SEMPA):
1. Initialize population of candidate solutions (5 solutions × 6 variables)
2. Evaluate fitness (TNPC) for each candidate
3. Apply SEMPA selective ensemble learning to dynamically adjust phase selection probabilities based on past performance
4. Iterate up to 100 times or until convergence
5. Select best solution (minimum TNPC satisfying LPSP ≤ 5%)

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

This system operates as a PV/Wind/Hydrogen microgrid for the Dakhla region of Morocco. Based on the component models and optimal sizes (SEMPA configuration), we can reconstruct a typical operational day:

**Morning (~6-9 AM):**
Solar irradiance begins to ramp up from zero. In the early morning hours, PV output is near zero while wind may be available (Dakhla coastal winds typically range from 2-10 m/s). The 55 kW of wind turbines likely provide the bulk of generation in these hours. If wind generation exceeds the load (which ranges 20-50 kW), excess power feeds the 55 kW electrolyzer. If wind is insufficient, the 27.90 kW fuel cell begins operating, drawing hydrogen from the 84.35 kg tank.

**Midday (~10 AM - 3 PM):**
This is peak solar generation. With 47 kW of PV at Dakhla's high irradiance levels (figure shows peak ~1000 W/m²), the PV array could output close to rated capacity. Combined with wind (which may decrease in midday), total renewable generation likely exceeds the ~50 kW peak load significantly. The surplus is directed to the electrolyzer (35.39 kW capacity), producing hydrogen at a rate determined by:
- H2 production (kg/h) ≈ P_el(MW) / (HHV of H2 ≈ 39.4 kWh/kg) / conversion efficiency

Assuming electrolyzer efficiency of ~70% (common for PEM electrolyzers) and 35.39 kW input: approximately 35.39 × 0.70 / 39.4 ≈ 0.63 kg/h of hydrogen produced.

**Evening (~4-8 PM):**
Solar drops rapidly while load may remain at moderate levels (figure shows load 30-45 kW during evening). With PV declining, the deficit is covered by wind (if available) and the fuel cell. The 27.90 kW FC can supply a significant fraction of the load. Assuming FC efficiency of ~50% (typical for PEM fuel cells): H2 consumption ≈ 27.90 / (0.50 × 39.4) ≈ 1.42 kg/h when running at full capacity.

**Night (~9 PM - 5 AM):**
Zero solar generation. The system relies entirely on wind turbines, fuel cell, and stored hydrogen. The 84.35 kg hydrogen tank provides a buffer. At full FC output consuming ~1.42 kg/h, the tank could theoretically support ~84.35/1.42 ≈ 59 hours of continuous FC operation at full load. However, the actual system is designed for daily charging/discharging cycles.

**Seasonal variations:**
The paper shows annual hourly profiles (8760 hours) in Figure 2 but does not discuss seasonal details. Dakhla has semi-arid climate with relatively consistent wind patterns (coastal trade winds) and strong solar insolation year-round, making it favorable for hybrid renewable systems.

### 5.2 System Behavior Analysis

**Why this configuration is optimal:**
The SEMPA-optimized configuration balances three cost drivers:
1. **PV cost** ($2000/kW) vs generation potential: At 47 kW, PV provides substantial daytime generation
2. **Wind cost** ($3200/kW, higher than PV but capacity factor may be better): At 55 kW, wind provides complementary generation (especially during cloudy periods and night)
3. **Hydrogen storage cost** (Electrolyzer $2000/kW, FC $3000/kW, Tank $1300/kg): The 35.39 kW electrolyzer, 27.90 kW FC, and 84.35 kg tank represent the cost-optimal storage size to cover the ~4.65% LPSP target

**Trade-offs identified by authors:**
- Larger PV arrays reduce fuel cell and diesel dependency but increase capital cost
- More improves reliability but at higher per-kW cost than PV
- Larger hydrogen storage increases reliability (lower LPSP) but adds cost
- The SEMPA algorithm's selective ensemble strategy prevents getting stuck in local optima, allowing it to find better solutions than MPA, PSO, or HS

**Key insight:** SEMPA achieves a standard deviation of only $4,022 across 30 runs (vs $30,977 for MPA, $58,510 for HS, $39,850 for PSO), demonstrating superior robustness and consistency.

**Edge case behavior (inferred from model):**
- Extended cloudy/low-wind periods: The 84.35 kg hydrogen tank provides the buffer. If the tank is depleted and renewables are insufficient, LPSP events occur (designed to be ≤5% of the time)
- The constraint E_tank(0) ≤ E_tank(8760) ensures the hydrogen tank has at least as much energy at year-end as year-start, preventing solutions that appear optimal only by fully depleting the tank

### 5.3 Critical Evaluation

**Reasonableness of assumptions:**
- The IEEE RTS load profile with 50 kW peak is a reasonable standardized test load but may not represent actual village demand in Dakhla
- No battery storage is included — only hydrogen storage. This is a design choice but batteries could provide faster response for transient conditions
- The paper references component costs from other references [3, 7], suggesting costs Moroccan prices
- The optimization uses 1-hour time steps (Δt = 1), which is standard but may miss sub-hourly transients
- No discussion of component degradation over the 20-year lifetime

**Limitations:**
1. No sensitivity analysis on component costs, discount rates, or load growth
2. No comparison with battery-based systems or grid-extension alternatives
3. No actual operational simulation results showing the power balance hour-by-hour
4. The COE values (0.3115-0.3215 $/kWh) are relatively high compared to grid electricity in most countries but reasonable for remote off-grid hydrogen-based systems
5. No diesel generator backup — the system relies entirely on PV, wind, and hydrogen, which means reliability depends entirely on renewable resource availability and storage sizing
6. Wind turbine efficiency parameters (cut-in, rated, cut-out speeds) are not given, making reproduction difficult
7. Fuel cell and electrolyzer efficiencies are not stated

**Generalizability:**
- The SEMPA optimization methodology is generalizable to any location and system configuration
- The specific numerical results (optimal sizes, costs) are specific to Dakhla's resources and the cost assumptions used
- The finding that SEMPA outperforms MPA/PSO/HS is likely generalizable given the statistical robustness demonstrated

**What if diesel were included?**
A diesel generator would reduce LPSP further and potentially lower the required hydrogen storage, but at the cost of fuel consumption, emissions, and ongoing fuel price risk. Given Morocco's location and diesel import costs, the all-renewable approach with hydrogen may be economically competitive for remote areas.

### 5.4 Derived/Inferred Values

*(All derived values shown with calculations and marked as estimated)*

**Daily energy demand:**
- Load profile is IEEE RTS with 50 kW peak
- The figure shows load ranging from ~20 to 50 kW
- Average load appears to be approximately 35-40 kW (estimated from visual inspection of load curve)
- **Annual energy demand ≈ 35 kW avg × 8760 h ≈ 306,600 kWh/year** (estimated, average load not explicitly stated)
- **Annual energy demand = 50 kW peak × capacity factor × 8760 h**. If capacity factor ≈ 70%: ~306,600 kWh/year

**Storage autonomy:**
- Hydrogen tank:35 kg × 39.4 kWh/kg (HHV) × η_fc (assume 50%) ≈ **1,662 kWh of usable electrical energy**
- At average load of ~35 kW: **~47 hours of full-load autonomy** from hydrogen storage alone
- This is a substantial storage buffer for a 129.9 kW system

**Component cost breakdown for SEMPA configuration (derived):**

| Component | Units | Unit Cost | Total Capital |
|---|---|---|---|
| Wind Turbine | 55 kW | $3,200/kW | $176,000 |
| PV panel | 47 kW | $2,000/kW | $94,000 |
| Inverter | 48.11 kW | $800/kW | $38,488 |
| Electrolyzer | 35.39 kW | $2,000/kW | $70,780 |
| Hydrogen tank | 84.35 kg | $1,300/kg | $109,655 |
| Fuel cell | 27.90 kW | $3,000/kW | $83,700 |
| **Total initial capital** | | | **~$572,623** |

- TNPC of $962,750 includes replacements, O&M, and discounted costs over 20 years
- TNPC/Initial capital ≈ 1.68, indicating significant O&M and replacement costs over the project life (this is plausible given the FC lifetime of only 5 years, requiring ~3 replacements in 20 years)

**COE verification:**
- COE = TNPC × CRF / Annual_energy, where CRF = ir(1+ir)^R / ((1+ir)^R - 1) = 0.06(1.06)^20 / ((1.06)^20 - 1) = 0.0872
- Annualized cost = $962,750 × 0.0872 = $83,952/year
- Implied annual energy = $83,952 / $0.3115 ≈ **269,508 kWh/year**
- This implies average load = 269,508 / 8760 ≈ **30.8 kW average**
- This is consistent with the load profile figure showing significant hours below 35 kW

### 5.5 Key Takeaways

1. **SEMPA outperforms existing algorithms:** The Selective Ensemble Marine Predators Algorithm achieves the lowest TNPC ($962,750) and best STD ($4,022) compared to MPA ($968,860), PSO ($966,340), and HS ($990,430). The selective ensemble strategy meaningfully improves optimization reliability.

2. **Hydrogen-only storage can achieve high reliability:** The off-grid PV/WT/FC system with 84.35 kg hydrogen storage achieves LPSP of 4.647% (under the 5% constraint), demonstrating that hydrogen storage alone can provide adequate reliability without batteries or diesel.

3. **COE of ~0.31 $/kWh is competitive for remote off-grid systems:** While higher than grid electricity, this COE is reasonable for a fully renewable off-grid system with hydrogen storage in a remote Moroccan location.

4. **Wind contributes more than PV in the optimal mix:** The optimal configuration has 55 kW wind vs 47 kW PV despite wind being 60% more expensive per kW ($3,200 vs $2,000), suggesting wind's higher capacity factor in Dakhla justifies the investment.

5. **The paper lacks operational detail:** Despite detailed optimization methodology, the paper does not report actual generation metrics, hourly dispatch behavior, or system performance beyond the cost/reliability metrics. This limits the paper's usefulness for understanding actual system operation.

---

## REFERENCES

[1-14] As listed in the paper's reference section. Key references:
- [3] Naderipour et al. (2022) — cost data reference
- [7] Bouaouda & Sayouti (2023) — Dandelion Optimizer work and cost data reference
- [11] Faramarzi et al. (2020) — original MPA paper

---

*Document generated from full-text extraction of Bouaouda & Sayouti (2024), Procedia Computer Science 236:111-118. All directly extracted values traceable to Tables 1-3 and Section 5 text. Section 5 analysis values are derived/inferred and marked as such.*
</｜DSML｜parameter>