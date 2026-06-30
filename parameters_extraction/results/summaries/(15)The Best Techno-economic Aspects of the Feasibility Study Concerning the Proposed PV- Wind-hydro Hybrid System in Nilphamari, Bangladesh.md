# Paper Summary: The Best Techno-economic Aspects of the Feasibility Study Concerning the Proposed PV-Wind-hydro Hybrid System in Nilphamari, Bangladesh

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** The Best Techno-economic Aspects of the Feasibility Study Concerning the Proposed PV-Wind-hydro Hybrid System in Nilphamari, Bangladesh
- **Authors:** Md. Sariful Islam, Nuhim Ahamed Noman, Md. Ahsan Habib
- **Journal/Conference name:** International Journal of Education and Management Engineering (IJEME)
- **Year of publication:** 2022
- **DOI:** 10.5815/ijeme.2022.05.04
- **Study location:** Nilphamari, Bangladesh (Latitude: 25°56.2' N, Longitude: 88°50.4' E)
- **System type:** Grid-connected PV-Wind-Hydro-Diesel hybrid system with electrolyzer, reformer, and hydrogen storage
- **Study type:** Simulation-based (no experimental component)
- **Software/tools used:** HOMER Pro software
- **Optimization method:** HOMER's built-in optimization — simulates all possible system configurations, discards infeasible ones, ranks feasible combinations by total NPC. Four parameters considered: COE, RF (renewable fraction), NPC, and CO2 emissions.

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Rated Capacity | Number of Units | Key Specifications |
|-----------|---------------|-----------------|-------------------|
| PV Array (Peimar Inc.) | 254 kW | — | Specific yield: 1,913 kWh/kW; PV penetration: 51.2% |
| Wind Turbine | 2.00 kW | 1 | Lifetime: 25.0 years; Hours of operation: 5,864 hrs/yr |
| Diesel Generator | 570 kW | 1 | Fuel: Diesel; Fuel price: $1.00/L; Marginal generation cost: $0.248/kWh; Fixed generation cost: $58.0/hr |
| Hydro Generator | 92.0 kW | 1 | Capacity factor: 128%; Operation hours: 8,760 hrs/yr; Levelized cost: $0.00378/kWh |
| Electrolyzer | 100 kW | 1 | Capacity factor: 12.8%; Specific consumption: 46.4 kWh/kg; Mean output: 0.277 kg/hr |
| Reformer | 3.00 kg/hr | 1 | Capacity factor: 0.0709%; Hours of operation: 3,317 hr/yr |
| Hydrogen Tank | 1.00 kg capacity | 1 | Energy storage capacity: 33.3 kWh; Tank autonomy: 0.307 hr |
| Battery (Surrette 4 KS 25P) | 3,305 kWh (rated) | 438 batteries | Expected life: 20.0 yr; Autonomy: 18.3 hr |
| System Converter | 433 kW (inverter + rectifier) | 1 | Inverter capacity factor: 12.0%; Rectifier capacity factor: 3.84% |

### 2.2 Total System Capacity

- **Total generation capacity:** 254 kW (PV) + 2 kW (Wind) + 570 kW (Diesel) + 92 kW (Hydro) = **918 kW**
- **Total storage capacity:** 3,305 kWh (battery) + 33.3 kWh (hydrogen tank) = **3,338.3 kWh**
- **Total conversion capacity:** 433 kW (converter/inverter) + 100 kW (electrolyzer) = **533 kW**

### 2.3 Component Costs (Capital, Replacement, O&M)

The paper does NOT provide explicit capital, replacement, or O&M costs per component. Costs are only reported as aggregated results (NPC, COE, operating cost). The only cost-related inputs explicitly stated are:
- Diesel fuel price: **$1.00/L**
- Fixed generation cost (diesel): **$58.0/hr**
- Electrolyzer operating expenses: **$1,000/yr**

> Not reported in this paper: per-component capital costs, replacement costs, O&M costs per component.

### 2.4 Economic Parameters

| Parameter | Value |
|-----------|-------|
| Project lifetime | Not explicitly stated (payback is 24.20 years, suggesting ~25-year project life) |
| Discount/interest rate | Not explicitly stated (HOMER calculates "actual discount rate") |
| Return on investment (ROI) | 86.1% |
| Internal rate of return (IRR) | 10.3% |
| Simple payback | 24.20 years |
| Present worth | $37,181 |
| Annual worth | $2,876/yr |
| Fuel price (diesel) | $1.00/L |
| Grid electricity price | Not reported |
| Currency and cost year | USD (year not explicitly stated, assumed 2022) |

### 2.5 Resource Data

| Resource | Value | Source |
|----------|-------|--------|
| Solar irradiance (annual average) | **5.85 kWh/m²/day** | NASA via HOMER |
| Maximum solar radiation | 6.080 kWh/m²/day (October) | NASA |
| Minimum solar radiation | 5.680 kWh/m²/day (May) | NASA |
| Wind speed (annual average) | **3.91 m/s** | NASA (USA) |
| Maximum wind speed | 4.980 m/s (June) | NASA |
| Minimum wind speed | 2.800 m/s (December) | NASA |
| Hydro stream flow (annual average) | **899,752.35 L/s** (Teesta River) | BWDB (Bangladesh Water Development Board), Jan 2016 – Dec 2020 |
| Maximum stream flow | 2,512,522.00 L/s (July) | BWDB |
| Minimum stream flow | 63,277.170 L/s (February) | BWDB |

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

| Metric | Value |
|--------|-------|
| LCOE (minimum from optimization) | **$0.224/kWh** |
| COE (proposed system) | **$0.241/kWh** |
| NPC | **$2,961,790.00** |
| Operating cost (annual) | **$16,156.16/yr** |
| Payback period | **24.20 years** |
| ROI | **86.1%** |
| IRR | **10.3%** |
| Initial capital cost | Not explicitly stated |

### 3.2 Reliability Metrics

| Metric | Value |
|--------|-------|
| LPSP (Loss of Power Supply Probability) | Not explicitly reported |
| Unmet load | Not explicitly reported |
| System availability | Not explicitly reported |

> Note: The paper does not report LPSP or unmet load values. The system is grid-connected, so grid import likely covers any shortfall.

### 3.3 Generation Metrics

| Metric | Value |
|--------|-------|
| Total annual electricity generation | Not explicitly stated as a single total |
| PV annual production | **486,337 kWh/yr** |
| Wind annual production | **1,304 kWh/yr** |
| Diesel generator annual production | **4,231 kWh/yr** |
| Hydro annual production | **1,027,199 kWh/yr** |
| Renewable fraction (energy-based) | **99.7%** of generation; **153%** of load |
| Renewable fraction (capacity-based) | **38.9%** nominal; **34.2%** usable |
| Excess electricity | Not explicitly stated |
| Battery annual throughput | **158,052 kWh/yr** |
| Battery losses | **35,341 kWh/yr** |
| Hydrogen production (electrolyzer) | **2,422 kg/yr** |
| Hydrogen production (reformer) | **1,863 kg/yr** |
| Total hydrogen production | **4,285 kg/yr** (2,422 + 1,863) |
| Hydrogen consumption (load) | **11 kg/day** = **4,015 kg/yr** (derived) |
| Diesel consumption | **1,289 L/yr** |
| Grid electricity imported/exported | Not explicitly stated |

### 3.4 Load Metrics

| Metric | Value |
|--------|-------|
| Total annual load demand | **949,230 kWh/yr** (derived: 2,602 kWh/day × 365) |
| Average daily load | **2,602 kWh/day** |
| Peak load | **518 kW** |
| Average load | Not explicitly stated (derived: ~108.2 kW from annual/days) |
| Maximum monthly average load | 398.37 kW (August) |
| Minimum monthly average load | 266.73 kW (January) |
| Load profile type | Not explicitly stated (community/residential mix for Nilphamari region) |
| Hydrogen load | **11 kg/day** (peak: 2.393 kg/hr) |

### 3.5 Optimal Configuration (if optimization was performed)

- **Winning configuration (as stated in conclusion):** 254 kW solar PV, 92 kW hydropower, 570 kW diesel generator, 438 batteries, 433 kW converter, 3 kW reformer, 100 kW electrolyzer
- **Objective function:** Minimize NPC (HOMER ranks by total NPC); four parameters considered: COE, RF, NPC, CO2 emissions
- **Constraints applied:** Not explicitly stated (HOMER discards infeasible configurations that cannot meet load)
- **Sensitivity analysis variables:** Diesel price at three levels: **$0.90/L, $1.00/L, $1.08/L**
  - COE at $0.90/L: $0.224/kWh
  - COE at $1.00/L: $0.226/kWh
  - COE at $1.08/L: $0.228/kWh
  - Renewable fraction for all three: **99.6%**

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

The paper does NOT explicitly describe the dispatch strategy or priority order of generation sources. HOMER Pro uses its default optimization logic:
- HOMER simulates every possible combination of components
- For each configuration, it performs hourly time-step simulation over one year
- It discards configurations that cannot meet the load constraints
- It ranks feasible configurations by total NPC

> Not explicitly reported: priority order of generation sources, decision logic for component on/off cycling.

### 4.2 Power Flow Logic

The paper does NOT explicitly describe:
- How excess renewable energy is handled (though the presence of electrolyzer and battery suggests excess goes to hydrogen production and battery charging)
- How deficit is handled (grid-connected, so grid import likely covers shortfall)
- Battery charging/discharging logic and SOC limits (not stated)
- Hydrogen production and consumption logic (electrolyzer produces H2 from excess electricity; reformer produces H2 from diesel fuel)
- Diesel generator start/stop conditions (only 29 hours/yr of operation reported, suggesting it runs only during extreme deficit)

### 4.3 Control Parameters

| Parameter | Value |
|-----------|-------|
| Battery SOC minimum | Not reported |
| Battery SOC maximum | Not reported |
| Battery autonomy | 18.3 hours |
| Diesel generator minimum load ratio | Not reported |
| Diesel generator operational life | 517 years (likely a HOMER default or data entry anomaly) |
| Diesel generator hours of operation | 29.0 hrs/yr |
| Electrolyzer capacity factor | 12.8% |
| Reformer capacity factor | 0.0709% |
| Inverter capacity factor | 12.0% |
| Rectifier capacity factor | 3.84% |
| Converter hours of operation | 3,521 hrs/yr (inverter); 4,778 hrs/yr (rectifier) |

### 4.4 Algorithm Flow

The paper does NOT provide a step-by-step energy management algorithm, decision tree, or power balance equations. The methodology relies entirely on HOMER Pro's internal simulation engine.

> Note: This is a HOMER-based feasibility study. The authors input component sizes, costs, and resource data; HOMER handles the dispatch optimization internally. The paper reports HOMER's outputs but does not describe the underlying control logic in detail.

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

This system is designed for Nilphamari, Bangladesh, a region that currently relies on grid electricity. The proposed hybrid system combines four generation sources — solar PV (254 kW), micro-hydro (92 kW on the Teesta River), a single small wind turbine (2 kW), and a diesel generator (570 kW) — along with substantial battery storage (3,305 kWh across 438 Surrette batteries), a 100 kW electrolyzer, a 3 kg/hr reformer, and a 1 kg hydrogen tank.

**Morning (6:00–9:00):** Solar radiation begins around 6 AM. Hydro generation runs continuously at approximately 92 kW (base load). The battery, which discharged overnight, begins receiving charge as PV output ramps up. The electrolyzer may start operating if excess power is available after serving the load and charging batteries.

**Midday (10:00–14:00):** Peak solar production occurs. PV generates up to 254 kW (rated), with maximum instantaneous output reaching 261 kW. Combined with hydro (~92 kW), total renewable generation reaches ~346 kW. The daytime load averages around 108 kW (annual average), so substantial excess is available. This excess charges the battery bank and powers the electrolyzer, which produces hydrogen at up to 2.15 kg/hr. The electrolyzer operates at 12.8% capacity factor, meaning it runs at full power only ~1,123 hours per year, suggesting it operates selectively during high-resource periods.

**Evening (17:00–20:00):** Solar output drops to zero by approximately 6–7 PM. Load typically peaks in the evening. Hydro continues generating ~92 kW. The battery bank (3,305 kWh, capable of powering the average load for 18.3 hours) discharges to meet the deficit. The diesel generator (570 kW) remains on standby, operating only 29 hours per year — it fires only during extended periods of low renewable output combined with high load and low battery SOC.

**Night (21:00–5:00):** Hydro provides base load (~92 kW). Wind contributes minimally (2 kW rated, producing only 1,304 kWh/yr — a capacity factor of ~7.4%). The battery covers the remaining deficit. Given the battery autonomy of 18.3 hours, the system can operate through the night without diesel in most conditions.

**Seasonal variations:** Hydro generation peaks in July (monsoon, stream flow 2,512,522 L/s) and drops in February (63,277 L/s). Solar peaks in October (6.080 kWh/m²/day) and dips slightly in May (5.680 kWh/m²/day). Wind peaks in June (4.98 m/s) and drops in December (2.80 m/s). The hydro resource dominates annual generation at 1,027,199 kWh/yr — more than double PV's 486,337 kWh/yr. The diesel generator's minimal operation (4,231 kWh/yr, 29 hours) confirms that renewables + storage meet virtually all load.

### 5.2 System Behavior Analysis

**Why this configuration was chosen as optimal:** HOMER evaluated all possible combinations and selected the one with the lowest NPC that meets the load. The dominance of hydro (1,027,199 kWh/yr from a 92 kW unit — capacity factor 128%, meaning the turbine can exceed rated capacity during high-flow periods) makes it the backbone. PV provides daytime surplus for electrolyzer operation. The diesel generator serves only as backup (running just 29 hours/year). The 438 batteries provide 18.3 hours of autonomy, ensuring reliability during low-resource periods.

**Relationship between renewable penetration and storage sizing:** The system achieves 99.7% renewable penetration (energy-based) with 3,305 kWh of battery storage. The battery throughput of 158,052 kWh/yr means each kWh of battery capacity cycles ~47.8 times per year (0.13 cycles/day), indicating relatively shallow daily cycling — the battery primarily shifts solar daytime surplus to evening/night rather than deep cycling.

**Dispatch strategy implications:** The diesel generator's 29 hours/yr operation and 1,289 L/yr fuel consumption means it runs less than 0.3% of the year. This minimizes fuel costs and CO2 emissions (3,373 kg/yr total). The electrolyzer operates at 12.8% capacity factor (6,148 hrs/yr), consuming 112,413 kWh/yr to produce 2,422 kg/yr of hydrogen. The reformer produces an additional 1,863 kg/yr from diesel, but at a very low capacity factor (0.0709%, 3,317 hrs/yr).

**Trade-offs identified by authors:** The paper notes that the minimum COE ($0.224/kWh at $0.90/L diesel) is close to the proposed system's COE ($0.241/kWh at $1.00/L diesel). The sensitivity analysis shows COE increases only slightly with diesel price, confirming the system's resilience to fuel price volatility. The authors emphasize that the system emits the least CO2 (3,373 kg/yr) among configurations considered.

**Edge cases:** During extended monsoon cloud cover, hydro generation actually increases (peak flow in July), compensating for reduced PV. During the dry season (February minimum flow), hydro output drops but PV and battery cover the gap. The diesel generator handles extreme cases (prolonged low wind + low solar + low hydro + high load).

### 5.3 Critical Evaluation

**Reasonableness of assumptions:**
- The hydro capacity factor of 128% is unusual — it suggests the turbine can operate above rated capacity during high-flow periods, which is plausible for certain turbine types but worth noting.
- The diesel generator operational life of 517 years is clearly a HOMER default or data entry artifact, not a realistic value.
- The wind turbine (2 kW) contributes negligibly (1,304 kWh/yr out of ~1.52 million kWh total generation). Its inclusion appears token — the annual average wind speed of 3.91 m/s is below the typical cut-in threshold for most commercial turbines (3.5–4 m/s).
- The hydrogen tank capacity of only 1 kg (33.3 kWh) is very small relative to daily hydrogen production (~11.7 kg/day combined) and consumption (11 kg/day), suggesting hydrogen is consumed nearly as fast as it's produced.

**Limitations of this study:**
- No explicit component costs are provided, making it impossible to verify the NPC calculation.
- The paper does not report LPSP, unmet load, or grid import/export quantities.
- The system is described as grid-connected but grid interaction details are absent.
- The electrolyzer and reformer serve a hydrogen load (11 kg/day) but the end use of this hydrogen is not specified.
- No comparison with a baseline (grid-only or diesel-only) scenario is provided.
- The "proposed" configuration selected by the authors does not match the minimum COE configuration ($0.224 vs $0.241/kWh), and the rationale for selecting a higher-COE configuration is not clearly explained beyond CO2 minimization.

**Generalizability:** The approach (HOMER-based techno-economic analysis) is widely applicable. The specific results are location-dependent (Teesta River flow data, Nilphamari solar/wind resources). The finding that hydro-dominated hybrids achieve very low COE ($0.224–$0.241/kWh) with 99.6% renewable fraction is relevant for similar riverine regions in South Asia.

**What would change if parameters differed:**
- If diesel price rose above $1.08/L, the economic case for any diesel inclusion weakens further.
- If the Teesta River flow decreased significantly (climate change, upstream diversion), the system would lose its primary generation source, requiring much more PV + battery + diesel.
- If battery costs decreased, the optimal battery size would increase, potentially eliminating even the 29 hours of diesel operation.

### 5.4 Derived/Inferred Values

| Derived Value | Calculation | Result |
|---------------|-------------|--------|
| Average daily generation (total) | PV (486,337) + Hydro (1,027,199) + Wind (1,304) + Diesel (4,231) = 1,519,071 kWh/yr ÷ 365 | **4,162 kWh/day** |
| Average daily generation per source | PV: 486,337÷365; Hydro: 1,027,199÷365; Wind: 1,304÷365; Diesel: 4,231÷365 | PV: 1,332 kWh/day; Hydro: 2,814 kWh/day; Wind: 3.6 kWh/day; Diesel: 11.6 kWh/day |
| Average daily unmet load | Not reported | Cannot derive |
| PV capacity factor | 486,337 ÷ (254 × 8,760) × 100 | **21.8%** |
| Hydro capacity factor | Stated as 128% (or: 1,027,199 ÷ (92 × 8,760) × 100 = 127.6%) | **128%** |
| Wind capacity factor | 1,304 ÷ (2 × 8,760) × 100 | **7.44%** |
| Diesel capacity factor | 4,231 ÷ (570 × 8,760) × 100 | **0.0847%** |
| Battery storage autonomy | Stated: 18.3 hours | 18.3 hours of average load |
| Battery cycles per year | 158,052 ÷ 3,305 | **47.8 cycles/yr** |
| Renewable fraction (generation) | (486,337 + 1,027,199 + 1,304) ÷ 1,519,071 × 100 | **99.7%** |
| Total annual generation | 486,337 + 1,304 + 4,231 + 1,027,199 | **1,519,071 kWh/yr** |
| Total annual load (electric) | 2,602 × 365 | **949,730 kWh/yr** |
| Excess electricity (implied) | 1,519,071 − 949,730 | **569,341 kWh/yr** (goes to electrolyzer, battery charging, losses, grid export) |
| Electrolyzer energy consumption | 112,413 kWh/yr (stated) | Confirms ~19.7% of excess goes to electrolyzer |
| Hydrogen load annual | 11 kg/day × 365 | **4,015 kg/yr** |
| Total hydrogen production | 2,422 + 1,863 | **4,285 kg/yr** |
| Hydrogen surplus | 4,285 − 4,015 | **270 kg/yr** (stored or exported) |
| Average load | 949,730 ÷ 8,760 | **108.4 kW** |
| CO2 per kWh generated | 3,373 ÷ 1,519,071 × 1,000 | **2.22 g/kWh** |
| Cost per kg of hydrogen (electrolyzer) | (112,413 × $0.241) ÷ 2,422 | **$11.18/kg** (using system COE as proxy) |

### 5.5 Key Takeaways

1. **Hydro dominates generation:** The 92 kW micro-hydro unit on the Teesta River produces 1,027,199 kWh/yr (67.6% of total generation) at a remarkably low levelized cost of $0.00378/kWh, making it the economic backbone of the system.

2. **Near-complete renewable penetration:** The system achieves 99.7% renewable electricity generation, with the diesel generator running only 29 hours per year (0.3% of the time) and consuming only 1,289 L of diesel annually.

3. **Competitive COE:** At $0.224–$0.241/kWh, the system is competitive with grid electricity in Bangladesh, while providing energy independence and dramatically lower emissions.

4. **Minimal wind contribution:** The 2 kW wind turbine contributes only 1,304 kWh/yr (0.09% of generation) due to the low average wind speed (3.91 m/s). This component is economically marginal.

5. **Hydrogen co-production:** The system produces ~4,285 kg/yr of hydrogen (via electrolyzer and reformer) against a load of ~4,015 kg/yr, demonstrating integrated electricity-hydrogen co-production, though the hydrogen end-use is not specified in the paper.

---

*Document generated from 14-page paper. All numerical values in Sections 1–4 are directly traceable to the source paper. Section 5 contains derived calculations and analytical commentary grounded in the paper's data.*
