# Paper Summary: Design and Economic Analysis of a Stand-alone microgrid system using Dandelion Optimizer - A rural case in Southwest Morocco

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Design and Economic Analysis of a Stand-alone microgrid system using Dandelion Optimizer - A rural case in Southwest Morocco
- **Authors:** Anas Bouaouda, Yassine Sayouti
- **Affiliation:** Faculty of Science and Technology, Hassan II University of Casablanca, Morocco
- **Journal/Conference:** 2023 3rd International Conference on Innovative Research in Applied Science, Engineering and Technology (IRASET) — IEEE
- **Year of publication:** 2023
- **DOI:** 10.1109/IRASET57153.2023.10152945
- **Study location:** Lagouira City, Southwest Morocco (latitude: 20.8333, longitude: -17.0917)
- **System type:** Off-grid HRES: PV/WT/Electrolyzer/Fuel Cell/Hydrogen Tank hybrid microgrid (no diesel generator, no battery explicitly modeled as a state-of-charge entity — batteries mentioned conceptually but not modeled as a primary storage component)
- **Study type:** Simulation-based (MATLAB/simulation, no experimental validation reported)
- **Software/tools:** Not explicitly named (models implemented numerically with hourly time steps over 1 year); HOMER referenced in literature comparison but not stated as the current study's tool
- **Optimization method:** Dandelion Optimizer (DO) — a novel metaheuristic proposed by Zhao et al. (2022). Comparison against Genetic Algorithm (GA) and Particle Swarm Optimization (PSO)

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Rated Size | Units/Count | Key Specifications |
|-----------|-----------|-------------|-------------------|
| PV array (per module) | 1 kW (STC) | **60 units** | Temperature coefficient: -3.7 x 10^-3 /°C; Cell temp at STC: 25°C |
| Wind Turbine (WT) | 1 kW (per turbine basis) | **55 units** | Hub height: 20 m; Cut-in: 3 m/s; Rated wind speed: 11 m/s; Cut-out: 25 m/s |
| Inverter | Rated | **49.46 kW** | Efficiency: 95% |
| Electrolyzer (EL) | Rated power | **18.85 kW** | Efficiency: 75% |
| Fuel Cell (FC) | Rated power | **20.22 kW** | Efficiency: 60% |
| Hydrogen Tank (HT) | Storage mass | **74.93 kg** | HHV of H2: 39.72 kWh/kg |

> **Notes from Table I & III (DO optimal):** System sizing is in terms of component counts for PV and WT, and rated power/capacity for EL, FC, HT, and inverter. The paper does NOT model battery state-of-charge as a dynamic variable — batteries are mentioned in introduction as part of general HRES but the actual simulated system is PV/WT/FC/EL/HT only.

### 2.2 Total System Capacity

- **Total PV capacity:** 60 kW (60 x 1 kW)
- **Total WT capacity:** 55 kW (55 x 1 kW)
- **Total renewable generation:** 115 kW (PV + WT)
- **Fuel cell capacity:** 20.22 kW
- **Electrolyzer capacity:** 18.85 kW
- **Inverter capacity:** 49.46 kW
- **Hydrogen storage:** 74.93 kg H2 (= 2,976 kWh equivalent at 39.72 kWh/kg)

### 2.3 Component Costs (Capital, Replacement, O&M)

| Component | Capital Cost | Replacement Cost | O&M Cost | Lifetime ( |
|-----------|-------------|-----------------|----------|-------------------|--------------|
| PV | $2,000/kW | $1,800/kW | $20/year | 20 | 100% |
| WT | $3,200/kW | $3,000/kW | $32/year | 20 | 100% |
| Inverter | $800/kW | $750/kW | $7/year | 15 | 100% |
| Electrolyzer | $2,000/kW | $1,500/kW | $20/year | 20 | 100% |
| Fuel Cell | $3,000/kW | $2,500/kW | $40/year | 5 | 100% |
| Hydrogen Tank | $1,300/kg | $1,200/kg | $15/year | 20 | 100% |

> **Source:** Table I of paper, citing refs [13], [21]

### 2.4 Economic Parameters

| Parameter | Value |
|-----------|-------|
| Project lifetime (y) | 20 years |
| Interest rate (i) | 6% per year |
| CRF | Calculated as i(1+i)^y / ((1+i)^y - 1) ≈ 0.0872 |
| Currency | USD (assumed, year not explicitly stated but consistent with referenced literature) |
| Cost year | Not explicitly stated (likely 2022-2023 USD) |
| Fuel price | N/A (no diesel generator) |
| Grid electricity price | N/A (off-grid) |
| Inflation rate | Not discussed |

### 2.5 Resource Data

| Parameter | Value | Source |
|-----------|-------|--------|
| Solar irradiance | Hourly data over 1 year, max ~1000 W/m² | NASA Surface Meteorology and Solar Energy website |
| Wind speed | Hourly data over 1 year at hub height, avg varies up to ~12 m/s | NASA (extrapolated from 10m to 20m using power law with gamma=1/7) |
| Temperature | Hourly data, range ~15-35°C | NASA |
| Location coordinates | 20.8333°N, 17.0917°W | — |
| Data period | 20-year average | NASA / sodapro.com |

> Figures 3, 4, 5 show hourly profiles but no explicit annual average GHI or wind speed value is stated as a single number.

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **COE (Cost of Energy)** | **0.2674 $/kWh** | Identical to what would be LCOE; Table III labels it "CEO" (typo) but equation (9) defines it as $/kWh NPC-based |
| **NPC (Net Present Cost)** | **$825,395** | Identical for DO, GA, PSO optimal solutions |
| **Minimum NPC across algorithms** | $825,395 | Best found by all three methods |
| Payback period | Not reported | — |
| IRR / ROI | Not reported | — |
| Initial capital cost | Not explicitly stated as a single number | Can be derived from component sizes and unit costs |

> **Note:** Table III uses "CEO" header which is a typo for "COE" (equation 9 defines COE = NPC × CRF / annual energy).

### 3.2 Reliability Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **LPSP** | **0.0499 (4.99%)** | DO and GA; PSO reports 0.0496 |
| **LPSPmax (constraint)** | **0.05 (5%)** | Set as maximum allowable |
| LOLP | Not mentioned | — |
| Unmet load (kWh/year) | Not stated as a single number | Shown in Figure 9(g) as hourly variation |
| System availability | Not explicitly stated as "availability %" | Implied 95.01% (1 - LPSP) |

### 3.3 Generation Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Total annual electricity generation | Not stated as a single number | Shown in Figure 9 as hourly plots |
| PV annual generation | Not stated numerically | Figure 9(a) shows hourly PV output (0-60 kW range) |
| WT annual generation | Not stated numerically | Figure 9(b) shows hourly WT output (0-40 kW range) |
| Renewable fraction | Not explicitly stated numerically | Implied high since only deficit covered by FC |
| Excess electricity | Not stated | Goes to electrolyzer (Figure 9(c) shows EL power up to ~14 kW) |
| Hydrogen production | Not stated as annual total kg/year | Hydrogen tank mass: 74.93 kg (storage level), hourly energy in tank shown in Figure 9(f) |
| Fuel cell operation | Not stated as annual kWh | Figure 9(d) shows FC power output up to ~12 kW |
| Diesel consumption | N/A | No diesel generator |
| Grid import/export | N/A | Off-grid system |

### 3.4 Load Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Load profile | IEEE test load profile | Figure 6 |
| Peak load | ~**50 kW** | From Figure 6, maximum of hourly demand curve |
| Average load | Not stated exactly | Estimable from Figure 6 (~20-30 kW range) |
| Total annual demand | Not stated as a total kWh number | Must be < sum of renewable generation to satisfy LPSP constraint |
| Load profile type | Not explicitly stated (likely generic/standard IEEE profile) | — |

### 3.5 Optimal Configuration (if optimization was performed)

| Parameter | DO Optimal |
|-----------|-----------|
| N_PV | 60 |
| N_WT | 55 |
| P_EL | 18.85 kW |
| P_FC | 20.22 kW |
| M_HST | 74.93 kg |
| P_Inv | 49.46 kW |
| LPSP | 0.0499 |
| NPC | $825,395 |
| COE | 0.2674 $/kWh |

| Parameter | GA Optimal | PSO Optimal |
|-----------|-----------|------------|
| N_PV | 59 | 60 |
| N_WT | 55 | 54 |
| P_EL | 19.29 kW | 18.87 kW |
| P_FC | 20.33 kW | 19.73 kW |
| M_HST | 74.75 kg | 75.03 kg |
| P_Inv | 49.96 kW | 49.66 kW |
| LPSP | 0.0499 | 0.0496 |
| NPC | $825,395 | $825,395 |
| COE | 0.2674 $/kWh | 0.2674 $/kWh |

**Optimization details:**
- **Objective:** Minimize COE (= NPC × CRF / annual load) subject to LPSP ≤ 5%
- **Algorithm settings:** 20 independent runs, 100 iterations, population size of 20
- **Constraints (variable bounds):**
  - N_PV min/max: not explicitly stated (but result stays within feasible range)
  - N_WT min/max: not explicitly stated
  - SOC_tank_min/max: not explicitly stated as percentages of capacity
- **Sensitivity analysis:** Not performed as a formal sensitivity study. Only comparison of GA/PSO/DO and literature comparison (Table V).

**Statistical comparison of optimization runs (Table IV):**

| Metric | DO | GA | PSO |
|--------|----|----|----|
| Best COE | 0.2674 | 0.2674 | 0.2674 |
| Worst COE | 0.2738 | 0.3063 | 0.3412 |
| Mean COE | 0.2698 | 0.2764 | 0.2787 |
| Median COE | 0.2694 | 0.2738 | 0.2696 |
| Std Dev | 1.90E-03 | 9.50E-03 | 2.03E-02 |
| Kurtosis | 3.0514 | 5.8537 | 6.0672 |
| Skewness | 1.0523 | 1.666 | 2.0876 |

> All values in $/kWh. DO shows lowest SD, kurtosis, and skewness — described as most stable/consistent.

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

The energy management strategy is a simple rule-based logic based on comparing renewable generation to load at each hour. No battery cycling logic is described (battery is not in the component model).

**Priority order:**
1. **PV + WT serve load first** (priority #1)
2. **Electrolyzer uses surplus** (priority #2 — secondary use)
3. **Fuel Cell covers deficit** (last resort when PV+WT insufficient)

### 4.2 Power Flow Logic

**Three operational scenarios (described in Section III-C):**

**Scenario 1 — Renewable equals load (P_ren = P_load / ε_inv):**
- All demand met directly from PV/WT
- LPSP = 0
- EL and FC idle

**Scenario 2 — Renewable exceeds load (P_ren > P_load / ε_inv):**
- Demand met from PV/WT
- Surplus power routed to Electrolyzer: P_EL = (P_ren - P_load/ε_inv)
- Electrolyzer produces hydrogen via water electrolysis: P_H2_out = P_EL × ε_EL (= P_EL × 0.75)
- Hydrogen stored in tank
- LPSP = 0

**Scenario 3 — Renewable below load (P_ren < P_load / ε_inv):**
- Shortfall = P_load/ε_inv - P_ren
- Fuel Cell activated, consuming hydrogen from tank: P_FC_out = P_FC_H2 × ε_FC (= P_FC_H2 × 0.60)
- If PV+WT+FC still cannot meet load: load is curtailed → LPSP > 0 (between 0 and 1)

**Grid interaction:** None — off-grid system

### 4.3 Control Parameters

| Parameter | Value |
|-----------|-------|
| Electrolyzer efficiency (ε_EL) | 75% |
| Fuel Cell efficiency (ε_FC) | 60% |
| Inverter efficiency (ε_inv) | 95% |
| Hydrogen tank storage efficiency (ε_HT) | (implied 100%, not stated as <100%) |
| HHV of H2 | 39.72 kWh/kg |
| Time step (Δt) | 1 hour |
| LPSPmax constraint | 0.05 (5%) |
| SOC tank min/max | Not explicitly specified as numeric boundaries |
| Fuel cell operating range | Not stated (assumed 0 to 20.22 kW) |
| Electrolyzer operating range | Not stated (assumed 0 to 18.85 kW) |
| Battery SOC limits | N/A (no battery modeled) |

### 4.4 Algorithm Flow

Step-by-step energy management logic per hour:

1. **At each hour t:**
   - Calculate P_PV(t) using equation (1): P_pv_out = P_rated × (G_t/1000) × [1 + K_t × (T_amb + 0.0256×G_t - T_C,STC)]
   - Calculate P_WT(t) using equation (2) piecewise based on wind speed V(t)
2. **Total renewable:** P_ren(t) = P_PV(t) + P_WT(t)
3. **Required power at inverter input:** P_req = P_load(t) / ε_inv
4. **Decision:**
   - IF P_ren(t) ≥ P_req: deficit = 0, surplus = P_ren(t) - P_req → sent to EL
   - IF P_ren(t) < P_req: deficit = P_req - P_ren(t) → covered by FC if H2 available; else load shed
5. **Hydrogen tank update:** E_HT(t) = E_HT(t-1) + P_ren_EL(t) × Δt - P_HT_FC(t) × Δt (equation 5, with ε_HT assumed 100%)
6. **LPSP calculation:** Sum of hourly unmet load / total annual load

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

**Daytime — Peak Sun Hours (approximately 9:00–15:00):**
The PV array of 60 kW rated capacity produces power roughly in proportion to solar irradiance. At midday irradiance up to ~1000 W/m², the approximate PV output approaches 50-55 kW (after temperature derating, estimated using equation 1 with ambient temperature ~25-35°C reducing output by ~5-8%). The 55 kW of wind turbines simultaneously generate power dependent on wind conditions at 20m hub height. If combined renewable output exceeds the hourly load (which peaks around 50 kW), the surplus — potentially 20-40 kW at good conditions — feeds the electrolyzer. However, the electrolyzer is limited to **18.85 kW**, so any additional surplus is either curtailed or the inverter caps throughput at 49.46 kW to meet AC load.

**Morning Transition (06:00–09:00):** Solar ramps from zero toward several kW. If wind is low during early morning, the fuel cell compensates — it generates up to **20.22 kW** rated capacity but at 60% efficiency, meaning it consumes hydrogen at 33.7 kg equivalent per hour of full-power operation. The hydrogen tank (74.93 kg, storing up to ~2,976 kWh of chemical energy) provides hours of FC autonomy.

**Evening Peak Demand (18:00–21:00):** Solar drops to zero after sunset. Wind may or may not be available depending on local weather patterns in coastal Morocco (trade winds are relatively consistent in Southwest Morocco). If wind + any remaining solar (last hour of twilight) is insufficient, the fuel cell dispatches. Total H2 storage of 2,976 kWh chemical energy could theoretically sustain full 20.22 kW FC output (consuming ~33.7 kWh chemical per hour) for approximately **88 hours** under maximum discharge — though actual usable amount is lower because the SOC minimum constraint is not stated.

**Night (22:00–05:00):** Wind turbines carry the load. If wind insufficient, fuel cell runs. The system is designed to tolerate up to 5% annual unmet load, translating to approximately **438 hours/year of potential shedding at 1 kW deficit** (or fewer hours at larger deficits), ensuring reliability without excessive oversizing.

**Seasonal Variations:** Southwest Morocco, being coastal, experiences mild temperatures (15-35°C range per Figure 4) which is favorable for PV efficiency (lower temperatures = higher PV output). Solar irradiance peaks in summer months, while wind patterns vary. The hourly NASA data captures these variations; Figure 3 shows irradiance fluctuating between ~200-1000 W/m² across the year.

Using the actual component sizes: With **60 PV units (60 kW)** and **55 WT units (55 kW)** generating electricity, and a daily demand profile centered around the IEEE test case peaking at 50 kW, estimated daily load is roughly **480-720 kWh/day** (assuming 20-30 kW average load × 24h). Annual load is therefore approximately **175,000–263,000 kWh/year**.

The optimal NPC of $825,395 with CRF ≈ 0.0872 yields annualized cost of ~$71,974/year. If COE = $0.2674/kWh, this implies annual energy served ≈ **269,000 kWh/year** ($71,974 / $0.2674). This is consistent with a ~740 kWh/day average load (~30.8 kW average). Given peak of 50 kW, the load factor is approximately 0.62 — reasonable for rural community demand.

### 5.2 System Behavior Analysis

**Why this specific configuration is optimal:**
The optimization found that a 115 kW total renewable capacity (60+55) paired with 18.85 kW electrolyzer, 20.22 kW fuel cell, and 74.93 kg hydrogen storage minimizes COE at $0.2674/kWh while keeping LPSP just under the 5% constraint (4.99%). The system sits at the boundary of the reliability constraint — any lower capacity would violate LPSP, and any higher would increase NPC disproportionately.

The remarkable finding that GA, PSO, and DO converge to essentially the same NPC ($825,395) with nearly identical COE suggests the problem has a clear global minimum and that traditional metaheuristics find it reliably — the "superiority" of DO claimed in the paper rests on **convergence speed and statistical robustness** (lower SD across 20 runs) rather than discovering a better objective value.

The authors' comparison with literature (Table V) shows their COE of $0.2674/kWh is competitive: lower than most PV/WT/FC systems in other regions (except one diesel-heavy system at $0.259/kWh), suggesting Morocco's solar and wind resources are excellent.

**Trade-offs identified:**
- Higher PV/WT capacity → more excess energy wasted (electrolyzer capped at 18.85 kW)
- Higher electrolyzer → more H2 storage needed → higher NPC
- Larger hydrogen tank → more stored energy for deficits → higher capital cost
- Lower LPSP constraint → more conservative sizing → higher COE
- The fuel cell's 5-year lifetime (shortest) means **4 replacements** over 20 years — a major economic driver (replacement cost $2,500/kW × 20.22 kW × 4 times)

**Edge cases:**
- Extended cloudy/low-wind periods: the system relies on H2 reserves. 74.93 kg ≈ 2,976 kWh chemical energy; at 30 kW average deficit, this provides ~100 hours of FC supply at reduced efficiency. For longer events, LPSP accumulates.
- Load growth: not studied; would require re-optimization with higher demand
- FC degradation after each 5-year replacement cycle: not modeled; assumes nominal performance after replacement

### 5.3 Critical Evaluation

**Reasonableness of assumptions:**
- The assumption of **1-hour time steps** for all inputs (weather, load) is standard but smooths sub-hourly variability that could affect battery cycling (not that batteries are modeled).
- Using **NASA satellite data** rather than ground measurements is common but may have 5-10% measurement uncertainty.
- **No battery modeling** is a notable gap — the introduction discusses batteries as short-term buffers, but the actual optimization eliminates them, choosing only hydrogen for storage. This simplifies the model but may underestimate short-term storage costs.
- The **5% LPSP constraint** translates to ~438 hours/year where the system cannot fully serve load. For a rural community, this means potential daily power interruptions. The paper does not discuss this practical implication.
- Component availability is assumed 100% — no maintenance downtime modeled.

**Limitations:**
- Single location only (Lagouira); results not generalized
- No component degradation over time or cycling degradation of FC
- No demand-side management or load shifting considered
- No sensitivity analysis on interest rate, fuel prices, or component costs
- The cost year is not stated, making the $0.2674/kWh hard to compare directly with other studies
- IEEE standard load profile is generic, not reflecting actual Lagouira rural community demand patterns
- No export of excess energy (off-grid) — all excess must go to electrolyzer or be curtailed

**What would change with different parameters:**
- Higher interest rate: increases CRF, increases NPC and COE; would shift optimal configuration toward lower capital (fewer PV/WT)
- Lower solar irradiance region: requires more PV capacity, higher COE (as shown in Table V — Iran at $0.4477/kWh)
- Diesel inclusion: would likely lower COE but increase emissions — not considered here
- Battery inclusion: could complement hydrogen storage for short-term cycling, potentially allowing smaller electrolyzer/FC

### 5.4 Derived/Inferred Values

| Derived Value | Calculation | Result |
|---------------|-------------|--------|
| **Annual energy served** | Annualized cost / COE = ($825,395 × 0.0872) / $0.2674 | ≈ **269,100 kWh/year** |
| **Average daily load** | 269,100 / 365 | ≈ **737 kWh/day** |
| **Average load** | 737 / 24 | ≈ **30.7 kW** |
| **Load factor** | Avg / Peak = 30.7 / 50 | ≈ **0.61 (61%)** |
| **H2 storage energy** | 74.93 kg × 39.72 kWh/kg | ≈ **2,976 kWh (chemical)** |
| **FC hours autonomy (full Output)** | (2,976 / 60% efficiency) / 20.22 kW usable = 2976×0.6 / 20.22 |
| **CRF** | 0.06×(1.06)^20 / ((1.06)^20 - 1) | ≈ **0.0872** |
| **Annualized NPC** | $825,395 × 0.0872 | ≈ **$71,974/year** |
| **FC replacements needed** | 20 years / 5 year lifetime - 1 | **4 replacements** |
| **FC lifetime replacement cost** | 20.22 kW × $2,500/kW × 4 | ≈ **$202,200** (NPV of replacements) |
| **Total PV capacity cost** | 60 kW × $2,000/kW | **$120,000** |
| **Total WT capacity cost** | 55 kW × $3,200/kW | **$176,000** |
| **Electrolyzer cost** | 18.85 kW × $2,000/kW | **$37,700** |
| **Fuel Cell initial** | 20.22 kW × $3,000/kW | **$60,660** |
| **H2 tank initial** | 74.93 kg × $1,300/kg | **$97,409** |
| **Inverter initial** | 49.46 kW × $800/kW | **$39,568** |
| **ROW sum of initial capital** | Sum of above | **≈ $531,337** |
| **ROW sum as % of NPC** | $531,337 / $825,395 | ≈ **64.4%** |
| **PV capacity factor (estimated)** | Annual_PV / (60 kW × 8760 h) — need PV annual output |

> **Note on capacity factors:** Paper does not give annual PV/WT generation totals. From Figure 9, average PV output estimated at 8-12 kW (depends on sun hours ~5-6 effective hours/day), giving PV capacity factor ≈ **13-20%**. Average WT output estimated 10-15 kW, giving WT capacity factor ≈ **18-27%**. These are rough estimates from visual inspection of Figure 9.

| Derived Value | Estimate |
|---------------|----------|
| PV capacity factor | ~15-18% |
| WT capacity factor | ~20-25% |
| Annual PV generation | ~79,000–95,000 kWh/year |
| Annual WT generation | ~96,000–120,000 kWh/year |
| Annual FC generation | ~25,000–40,000 kWh/year |
| Annual unmet load | ~5% × 269,100 ≈ **13,455 kWh/year** |

### 5.5 Key Takeaways

1. **Dandelion Optimizer is statistically more robust** than GA and PSO for this problem (lower variance across 20 runs), though all three converge to the same optimal NPC of $825,395 and COE of $0.2674/kWh. The advantage lies in reliability of convergence, not solution quality.

2. **Morocco's renewable resources enable very low COE ($0.2674/kWh)** — among the lowest reported globally for PV/WT/FC systems, competitive with diesel-hybrid systems in Nigeria. This makes hydrogen-based off-grid systems economically viable for rural electrification.

3. **High renewable penetration is feasible with hydrogen storage** — the system meets 95% of demand using only PV and WT, with hydrogen storage (74.93 kg) and fuel cell (20.22 kW) as backup. No diesel or batteries required.

4. **Fuel cell lifecycle cost is significant** — with a 5-year lifetime requiring 4 replacements over the 20-year project, FC replacement costs are a major contributor to the $825,395 NPC. Extending FC lifetime through degradation-aware dispatch would improve economics.

5. **The optimal configuration sits at the reliability constraint boundary** (LPSP = 4.99% vs. max 5%), meaning the optimizer is exploiting the full allowable risk margin to minimize cost — a classic economic-reliability trade-off that leaves no "safety margin" beyond the constraint.

---
