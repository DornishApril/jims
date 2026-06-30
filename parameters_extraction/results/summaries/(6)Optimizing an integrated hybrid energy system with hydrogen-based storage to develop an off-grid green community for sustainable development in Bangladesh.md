# Paper Summary: Optimizing an integrated hybrid energy system with hydrogen-based storage to develop an off-grid green community for sustainable development in Bangladesh

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title**: Optimizing an integrated hybrid energy system with hydrogen-based storage to develop an off-grid green community for sustainable development in Bangladesh
- **Authors**: Asif Jaman, Rafid Al Mahmud, Barun K. Das, Mohammad Shahed H.K. Tushar
- **Journal/Conference name**: International Journal of Hydrogen Energy
- **Year of publication**: 2025 (Volume 97, pages 766–786, available online December 4, 2024)
- **DOI**: 10.1016/j.ijhydene.2024.11.454
- **Study location**: Katakhali municipality, Rajshahi City Corporation (RCC), northwestern Bangladesh (24°21'54.5"N, 88°40'30.8"E)
- **System type**: Off-grid PV/WT/Biogas/Fuel Cell/Electrolyzer-H2 Tank hybrid renewable energy system (HRES) with dual load (community + EV charging stations)
- **Study type**: Simulation-based optimization study
- **Software/tools used**: HOMER (resource/load data pre-processing), MATLAB (energy management strategy, multi-objective optimization, fuzzy decision-making)
- **Optimization method used**: NSGA-II (Non-dominated Sorting Genetic Algorithm II) with fuzzy-based multi-criteria decision-making for final solution selection

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Model/Type | Rated Capacity | Units in Optimal Configuration | Key Specifications |
|-----------|-----------|---------------|-------------------------------|-------------------|
| PV module | SPR-E20-327 (SunPower) | 327 Wp | Sufficient units for 270 kW total | 20.4% efficiency, Vmpp=54.7V, Impp=5.98A, temp coefficient = −0.35%/°C, derating ratio = 88%, lifespan = 25 years |
| Wind turbine | H-Darrius type VAWT | 5 kW | Sufficient units for 375 kW total | Rotor diameter=5.8m, rotor height=10m, 5 blades, cut-in=1.8 m/s, rated=12 m/s, cut-off=65 m/s, generator efficiency=80%, lifespan=20 years |
| Biogas generator | Generic MSW/cow-dung-fed | 50 kW per unit (up to 9 units) | 500 kW total (10 units × 50 kW, but constrained by NBG=9 max in optimization) | Overall efficiency 28.45%, LHV of biogas=23 MJ/m³, density=1.20 kg/m³, lifespan=25,000 hours |
| Fuel cell | PEMFC (Proton Exchange Membrane) | 2 kW per unit | Sufficient units for 70 kW total | Electrical conversion efficiency ηFC=50%, HHV of H₂=39.4 kWh/kg, lifespan=5 years |
| Electrolyzer | PEM electrolyzer | 2 kW per unit | Sufficient units for 2000 kW total | Lifespan=15 years; performance modeled via empirical H₂ production equation |
| Hydrogen storage tank | Generic pressurized H₂ tank | 6 kg per unit | Sufficient units for 726 kg total | Lifespan=20 years |
| Inverter (bi-directional) | Generic | 1 kW | 311 kW total | ηinv=96%, lifespan=15 years |

### 2.2 Total System Capacity

- **Total generation capacity (PV+WT+FC+BG)**: 270 + 375 + 70 + 500 = **1,215 kW**
- **Total hydrogen storage**: **726 kg**
- **Total conversion capacity (electrolyzer+inverter)**: 200 + 311 = **511 kW**
- **Total electrolyzer capacity**: 2,000 kW

### 2.3 Component Costs (Capital, Replacement, O&M)

| Component | Capital Cost | Replacement Cost | O&M Cost | Lifetime |
|-----------|-------------|-----------------|----------|----------|
| PV module | $1,300/kW | $0 | $20/kW/year | 25 years |
| Wind turbine | $420/kW | $0 | $0.011/kWh | 20 years |
| Biogas generator | $1,600/kW | $1,280/kW | $0.025/hour | 25,000 hours |
| Fuel cell | $3,000/kW | $2,500/kW | 0.02 × initial expenditure/year | 5 years |
| Hydrogen tank | $660/kW | — | 0.02 × initial expenditure/year | 20 years |
| Electrolyzer | $2,000/kW | $1,500/kW | $20/unit/year | 15 years |
| Inverter | $300/kW | $300/kW | $0 | 15 years |

### 2.4 Economic Parameters

- **Project lifetime**: **25 years**
- **Real annual interest rate**: used for discounting (NPC calculations) — exact rate implied by CRF in COE formula; paper refers to standard practice, but **COE numerator = NPC × CRF(i,L)**. The paper does not explicitly state the interest rate value used in the NPC/CRF calculation, though references [67,68] define CRF(i,L).
- **Biogas cost**: $0.33/m³ (reference [53])
- **Carbon emission tax**: $0.015 per kg CO₂-eq
- **Currency and cost year**: USD, cost year not explicitly stated
- **Inflation rate**: Not reported explicitly (real interest rate used)

### 2.5 Resource Data

- **Solar irradiance**: Sourced from NASA meteorological database via HOMER; daily average above 5 kWh/m²/day (peaks close to 10 kW/m²/day); hourly time steps used
- **Wind speed**: Average annual wind speed approximately **2.60 m/s** at the study site; sourced from NASA/HOMER; hourly time steps
- **Temperature data**: Used in PV cell temperature calculations (via NOCT model); not separately reported
- **Biogas feedstock**: Municipal solid waste (MSW) at 124.02 tons/day total, of which **71.1% (98.13 tons/day organic fraction)** is biodegradable; **7,500 kg/day of cow dung** (from ~500 cattle); 1 ton MSW → 66 m³ biogas; 1 kg cow dung → 0.04 m³ biogas
- **Daily biogas potential**: ~6,776.58 m³/day (300 from cow dung + 6,476.58 from MSW)
- **Daily electricity from biogas potential**: ~43,302 kWh/day (using 6.39 kWh per m³)
- **1 m³ biogas ≈ 6.39 kWh electrical energy**

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

| Metric | PV/WT/FC/BG (Optimal) | PV/FC/BG | WT/FC/BG |
|--------|----------------------|---------|---------|
| **COE** | **0.1634 $/kWh** | 0.1951 $/kWh | 0.2457 $/kWh |
| **NPC** | **$3,988,169** | $4,762,796 | $5,997,060 |

- Payback period: Not reported
- IRR/ROI: Not reported

### 3.2 Reliability Metrics

| Metric | PV/WT/FC/BG | PV/FC/BG | WT/FC/BG |
|--------|------------|---------|---------|
| **LPSP constraint** | 1 ± 0.5% | Same | Same |
| **Unmet electric demand (kWh/yr)** | 16,692 | 19,838 | 10,128 |

- LPSP exact value: The paper states LPSP ≤ 1% ± 0.5% as constraint; exact achieved LPSP not separately reported
- System availability: Not explicitly stated as a percentage
- LOLP: Not mentioned

### 3.3 Generation Metrics

| Metric | PV/WT/FC/BG | PV/FC/BG | WT/FC/BG |
|--------|------------|---------|---------|
| PV energy (kWh/yr) | 453,956 | 1,415,415 | 0 |
| Wind energy (kWh/yr) | 235,895 | 0 | 558,388 |
| Biogas energy (kWh/yr) | 1,400,252 | 1,083,146 | 1,581,642 |
| **Total generation (kWh/yr)** | 2,090,103 | 2,498,561 | 2,140,030 |
| **Electrical demand supplied (kWh/yr)** | 1,907,186 | 1,907,186 | 1,907,186 |
| **Excess energy (kWh/yr)** | 273,130 | 808,788 | 310,855 |
| Energy loss (kWh/yr) | 49,202 | 143,641 | 156,871 |
| System efficiency | **85%** | 62% | 78% |
| Excess Energy Utilization Factor (EUF) | 82% | 82% | 50% |

- Renewable fraction: Not explicitly stated as a percentage
- Hydrogen production/consumption: Modeled hourly via electrolyzer/FC equations; annual totals not stated
- Diesel consumption: **None** (system has no diesel generator)
- Grid import/export: **None** (off-grid system)

### 3.4 Load Metrics

| Metric | Summer (Mar–Oct) | Winter (Nov–Feb) |
|--------|-----------------|-----------------|
| **EVCS daily demand** | 3,072 kWh/day | 2,688 kWh/day |
| **Community daily demand** | 2,461.06 kWh/day | 1,837.34 kWh/day |
| **Combined daily demand** | 5,533.06 kWh/day | 4,525.34 kWh/day |
| **Annual electrical demand** | **1,907,186 kWh/yr** (same for both) | |
- **Peak load**: Not explicitly stated as a single kW value
- **Average load**: ~217.7 kW (1,907,186 kWh / 8760 h)
- **Load profile type**: Community (500 residential + 2 schools + 1 health center + 10 retail + 1 commercial + 1 post office + 1 bank + 2 ATMs + streetlights) + EV Charging Stations (5 stations, each 4.8 kW BEV)

### 3.5 Optimal Configuration (Three HRES Variants Compared)

| Component | PV/WT/FC/BG | PV/FC/BG | WT/FC/BG |
|-----------|:-----------:|:--------:|:--------:|
| PV (kW) | 270 | 842 | 0 |
| WT (kW) | 375 | 0 | 890 |
| Biogas gen. (kW) | 500 | 500 | 500 |
| FC (kW) | 70 | 200 | 58 |
| H₂ tank (kg) | 726 | 1,246 | 1,104 |
| Electrolyzer (kW) | 2,000 | 274 | 74 |
| Converter (kW) | 311 | 969 | 67 |

- **Objective function**: Minimize {COE, HHD} (Cost of Energy and Human Health Damage)
- **Constraints**: Energy balance (Eq. 35), H₂ storage capacity bounds, LPSP ≤ 1%
- **NSGA-II parameters**: Population=200, Generations=200, Crossover rate=0.9, Mutation rate=0.1
- **Sensitivity analysis**: Load increments of 10%, 20%, 30%, 40%, 50% above baseline; PV modules increase 187.6% at 50% load increment
- **Load increment effects on cost**: TNPC at baseline=$3,988,169; at +50% load=$5,847,320 (+46.59%); at +10%=$4,378,024 (+9.77%)

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION

### 4.1 Dispatch Strategy

The paper defines a rule-based power management strategy (PMS) with three main branches:

1. **ENet(t) > 0** (renewable generation exceeds community load demand):
   - Community load is fully met by PV+WT
   - Check if excess ≥ EVCS demand: if so, use remaining excess for electrolyzer H₂ production
   - If H₂ tank is full, discharge surplus to dump load (resistive)
   - If excess < EVCS demand, check H₂ tank SOC: if sufficient, run FC for EV deficit; otherwise start BG

2. **ENet(t) = 0** (renewable generation = community load):
   - No excess energy produced
   - Check H₂ tank SOC: if sufficient, run FC for EVCS demand
   - Otherwise start BG (minimum 30% rated power = 15 kW per unit as minimum load threshold)
   - Below 15 kW threshold = unmet load

3. **ENet(t) < 0** (renewable generation < community load):
   - FC makes up deficit using H₂ from tank
   - If FC cannot fill shortfall and P_load ≥ 30% of BG rated power, start BG
   - Below 15 kW threshold = unmet load
   - If renewables + storage both unavailable, BG runs at max capacity

### 4.2 Power Flow Logic

- **Excess renewable →** electrolyzer (H₂ production) → if H₂ tank full → dump load
- **Deficit →** fuel cell (from H₂ tank) → if FC insufficient/unavailable → biogas generator
- **Biogas generator minimum load**: 15 kW per unit (30% of 50 kW rated); below this threshold, load is classified as "unmet"
- **Battery role**: No battery in this system — hydrogen serves as the only storage medium
- **EVCS charging**: Prioritized from excess renewable → FC (if H₂ available) → BG
- **Grid interaction**: None (designed as off-grid system)

### 4.3 Control Parameters

- **BG minimum load threshold**: **15 kW per unit** (30% of 50 kW rated)
- **BG minimum power per unit**: 15 kW
- **Inverter efficiency (ηinv)**: **96%**
- **FC efficiency (ηFC)**: **50%**
- **H₂ higher heating value (HHVH₂)**: **39.4 kWh/kg**
- **H₂ tank capacity bounds**: Not stated numerically (HHS,max and HHS,min not given specific values)
- **PV cell efficiency**: **20.4%** (SPR-E20-327 panel)
- **VAWT cut-in**: 1.8 m/s, rated: 12 m/s, cut-off: 65 m/s
- **BG overall conversion efficiency**: **28.45%**
- **Simulation time step**: 1 hour (8760 time steps per year)

### 4.4 Algorithm Flow

The power management strategy flow is depicted in Fig. 7 of the paper:

```
Step 1: Measure PV output (EPV), WT output (EWT), community load (EElec), EVCS demand (EEVCS)
Step 2: Compute ENet = EPV + EWT − EElec  (AC side after inverter efficiency)
Step 3: If ENet > 0 (surplus):
  - Excess energy = ENet
  - If excess ≥ EVCS demand: serve EVCS, remaining → electrolyzer → H₂ tank
  - If H₂ tank full: dump surplus
  - If excess < EVCS: serve what possible, check H₂ tank for FC to make up EVCS deficit
    - If H₂ tank SOC sufficient: run FC
    - Else: start biogas generator
Step 4: If ENet = 0 (balanced):
  - No excess → check H₂ tank for EVCS demand via FC
  - If insufficient: start BG if load ≥ 15 kW
Step 5: If ENet < 0 (deficit):
  - FC runs using H₂ tank to fill shortfall
  - If FC insufficient and P ≥ 15 kW: start BG as supplement
  - Below 15 kW: unmet load
Step 6: If all resources failed: BG runs at max capacity
```

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

On a typical summer day at Katakhali, the system operates as follows:

**Early Morning (4:00–6:00 AM):**
Sunrise has not yet begun, wind contribution is typically low (~2.6 m/s average may produce up to ~2-3 kW from each 5 kW VAWT due to sub-rated speed), and the community load begins rising as households wake up. The fuel cell is active, withdrawing hydrogen from the 726 kg tank to cover the shortfall. If the deficit persists and exceeds 15 kW, the biogas generator starts, burning MSW/cow-dung-derived biogas (at ~$0.33/m³). Peak load is reported at 7:00 AM, met with FC + BG augmentation when PV is still ramping up.

**Midday (10:00 AM–2:00 PM):**
With solar irradiance averaging above 5 kWh/m²/day and peaks approaching 10 kW/m²/day, the 270 kW PV array at 20.4% efficiency generates substantial power. The combined community + EVCS load of ~5,533 kWh/day in summer is spread over 24 hours, so peak instantaneous demand is much lower. Excess generation drives the 2,000 kW electrolyzer at high capacity, producing hydrogen via the empirical equation (HElectrolyzer = 1.43×10⁻³ + 2.39×10⁻² × EElectrolyzer − 4.32×10⁻⁵ × EElectrolyzer²). This hydrogen is stored in the 726 kg-rated tank. The authors note there is no dumped energy and no unmet load during the specific day studied in the PV/WT/FC/BG configuration.

**Evening (5:00–8:00 PM):**
Solar output drops as irradiance declines, while community load peaks (evening lighting, appliances). The fuel cell ramps up using stored hydrogen, and the biogas generator supplements. The paper notes that without wind turbines (PV/FC/BG case), evening becomes more challenging, with dumped energy from daytime over-generation and occasional unmet load at 7:00 AM.

**Night (9:00 PM–3:00 AM):**
No solar generation. Wind may contribute intermittently. The system relies on biogas generators running on stored biogas and fuel cells consuming stored hydrogen. The 6.39 kWh/m³ conversion rate means each m³ of biogas (costing $0.33) yields ~$0.55 worth of electricity at the achieved COE of $0.1634/kWh — a profitable operating margin for BG at night.

**Seasonal Variation:**
Summer demand (community: 2,461 kWh/day) is significantly higher than winter (1,837 kWh/day) because of air conditioning and fan loads (Table 4). EVCS demand also drops from 3,072 to 2,688 kWh/day in winter. The system must be sized to satisfy summer peaks, meaning winter operation will have larger relative excess capacity.

### 5.2 System Behavior Analysis

**Why PV/WT/FC/BG was chosen as optimal:**
The multi-objective optimization reveals that including both PV and WT creates the most balanced generation profile. Solar peaks midday, wind (especially VAWT performing well at lower speeds in Bangladesh's modest wind regime) provides complementary temporal coverage. The combination reduces total excess energy (273,130 vs 808,788 vs 310,855 kWh/yr), which translates to lower component oversizing and better EUF.

vs PV/FC/BG (no wind):
Without WT, PV must be scaled to 842 kW (3× larger), creating massive excess (808,788 kWh/yr, i.e. 42% of generation wasted). Despite lower BG emissions, total lifecycle emissions rise because manufacturing 842 kW of PV panels produces more CO₂ per panel than manufacturing wind turbines and a smaller PV array. The cost jumps to $0.1951/kWh (+19.4%).

vs WT/FC/BG (no solar):
Without PV, WT capacity skyrockets from 375 to 890 kW (+137.3%). Wind-only systems have less predictable seasonal patterns, and despite good excess energy utilization, the COE reaches $0.2457/kWh (+50.3% vs PV/WT/FC/BG).

**Hydrogen storage sizing:**
The 726 kg H₂ tank (~28,573 kWh of chemical energy at 39.4 kWh/kg × 50% FC efficiency = ~14,287 kWh usable electrical energy) provides roughly 2.6 hours of peak demand (5,533 kWh/day ÷ 24 h × 96% inverter efficiency ≈ 221 kW average × 2.6 h ≈ 575 kWh). The electrolyzer capacity at 2,000 kW is oversized relative to PV+WT output (only 645 kW total renewable capacity), meaning it can rapidly absorb surpluses when generation peaks.

**Dispatch strategy implications:**
The biogas generator serves as a high-cost backup (requiring feedstock handling, $0.025/hour O&M plus fuel cost), used only when hydrogen storage is depleted. The authors note that the BG minimum load limit of 15 kW creates an "unmet load band" where small deficits below 15 kW cannot be served — a design trade-off to prevent inefficient BG operation at very partial load.

### 5.3 Critical Evaluation

**Assumptions:**
- Hourly resolution with negligible intra-hour variation: reasonable for a system of this scale
- No T&D losses: optimistic given the small geographic scale of Katakhali
- No HRES device failures or soiling: unrealistic for long-term PV performance in Bangladesh's humid, dusty climate
- Effects of humidity, ambient pressure, and soiling neglected: PV output may be 5-15% lower in practice
- No battery in the system: unconventional but deliberate — the authors argue hydrogen eliminates battery replacement costs and disposal issues

**Limitations:**
- The study uses a mathematical model in MATLAB with idealized component behavior, limiting consideration of dynamic transients
- NSGA-II with fixed population/generations may not explore the full solution space; the authors mention "trial and error" for parameter bounds
- Economic parameters likely from literature, not site-specific quotations
- HOMER used only for resource pre-processing; full optimization in MATLAB limits comparison with HOMER's built-in dispatch validation
- No sensitivity analysis on interest rate, component cost escalation, or fuel price variability
- No consideration of hydrogen storage safety or community acceptance

**Generalizability:**
The PV/WT/FC/BG architecture with MSW biogas is highly transferable to South/Southeast Asian contexts with similar municipal waste generation and modest wind resources. The specific component sizing would change, but the optimization framework (NSGA-II with fuzzy decision-making on COE/HHD Pareto front) is broadly applicable.

**What if diesel were included?**
The paper evaluated only 3 configurations; a PV/WT/DG/H₂ hybrid could reduce BG dependency and potentially lower lifecycle emissions (modern diesel generators at >80% load can be clean), but would increase operational fuel costs and carbon penalties significantly.

### 5.4 Derived/Inferred Values

The following values are NOT stated in the paper but can be calculated from the provided data:

| Derived Value | Calculation | Result |
|--------------|-------------|--------|
| Average daily PV generation (PV/WT/FC/BG) | 453,956 kWh/yr ÷ 365 | **1,244 kWh/day** |
| Average daily WT generation (PV/WT/FC/BG) | 235,895 kWh/yr ÷ 365 | **646 kWh/day** |
| Average daily BG generation (PV/WT/FC/BG) | 1,400,252 kWh/yr ÷ 365 | **3,836 kWh/day** |
| PV capacity factor (PV/WT/FC/BG) | 453,956 ÷ (270 × 8760) | **19.2%** |
| WT capacity factor (PV/WT/FC/BG) | 235,895 ÷ (375 × 8760) | **7.2%** |
| BG capacity factor (PV/WT/FC/BG) | 1,400,252 � (500 × 8760) | **32.0%** |
| Average daily unmet load (PV/WT/FC/BG) | 16,692 kWh/yr ÷ 365 | **45.7 kWh/day** |
| Storage autonomy (H₂ usable energy � avg load) | ~14,287 kWh ÷ 217.7 kW | **~65.6 hours** |
| EUF formula verification | Paper confirms 82% for PV/WT/FC/BG | Consistent |
| Load growth sensitivity | COE stability despite 50% load increase | Demonstrates robust NSGA-II optimization |
| CO₂ penalty share of COE | ($1,856/yr × 25 yr) � (1,907,186 kWh/yr × 25) | ~0.039 $/kWh effective surcharge |

**Cost breakdown by component (% of NPC):**
- BG share: **36.20%** (stated in paper)
- PV share: Inferred from cost data (~13% of NPC for PV/WT/FC/BG)
- WT share: Significant but < FC contribution overall
- FC cost share: Lower capital share but higher relative due to 5-year replacement cycle

### 5.5 Key Takeaways

1. **The PV/WT/FC/BG hybrid configuration achieves the lowest COE ($0.1634/kWh) and highest system efficiency (85%) among the three HRES variants tested**, demonstrating that combining solar, wind, biogas with hydrogen storage provides the optimal balance of cost, reliability, and environmental impact for off-grid electrification in Bangladesh.

2. **Biogas generators contribute 69.90% of total lifecycle CO₂ emissions** despite providing baseload reliability, highlighting a critical trade-off: the waste-to-energy approach solves municipal waste management but creates an emission source that must be managed through carbon pricing.

3. **The system avoids grid dependency entirely** while simultaneously supporting EV charging infrastructure, proving that hybrid renewables with hydrogen storage can support both community and transportation loads without fossil fuel backup or grid import.

4. **COE remains stable ($0.1574–$0.1634/kWh) even with 50% load increment**, demonstrating that the NSGA-II-optimized system design has sufficient margin and that scaling up production linearly increases NPC without disproportionately increasing per-unit energy costs.

5. **Hydrogen storage (726 kg) and electrolyzer capacity (2,000 kW) are critically oversized relative to renewable generation (645 kW PV+WT)**, reflecting the high priority placed on minimizing excess energy waste and ensuring FC can meet deficits over extended low-renewability periods.
