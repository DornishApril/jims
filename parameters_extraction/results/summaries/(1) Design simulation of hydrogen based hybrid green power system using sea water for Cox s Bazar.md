# Design & Simulation of Hydrogen Based Hybrid Green Power System Using Sea Water for Cox's Bazar

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

| Field | Value |
|-------|-------|
| **Full Title** | Design & simulation of hydrogen based hybrid green power system using sea water for Cox's Bazar |
| **Authors** | Kazi Meharajul Kabir and Mahmud Abdul Matin Bhuiyan |
| **Journal** | Cogent Engineering (Taylor & Francis Group / Cogent OA) |
| **Year** | 2017 |
| **DOI** | 10.1080/23311916.2017.1347029 |
| **Study Location** | Diabatic beach, Kolatoli, Cox's Bazar, Bangladesh (22°26' N, 91°57' E) |
| **System Type** | Off-grid PV-Wind-PEM Electrolyzer-Hydrogen Tank-Gas Turbine Generator hybrid system (sea water electrolysis for hydrogen production) |
| **Study Type** | Simulation-based (HOMER Pro) |
| **Software** | HOMER Pro (HOMER Energy, 2016) |
| **Optimization Method** | HOMER Pro simulation-based optimization (no metaheuristic; HOMER searches component sizing combinations) |
| **Affiliation** | Institute of Energy Technology (IET) and Department of EEE, Chittagong University of Engineering and Technology (CUET), Chittagong 4349, Bangladesh |

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT

### 2.1 Component List and Capacities

| Component | Model | Capacity | Units | Key Specs |
|-----------|-------|----------|-------|-----------|
| **PV Array** | Generic flat plate PV | 2.2 MW (2,200 kW) | 1 system | Derating factor: 80%, No tracking, Slope: 23.00°, Ground reflectance: 20% |
| **Wind Turbine Generator** | XL-500 | 500 kW each | 9 units | Rotor diameter: 22 m, Hub height: 35 m, Cut-in: 3 m/s, Cut-out: 25 m/s, Start-up: 2.5 m/s |
| **PEM Electrolyzer** | Not specified (generic PEM) | 3 MW (3,000 kW) | 1 unit | Efficiency: 85%, Lifetime: 15 yr |
| **Hydrogen Storage Tank** | Not specified | 50,000 kg | 1 unit | — |
| **Gas Turbine Generator** | 3 MW Genset | 3,000 kW | 1 unit | Fuel: Hydrogen, Lower heating value: 120 MJ/kg, Lifetime: 25,000 hrs |

*Note: The paper Table 1 lists electrolyzer as 3 MW but text in Section 5.1 states "300 kW" — this appears to be a typo. All subsequent data (Table 10: total input power 6,499,506 kWh/yr, mean 741.95 kW) are consistent with 3 MW rated capacity.*

### 2.2 Total System Capacity

| Category | Total |
|----------|-------|
| **Total Generation Capacity** | 2.2 MW (PV) + 4.5 MW (Wind) + 3 MW (Gas Turbine) = **9.7 MW** |
| **Total Conversion Capacity** | 3 MW (PEM Electrolyzer) |
| **Total Storage Capacity** | 50,000 kg hydrogen |
| **Peak Load Demand** | 9 MW (5–10 PM daily) |

### 2.3 Component Costs (Capital, Replacement, O&M)

| Component | Initial Capital | Replacement Cost |
|-----------|----------------|-----------------|
| PV (2.2 MW) | $1,760,000 | $509,658 |
| Wind Turbine (9 × 500 kW) | $1,800,000 | $625,489 |
| PEM Electrolyzer (3 MW) | $1,800,000 | $1,010,851 |
| Hydrogen Storage Tank | $5,000 | $915 |
| Gas Turbine Generator (3 MW) | $750,000 | $354,247 |
| **Total System** | **$6,115,000** | **$2,501,160** |

*Note: O&M costs are included in the annual costs in Table 15 but not broken down separately per component. PV LCOE: $0.039/kWh. Wind LCOE: $0.040/kWh.*

### 2.4 Economic Parameters

| Parameter | Value |
|-----------|-------|
| **Project Lifetime** | 25 years |
| **Overall Cost of Energy (COE)** | **$0.178/kWh** |
| **Annual Cost** | $388,195 |
| **Total System Cost (lifetime)** | $9,240,844 |
| **Discount/Interest Rate** | Not explicitly stated |
| **Inflation Rate** | Not stated |
| **Fuel Price** | N/A (hydrogen is produced on-site from renewable energy) |
| **Currency** | USD (assumed 2017) |

### 2.5 Resource Data

| Resource | Annual Average | Data Source |
|----------|---------------|-------------|
| **Solar GHI** | 4.77 kWh/m²/day | NASA Surface Meteorology and SolarWind Speed** | 3.55 m/s (at 20 m hub height) | NASA Surface Meteorology and Solar Energy |
| **Monthly Solar Range** | 3.81 kWh/m²/day (July) to 6.09 kWh/m²/day (April) | NASA |
| **Monthly Wind Range** | 2.70 m/s (October) to 4.87 m/s (June) | NASA |
| **Clearness Index** | Annual avg: 0.526 | NASA |

**Monthly Solar Radiation and Wind Speed (Cox's Bazar):**

| Month | Solar GHI (kWh/m²/day) | Wind Speed (m/s) |
|-------|------------------------|------------------|
| January | 4.750 | 2.90 |
| February | 5.330 | 3.13 |
| March | 5.930 | 3.40 |
| April | 6.090 | 3.68 |
| May | 5.520 | 3.75 |
| June | 4.110 | 4.87 |
| July | 3.810 | 4.83 |
| August | 4.030 | 4.32 |
| September | 4.150 | 3.35 |
| October | 4.530 | 2.70 |
| November | 4.480 | 2.86 |
| December | 4.560 | 2.82 |

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT

### 3.1 Cost Metrics

| Metric | Value |
|--------|-------|
| **Initial Capital Cost** | $6,115,000 |
| **Overall Cost of Energy (COE)** | $0.178/kWh |
| **PV Levelized Cost** | $0.039/kWh |
| **Wind Levelized Cost** | $0.040/kWh |
| **Total Lifetime Cost** | $9,240,844 |
| **Annualized Cost** | $388,195/year |
| **Payback Period** | Not reported |

### 3.2 Reliability Metrics

| Metric | Value |
|--------|-------|
| **LPSP** | Not explicitly reported (system appears to meet load: GT produces 3,281,028 kWh/yr vs load of 3,285,000 kWh/yr — near-perfect match) |
| **Unmet Load** | ~3,972 kWh/yr (implied: 3,285,000 − 3,281,028) |
| **System Availability** | Not reported |

### 3.3 Generation Metrics

**Total Annual Electricity Production: 9,969,159 kWh/yr**

| Component | Annual Production (kWh/yr) | Fraction (%) | Type |
|-----------|---------------------------|-------------|------|
| PV Array | 3,263,389 | 33% | DC |
| Wind Turbine | 3,263,389→3,424,742 | 34% | DC |
| Gas Turbine Generator | 3,281,028 | 33% | AC |
| **Total** | **9,969,159** | **100%** | — |

| Parameter | Value |
|-----------|-------|
| **PV Mean Output** | 373 kW (8,940.79 kWh/day) |
| **Wind Mean Output** | 391 kW |
| **Total H₂ Production** | 1,400,659.79 kg/yr (Table 11) / 140,060 kg/yr (Table 14 — **DISCREPANCY noted**) |
| **H₂ Consumption by GT** | 137,803 L/yr (or kg/yr — units ambiguous) |
| **Excess Hydrogen** | 2,257 kg/yr |
| **Electrolyzer Input Power** | 6,499,506.36 kWh/yr |
| **Electrolyzer Mean Power** | 741.95 kW |
| **Specific Fuel Consumption (Electrolyzer)** | 46.41 kWh/kg |
| **GT Specific Fuel Consumption** | 0.04 L/kWh |
| **GT Mean Electrical Efficiency** | 71% |
| **GT Fuel Energy Input** | 4,593,439 kWh/yr |
| **Renewable Fraction** | ~67% (PV + Wind generate ~6,688,131 kWh of the ~9,969,159 kWh total) |

**DISCREPANCY:** Table 11 reports H₂ production as 1,400,659.79 kg/yr. Table 14 reports H₂ production as 140,060 kg/yr (exactly �10). The Table 14 value appears to be a decimal/unit error. Using electrolyzer input (6,499,506 kWh/yr) and specific consumption (46.41 kWh/kg): 6,499,506 � 46.41 ≈ **140,058 kg/yr**, confirming Table 14 value is more internally consistent.

### 3.4 Load Metrics

| Parameter | Value |
|-----------|-------|
| **Peak Load Demand** | 9 MW |
| **Daily Peak Load Duration** | 5 hours (5–10 PM) |
| **Daily Energy Demand** | 9,000 kWh/day |
| **5–6 PM Demand** | 1,500 kWh |
| **6–7 PM Demand** | 2,000 kWh |
| **7–8 PM Demand** | 2,000 kWh |
| **8–9 PM Demand** | 2,000 kWh |
| **9–10 PM Demand** | 2,000 kWh |
| **Total Annual Load** | **3,285,000 kWh/yr** |
| **Load Profile Type** | Peak load (evening, AC) |

### 3.5 Optimal Configuration

| Parameter | Value |
|-----------|-------|
| **Optimal Configuration** | 2.2 MW PV + 4.5 MW Wind (9 × 500 kW) + 3 MW PEM Electrolyzer + 50,000 kg H₂ Tank + 3 MW Gas Turbine |
| **Objective** | Meet 9 MW peak demand at minimum cost |
| **Constraints** | Peak load schedule 5–10 PM; Hydrogen self-production required |
| **Sensitivity Analysis** | Not formally conducted (single scenario simulation) |
| **Optimization Search** | HOMER Pro simulation across timesteps |

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION

### 4.1 Dispatch Strategy

The paper describes a **two-stage conversion system** rather than a traditional dispatch:

| Feature | Description |
|---------|-------------|
| **Architecture** | DC-coupled: PV (DC) + Wind (DC, via controller) → PEM Electrolyzer → H₂ Storage → Gas Turbine Generator (AC) |
| **Priority** | All available renewable power (PV + Wind) feeds the electrolyzer to produce hydrogen. The gas turbine runs on stored hydrogen to meet peak load. |
| **No Battery** | Unlike conventional hybrid systems, there is NO battery storage. Energy is stored as hydrogen. |
| **No Direct Load Feeding** | Renewable electricity does NOT directly power the load. All renewable output goes to electrolysis. |

### 4.2 Power Flow Logic

| Condition | Action |
|-----------|--------|
| **PV + Wind generating** | All DC power routed to PEM electrolyzer (via controller) |
| **Electrolyzer active** | Produces H₂ from sea water; H₂ stored in tank |
| **Peak load period (5–10 PM)** | Gas turbine generator runs on stored H₂ to produce AC power |
| **Off-peak (10 PM–5 PM)** | No gas turbine operation; electrolyzer continues to produce H₂ |
| **Excess renewable (beyond 3 MW electrolyzer capacity)** | **NOT EXPLICITLY ADDRESSED** — paper does not state what happens when PV+Wind > 3 MW |
| **H₂ storage full** | Not addressed |

### 4.3 Control Parameters

| Parameter | Value |
|-----------|-------|
| **Electrolyzer Capacity** | 3,000 kW (upper limit on renewable absorption) |
| **H₂ Tank Capacity** | 50,000 kg |
| **Gas Turbine Capacity** | 3,000 kW |
| **GT Operating Schedule** | 5–10 PM daily (1,825 hrs/yr) |
| **GT Fixed Generation Cost** | $24.09/hr |
| **GT Fuel Curve Intercept** | 0.01400 L/hr/kW |
| **GT Fuel Curve Slope** | 0.0420 L/hr/kW |
| **Electrolyzer Efficiency** | 85% |
| **PV Derating Factor** | 80% |
| **Wind Cut-in Speed** | 3 m/s |
| **Wind Cut-out Speed** | 25 m/s |

### 4.4 Algorithm Flow

The paper does NOT provide a formal algorithm flowchart or step-by-step control logic. The described logic is:

1. **Daytime/Always:** PV captures solar radiation → DC electricity; Wind turbines spin → DC electricity
2. **Power Conditioning:** Controller manages DC power from both sources to match PEM electrolyzer input requirements
3. **Electrolysis:** PEM electrolyzer splits sea water (H₂O + electrical energy → O₂ + 2H₂)
4. **Storage:** Hydrogen stored in tank (50,000 kg capacity)
5. **Generation:** During 5–10 PM peak, gas turbine burns H₂ to generate 3,000 kW AC power
6. **Delivery:** AC power supplied to Kolatoli peak load

**Chemical Reactions (sea water electrolysis):**
- Anode: Cl⁻ → ½Cl₂(g) + e⁻
- Net reaction: NaCl(aq) + H₂O(l) → Na⁺(aq) + OH⁻(aq) + H₂(g) + ½Cl₂(g)
- Overall electrolysis: 2H₂O + electrical energy → O₂ + 2H₂

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION

### 5.1 Power Generation Walkthrough

This system operates on an **indirect renewable-to-load architecture** — a distinctive approach where solar and wind power NEVER reach the load directly. Instead, all renewable output is converted to hydrogen, which is then combusted in a gas turbine during evening peak hours.

**Morning (6 AM – 12 PM):**
As solar radiation intensifies, PV output ramps from zero toward its peak (approximately 2.2 MW nameplate, derated to ~1.76 MW physical maximum with 80% derating). Meanwhile, late-morning wind speeds in Cox's Bazar average 3.4–3.7 m/s — above the 3 m/s cut-in threshold — so the 9 × 500 kW turbines also contribute. With total renewable output potentially reaching 3+ MW by late morning, the PEM electrolyzer begins or continues processing at its 3 MW capacity. Excess power beyond 3 MW is a critical unanswered question in the paper — the system has no dump load, battery, or grid connection to absorb surplus. If PV + Wind exceeds 3 MW (which is plausible given 6.7 MW total nameplate), the electrolyzer caps at 3 MW and curtailment occurs, though the paper does not explicitly model this.

**Midday (12 PM – 4 PM):**
Solar radiation peaks (up to 6.09 kWh/m²/day in April). PV output reaches daily maximum. Wind speeds are moderate (3.5–3.8 m/s). Combined renewable output likely exceeds 3 MW for several hours, but the electrolyzer caps input. Hydrogen production continues at ~15.99 kg/hr (max rated throughput), storing energy for the evening peak. With specific consumption of 46.41 kWh/kg, the electrolyzer converts up to 3 MW of electricity into ~64.6 kg/hr of H₂ at full capacity.

**Evening Peak (5 PM – 10 PM):**
Solar output drops to nearly zero by 6–7 PM (Bangladesh sunset ~5:30–6:30 PM depending on season). Wind speeds in the evening average 2.7–3.4 m/s — marginal, sometimes below cut-in. The gas turbine starts at 5 PM and runs at ~1,798 kW mean output for exactly 5 hours, consuming hydrogen at 0.04 L/kWh to generate 9,000 kWh of AC electricity matching the daily evening peak load. The GT operates ~365 days/year with 1,825 operating hours annually.

**Night (10 PM – 6 AM):**
Gas turbine shuts off. PV is zero. Wind turbines may continue generating if speeds exceed 3 m/s (post-monsoon evenings: 2.7–3.3 m/s, marginal). Any wind generation continues to produce hydrogen, rebuilding storage depleted during the evening generation cycle.

**Seasonal Variations:**
- **Monsoon (June–August):** Highest wind speeds (4.87, 4.83, 4.32 m/s) compensate for lower solar radiation (4.11, 3.81, 4.03 kWh/m²/day). Wind becomes the dominant electrolyzer power source.
- **Dry season (November–February):** Lower wind speeds (2.82–3.13 m/s) but rising solar radiation (4.56–5.33 kWh/m²/day). PV dominates hydrogen production.
- **Transition months (March–May):** Peak solar radiation (5.93–6.09 kWh/m²/day) provides the highest PV output of the year.

### 5.2 System Behavior Analysis

**Why this configuration is "optimal":**
The paper does not perform a comparative optimization across multiple configurations. HOMER Pro simulated the specific design the authors proposed. The "achieved" label comes from the system successfully meeting its 9 MW peak load target at $0.178/kWh — lower than Bangladesh's quick rental power plant rates. The choice to use hydrogen as an energy carrier rather than batteries reflects two strategic decisions:

1. **Hydrogen as long-duration seasonal storage:** A 50,000 kg hydrogen tank represents ~6,000 MWh of embodied energy (at 120 MJ/kg), providing multi-day storage that batteries of equivalent cost cannot match. This is critical because Cox's Bazar's wind resource is strongest during monsoon months while load demand is year-round.

2. **Power-to-gas-to-power cycle efficiency:** The round modest — electrolyzer ( gas turbine (71%) ≈ 60% net round-trip, not counting auxiliary loads. This is significantly lower than battery storage (85–90% round-trip). However, hydrogen's advantage is storage duration and energy density, not cycle efficiency.

**Critical design trade-off:**
The paper's most notable omission is what happens when PV + Wind output exceeds the 3 MW electrolyzer capacity. In monsoon afternoons, wind alone (4.5 MW) exceeds electrolyzer capacity. Combined with PV, this could mean 4–5 MW of curtailment daily. The system essentially "throws away" renewable energy because it lacks: (a) a battery buffer, (b) a larger electrolyzer, (c) grid export capability, or (d) a dump load. The annual hydrogen production (140,060 kg) and consumption (137,803 kg) are in near-balance, suggesting HOMER may have sized the electrolyzer to absorb most renewable output, but curtailment losses are not reported.

**Why no batteries?**
Batteries are absent from this design. The paper's system relies entirely on hydrogen for storage. This dramatically changes the economics: batteries provide high round-trip efficiency but at high cost per kWh of storage capacity. Hydrogen provides cheap long-duration storage (the tank costs only $5,000 initial) but at lower round-trip efficiency depending on gas turbine efficiency vs fuel cell cost.

### 5.3 Critical Evaluation

**Assumptions Reasonableness:**
- Sea water electrolysis at scale is still largely experimental. The paper treats PEM electrolyzer specifications as mature technology, but large-scale sea water PEM electrolysis with chlorine co-oxidation chemistry at the anode introduces engineering challenges (corrosion, chlorine handling) not addressed.
- The 85% electrolyzer efficiency and 71% gas turbine efficiency are optimistic for a small (3 MW) hydrogen-fired gas turbine. Commercial hydrogen GTs in this size range are rare.
- The hydrogen storage tank at $5,000 for 50,000 kg is implausibly cheap — this appears to be the storage vessel only, omitting compression costs which dominate hydrogen system economics.

**Limitations:**
- No optimization comparison against battery-only, fuel cell-only, or conventional diesel alternatives
- Single-year resource data (no interannual variability analysis)
- No sensitivity analysis on component sizing, resource variation, or cost parameters
- No discussion of hydrogen, storage safety, or chlorine handling from sea water electrolysis
- The electrolyzer capacity (3 MW) appears undersized relative to total renewable nameplate (6.7 MW), causing unquantified curtailment
- System serves only the 5-hour evening peak; the remaining 19 hours of village load are not addressed

**Generalizability Findings:**
The power-to-hydrogen-to-power architecture demonstrated here is relevant for coastal locations with:
- Sea water availability (electrolysis feedstock)
- Complementary solar and wind resources (seasonal complementarity)
- Concentrated evening (5-hour window)
- Need for green (zero CO₂) power

The $0.178/kWh is competitive with diesel generation in remote Bangladeshi contexts but remains higher than grid-connected solar ($0.039/kWh) — the premium is essentially the cost of firming variable renewables with hydrogen storage.

**What if parameters changed?**
- If electrolyzer capacity were doubled to 6 MW, nearly all renewable energy would be captured, hydrogen production would nearly double, and excess hydrogen could power a daytime electricity generator as well.
- If a PEM fuel cell replaced the gas turbine for power generation, noise and maintenance would decrease, but fuel cell costs in 2017 were prohibitive.
- If battery storage (even small, 1-hour buffer) were added, the electrolyzer could operate more continuously, improving capacity factor.

### 5.4 Derived/Inferred Values

| Derived Metric | Calculation | Result |
|----------------|-------------|--------|
| **Average daily hydrogen production** | 140,060 kg ÷ 365 days | **383.7 kg/day** |
| **Average daily hydrogen consumption** | 137,803 kg � 365 days | **377.5 kg/day** |
| **Net daily hydrogen surplus** | 383.7 − 377.5 | **6.2 kg/day** |
| **PV capacity factor** | 3,263,389 kWh ÷ (2,200 kW × 8,760 hrs) | **16.9%** |
| **Wind capacity factor** | 3,424,742 kWh ÷ (4,500 kW × 8,760 hrs) | **8.7%** |
| **GT capacity factor** | 3,281,028 kWh ÷ (3,000 kW × 8,760 hrs) | **12.5%** |
| **GT operational hours/day** | 1,825 hrs ÷ 365 days | **5.0 hrs/day** |
| **Electrolyzer capacity factor** | 6,499,506 kWh ÷ (3,000 kW × 8,760 hrs) | **24.7%** |
| **Electrolyzer operating hours/day** | 8,458 hrs ÷ 365 days | **23.2 hrs/day** |
| **PV daily output per kW** | 8,940.79 kWh ÷ 2,200 kW | **4.07 kWh/kW/day** |
| **Wind daily output per turbine** | 3,263,388 kWh ÷ 9 turbines ÷ 365 | ~1,001 kWh/turbine (wait: 3,424,742 ÷ 9 ÷ 365) | **~1,042 kWh/turbine/day** |
| **Storage autonomy** | 50,000 kg H₂ × 46.41 kWh/kg � 9,000 kWh daily peak | **~258 days** (theoretical, ignores GT consumption pattern) |
| **Hydrogen balance check** | Production (140,060) − Consumption (137,803) | 2,257 kg surplus (1.6%) |
| **Renewable fraction of total generation** | (3,263,389 + 3,424,742) ÷ 9,969,159 | **67.1%** |
| **Excess/unused indicator** | PV+Wind (6,688,131) − Electrolyzer input (6,499,506) | **188,625 kWh/yr potentially curtailed** (2.8% of renewable) |
| **Initial cost per kW of peak** | $6,115,000 � 9,000 kW peak | **$679/kW** |
| **Specific electrolyzer cost (implied)** | $1,800,000 ÷ 3,000 kW | **$600/kW** |
| **Specific PV cost (implied)** | $1,760,000 ÷ 2,200 kW | **$800/kW** |
| **Specific wind cost (implied)** | $1,800,000 ÷ 4,500 kW | **$400/kW** |

### 5.5 Key Takeaways

1. **Hydrogen as seasonal storage for coastal microgrids:** The paper demonstrates a proof-of-concept that PV + Wind → Hydrogen → Gas Turbine can serve concentrated peak loads in coastal Bangladesh without batteries. The round-trip efficiency loss (~40%) is the price of multi-day storage that batteries cannot economically provide.

2. **Complementary resources matter more than peak resource quality:** Cox's Bazar's solar (4.77 kWh/m²/day) and wind (3.55 m/s) are individually modest. But their seasonal anti-correlation (wind peaks in monsoon when solar dips) makes the combined system more resilient than either alone. Hydrogen storage decouples generation timing from demand timing.

3. **The gas turbine is the system bottleneck:** At 3 MW capacity sized for peak load, but with only 3 MW electrolyzer capacity sized for average renewable input (mean PV: 373 kW + mean Wind: 391 kW = ~762 kW actual average), the system is oversized for average conditions but potentially undersized for capturing windy monsoon afternoons when wind alone could push >3 MW.

4. **Cost competitiveness is contextual at $0.178/kWh:** This is cheaper than Bangladesh's quick rental diesel plants ($0.20+/kWh) but approximately 4× the standalone solar PV cost ($0.039/kWh). The premium is the cost of reliability — converting variable solar/wind into firm dispatchable evening power via hydrogen.

5. **Sea water electrolysis adds complexity not fully addressed:** The paper shows chemical reactions for chlorine evolution at the anode (from NaCl in sea water) but does not address the engineering implications: chlorine gas handling, electrode corrosion, or pre-treatment requirements. The economics assume conventional PEM operation (designed for pure water), which may not translate directly to sea water feedstock.

---

*Summary generated from: Kabir, K.M. & Matin Bhuiyan, M.A. (2017). "Design & simulation of hydrogen based hybrid green power system using sea water for Cox's Bazar." Cogent Engineering, 4:1, 1347029. DOI: 10.1080/23311916.2017.1347029*
