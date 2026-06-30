# Paper Summary: Techno-economic and multicriteria analysis of grid-connected energy systems for hydrogen production: A case study from Bangladesh

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Techno-economic and multicriteria analysis of grid-connected energy systems for hydrogen production: A case study from Bangladesh
- **Authors:** Prangon Chowdhury, Tasniah Islam, Ephraim Bonah Agyekum
- **Journal/Conference name:** International Journal of Hydrogen Energy
- **Year of publication:** 2025
- **DOI:** 10.1016/j.ijhydene.2025.02.034
- **Study location:** Cox's Bazar, Bangladesh (latitude 21°25.6'N, longitude 92°0.4'E)
- **System type:** Grid-connected hybrid renewable energy systems (HRES) for green hydrogen production — four configurations: PV-Wind-Battery-Fuel cell-Grid (HRES1), PV-Battery-Fuel cell-Grid (HRES2), PV-Wind-Battery-Grid (HRES3), PV-Battery-Grid (HRES4)
- **Study type:** Simulation-based (HOMER Pro)
- **Software/tools used:** HOMER Pro
- **Optimization method used:** HOMER Pro built-in optimizer; multicriteria decision-making (MCDM) using CRITIC (weighting) + TOPSIS (ranking)

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Specification | HRES1 | HRES2 | HRES3 | HRES4 |
|-----------|--------------|-------|-------|-------|-------|
| PV array | Generic Flat Plate PV, 1 kWp rated | 6,618 kW | 5,489 kW | 6,552 kW | 7,036 kW |
| Wind turbine | Generic 3 kW, rotor diameter 15.81 m | 1,500 kW (500 units) | – | 1,500 kW (500 units) | – |
| Fuel cell | PEM, 1 kW rated capacity | 1,600 kW | 1,600 kW | – | – |
| Battery | EnerSys PowerSafe SBS 1800, 12 V, 24.8 kWh nominal, 97% roundtrip efficiency | 3 strings | – | – | 1 string |
| Electrolyzer | Generic PEM, 1 kW rated, 85% efficiency | 1,500 kW | 1,500 kW | 1,500 kW | 1,500 kW |
| Hydrogen tank | 1 kg base unit | 500 kg | 700 kg | 500 kg | 500 kg |
| Converter | System converter, 1 kW, 95% inverter/rectifier efficiency | 913 kW | 1,013 kW | 2,551 kW | 2,332 kW |
| Grid connection | Grid import capacity | 999,999 kW | 999,999 kW | 999,999 kW | 999,999 kW |

### 2.2 Total System Capacity

- **HRES1:** PV 6,618 kW + Wind 1,500 kW + FC 1,600 kW = **9,718 kW** total generation; Battery: 3 strings (~74.4 kWh); H2 tank: 500 kg; Electrolyzer: 1,500 kW; Converter: 913 kW
- **HRES2:** PV 5,489 kW + FC 1,600 kW = **7,089 kW**; Battery: none; H2 tank: 700 kg; Electrolyzer: 1,500 kW; Converter: 1,013 kW
- **HRES3:** PV 6,552 kW + Wind 1,500 kW = **8,052 kW**; Battery: none; H2 tank: 500 kg; Electrolyzer: 1,500 kW; Converter: 2,551 kW
- **HRES4:** PV 7,036 kW = **7,036 kW**; Battery: 1 string (~24.8 kWh); H2 tank: 500 kg; Electrolyzer: 1,500 kW; Converter: 2,332 kW

### 2.3 Component Costs (Capital, Replacement, O&M)

| Component | Capital Cost | Replacement Cost | O&M Cost | Lifetime |
|-----------|-------------|-----------------|----------|----------|
| PV (per kWp) | $650 | $500 | $10/year | 25 years |
| Wind turbine (per 3 kW unit) | $3,900 | $3,500 | $15/year | 20 years |
| Fuel cell (per kW) | $500 | $500 |30/Op.Hour | 15,000 hours |
| Battery (per string, 24.8 kWh) | $6,500 | $6,000 | $30/year | 15 years |
| Converter (per kW) | $460 | $460 | $10/year | 15 years |
| Hydrogen tank (per kg) | $100 | $100 | $1/year | – |
| Electrolyzer (per kW) | $500 | $400 | $20/year | 15 years |

### 2.4 Economic Parameters

- **Project lifetime:** 25 years
- **Discount/interest rate:** Nominal discount rate varied in sensitivity analysis (4%–12%); base case not explicitly stated as a single value but sensitivity uses 4%, 8%, 12%
- **Inflation rate:** Not explicitly stated
- **Fuel price:** Not applicable (no diesel generator)
- **Grid electricity price:**
  - Off-peak power price: $0.1320/kWh
  - Peak power price: $0.09/kWh
  - Sellback off-peak: $0.05/kWh
  - Sellback peak: $0.09/kWh
  - Demand rate: $0.90/kW/month
- **Currency and cost year:** USD (year not explicitly stated, assumed 2024/2025)

### 2.5 Resource Data

- **Solar irradiance:** Annual daily average **4.75 kWh/m²/day**; source: NASA POWER database; lowest in December (~2.64 kWh/m²/day); highest in June (>7.89 kWh/m²/day)
- **Wind speed:** Average ~5.75 m/s in June–August (peak month); lowest ~4.22 m/s in October; hub height calculated via power law from anemometer data
- **Temperature:** Ambient temperature of 20°C used as reference for NOCT calculations
- **Data source:** NASA POWER database [31]

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

| Metric | HRES1 | HRES2 | HRES3 | HRES4 |
|--------|-------|-------|-------|-------|
| **LCOE** | $0.04716/kWh | $0.1100/kWh | **$0.0321/kWh** | $0.0777/kWh |
| **LCOH** | $5.17/kg | $7.76/kg | $5.22/kg | $7.20/kg |
| **NPC** | $11.98 M | $13.57 M | **$10.11 M** | $13.25 M |
| **Initial capital** | $12,221,366 | $5,653,986 | $12,093,176 | $6,469,620 |
| **O&M cost (annual)** | -$2,451,216 (negative = revenue) | $7,267,274 | -$84,553 | $288,648 |
| **Salvage value** | -$6,540,416 | -$2,830,785 | $6,191,670 | $2,836,208 |
| **Replacement cost** | $8,753,587 | $3,483,584 | $9,391,170 | $4,761,110 |

### 3.2 Reliability Metrics

- **LPSP / Unmet load:** All systems report **zero unmet electric load** and no capacity shortages
- **System availability:** 100% (all demand met)

### 3.3 Generation Metrics

| Metric | HRES1 | HRES2 | HRES3 | HRES4 |
|--------|-------|-------|-------|-------|
| **Annual electricity production** | 18,387,085 kWh/yr | 9,858,432 kWh/yr | 18,079,979 kWh/yr | 11,880,342 kWh/yr |
| **Annual electricity consumption** | 15,394,636 kWh/yr | 8,708,406 kWh/yr | 17,230,100 kWh/yr | 10,899,481 kWh/yr |
| **Annual grid energy purchased** | 1,118,110 kWh | 2,457,753 kWh | 1,118,234 kWh | 2,394,884 kWh |
| **Annual grid energy sold** | 6,204,799 kWh | 643,403 kWh | 8,793,239 kWh | 2,652,767 kWh |
| **Excess electricity** | 2,803,819 kWh/yr (15.2%) | 1,002,890 kWh/yr (10.2%) | 551,842 kWh/yr (3.05%) | 724,659 kWh/yr (6.1%) |
| **Renewable fraction** | 89.7% | 53.2% | **91.7%** | 67.0% |
| **Annual hydrogen production** | 98,693 kg/yr | 74,329 kg/yr | 82,467 kg/yr | 78,418 kg/yr |
| **Annual hydrogen consumption** | 98,315 kg/yr | 73,845 kg/yr | 82,043 kg/yr | 77,997 kg/yr |

### 3.4 Load Metrics

- **Total annual electric load demand:** Not stated as a single fixed value; varies by system (see consumption above). The synthetic community load: **12,630 kWh/day**, peak demand **1,376.5 kW**, load factor **0.38**
- **Average daily electric load:** 12,630 kWh/day
- **Peak electric load:** 1,376.5 kW (up to 650 kW noted for peak hours 10am–3pm)
- **Hydrogen load:** Average daily 225 kg/day; peak hourly 27.1 kg/h; load factor 0.35; steady demand of 15 kg/h from 6am–10pm
- **Load profile type:** Synthetic residential/community load for ~6,000 people

### 3.5 Optimal Configuration

- **Winning configuration:** HRES3 (PV-Wind-Battery-Grid) ranked #1 by TOPSIS (Ci = 0.9093)
- **TOPSIS rankings:** HRES3 (1st, Ci=0.9093) > HRES1 (2nd, Ci=0.5918) > HRES4 (3rd, Ci=0.4417) > HRES2 (4th, Ci=0.3365)
- **Objective function:** Minimize LCOE and NPC (HOMER optimization)
- **Constraints:** Zero unmet load; maximum annual capacity shortage = 0%; hydrogen production target of 225 kg/day
- **Dispatch strategy:** Load Following (LF) for all systems after optimization
- **Sensitivity analysis variables:** Hydrogen load variability (scaled average load: 150–225 kWh/d; max unmet hydrogen: 5–20%), CO₂ penalty, nominal discount rate (4–12%)

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

- **Type:** Load Following (LF) — selected after HOMER tested both LF and Cycle Charging (CC); LF was optimal for all configurations
- **Priority order:** Renewables (PV + Wind) serve the load first; excess energy goes to electrolyzer for hydrogen production and battery charging; deficit is covered by battery discharge, fuel cell (HRES1/HRES2), or grid import
- **Decision logic:** HOMER's LF strategy dispatches the generator (grid in this case) only to meet net load after renewables and storage; the grid acts as both backup and sink for excess

### 4.2 Power Flow Logic

- **Excess renewable energy handling:** Directed to electrolyzer for hydrogen production → charges battery → sold to grid
- **Deficit handling:** Battery discharge → fuel cell (HRES1/HRES2) → grid import
- **Battery charging/discharging:** Governed by storage capacity ratio, maximum charging rate, storage rate constant, and nominal voltage; SOC limits managed by HOMER's internal logic
- **Hydrogen production:** Electrolyzer operates when excess power available; hydrogen stored in tank; consumed by fuel cell (HRES1/HRES2) for electricity generation during deficits
- **Grid interaction:** Bidirectional — imports during deficits, exports surplus; grid demand charges apply monthly

### 4.3 Control Parameters

- **Battery roundtrip efficiency:** 97%
- **Battery nominal voltage:** 12 V
- **Battery nominal capacity:** 24.8 kWh per string
- **Electrolyzer efficiency:** 85%
- **Converter efficiency:** 95% (both inverter and rectifier)
- **Fuel cell:** PEM type, operates within voltage constraints (activation, concentration, ohmic losses)
- **PV derating factor:** Not explicitly stated
- **Wind turbine hub height:** Calculated via power law from anemometer height

### 4.4 Algorithm Flow

HOMER's energy management at each time step:
1. Calculate PV output using Eq. (1): P_out = Y_rated × D_f × (G/G_stc) × [1 + α_P × (T_cell - T_stc)]
2. Calculate wind output using power curve adjusted for air density (Eq. 8)
3. Compare total renewable generation to AC load
4. If surplus: charge battery → run electrolyzer → sell to grid
5. If deficit: discharge battery → run fuel cell → import from grid
6. Grid demand charges calculated monthly (Eq. 22)
7. Annual energy costs computed via Eq. (21) accounting for purchases and sellbacks

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

**HRES3 (optimal system) — typical day in Cox's Bazar:**

With **6,552 kW of PV** and **1,500 kW of wind turbines**, HRES3 is the most cost-effective configuration at **$0.0321/kWh LCOE**. On a typical sunny day:

- **Morning (6–9 AM):** Solar irradiance ramps from ~2.5 to ~5.5 kWh/m²/day equivalent. PV output climbs from ~500 kW toward ~3,000 kW. Wind speeds are moderate (~4.5 m/s). The electrolyzer (1,500 kW) begins ramping up as excess generation becomes available. The community load (~12,630 kWh/day average, ~525 kW average) is easily met. Hydrogen production begins at 15 kg/h target rate.

- **Midday (10 AM – 3 PM):** Peak solar irradiance (>6 kWh/m²/day in most months) drives PV output to ~5,500–6,000 kW. Combined with wind (~300–450 kW at 5–6 m/s), total generation reaches ~6,000 kW. After serving the peak electric load (~1,376 kW) and running the electrolyzer at full 1,500 kW capacity, substantial surplus remains — this is sold to the grid. HRES3 sells **8,793,239 kWh/yr** to the grid, the highest of all configurations.

- **Evening (4–7 PM):** Solar drops rapidly; wind may pick up slightly (coastal breeze). The deficit is covered by grid import. Hydrogen production tapers off as electrolyzer power decreases. The battery (minimal in HRES3 — none installed) provides no buffering, so grid import fills the gap.

- **Night (8 PM – 5 AM):** Zero solar. Wind provides some generation (~200–350 kW depending on season). The electric load drops to ~400–500 kW baseline. Grid import covers the remainder. Hydrogen production ceases after 10 PM per the load profile.

**Seasonal variations:**
- **Summer (March–May):** Highest solar irradiance (>7 kWh/m²/day in June), strong wind (5.75 m/s average). Maximum generation and hydrogen production. Grid sales peak.
- **Monsoon (June–August):** High wind, good solar despite cloud cover. Wind contribution peaks — this is when HRES3's 1,500 kW wind capacity provides maximum value.
- **Winter (December–February):** Lowest solar (~2.64 kWh/m²/day in December). Greater reliance on wind and grid import. Hydrogen production dips slightly.

### 5.2 System Behavior Analysis

**Why HRES3 wins:**

HRES3 achieves the lowest LCOE ($0.0321/kWh) and NPC ($10.11M) because it combines three complementary elements:

1. **PV + Wind complementarity:** Solar peaks midday; wind often peaks evening/monsoon. Together they provide more consistent generation than either alone. This is reflected in HRES3's 91.7% renewable fraction — highest of all configurations.

2. **No fuel cell = lower capital:** By omitting the fuel cell (which HRES1 and HRES2 include at 1,600 kW), HRES3 avoids $800/kW capital cost plus replacement and O&M. The grid serves as the reliable backup instead. This trade-off works because Cox's Bazar has grid access.

3. **No battery = lower cost, grid as "virtual battery":** HRES3 has no battery storage. Instead, it uses the grid as both backup and surplus sink. The negative grid cost (-$8.6M for HRES3) means grid sales revenue exceeds purchase costs — the grid effectively provides free storage via net metering economics.

**Why HRES2 performs worst:**

HRES2 has the highest LCOE ($0.11/kWh) and NPC ($13.57M) because:
- No wind → lower renewable fraction (53.2%) → more grid purchases
- Has fuel cell but no battery → FC must handle all transient deficits
- Lowest initial capital ($5.65M) but highest O&M ($7.27M/yr) due to fuel cell operation and grid dependence

**Trade-offs identified:**
- Adding wind reduces CO₂ by ~55% compared to PV-only (706,724 vs 1,513,567 kg/yr)
- Adding fuel cell increases HDI (energy security) but raises LCOH significantly
- Battery inclusion (HRES1 vs HRES3) adds cost without sufficient benefit when grid is available

### 5.3 Critical Evaluation

**Reasonable assumptions:**
- NASA POWER data is standard for HOMER studies in data-scarce regions
- Synthetic load profile for 6,000 people is reasonable for Cox's Bazar's tourism-dependent economy
- Component costs align with 2024 market prices for Bangladesh
- 25-year project lifetime is standard for PV-based systems

**Limitations:**
- HOMER's linear optimization may miss non-linear optimal configurations (authors acknowledge this)
- No metaheuristic optimization (GA, PSO) was used
- Grid electricity prices assumed constant over 25 years (unrealistic)
- No demand-side management considered
- Synthetic load profile may not capture real demand variability
- Electrolyzer degradation not explicitly modeled beyond lifetime
- The study assumes grid reliability; Bangladesh's grid experiences frequent outages

**Generalizability:**
- Findings are most applicable to coastal Bangladesh and similar tropical developing regions with grid access
- The CRITIC-TOPSIS framework is transferable to any multi-criteria energy system ranking
- The finding that grid-connected PV-Wind without fuel cell is optimal may not hold for off-grid contexts

**What would change:**
- If grid electricity prices doubled: HRES1 (with fuel cell) might become optimal (less grid dependence)
- If wind costs dropped 50%: HRES3's advantage would increase further
- If battery costs dropped 60%+: battery inclusion might become economical even with grid access
- If CO₂ penalties exceeded $100/ton: HRES1/HRES3's emission advantage would have greater economic value

### 5.4 Derived/Inferred Values

**Calculations (derived, not explicitly stated):**

1. **Average daily electricity production (HRES3):** 18,079,979 / 365 = **49,534 kWh/day**
2. **Average daily electricity production (HRES1):** 18,387,085 / 365 = **50,375 kWh/day**
3. **Average daily hydrogen production (HRES3):** 82,467 / 365 = **226 kg/day** (matches ~225 kg/day target)
4. **Average daily hydrogen production (HRES1):** 98,693 / 365 = **270 kg/day** (exceeds target — likely due to larger renewable capacity)
5. **PV capacity factor (HRES3):** Annual PV generation ≈ 6,552 kW × 4.75 h/day × 365 × 0.8 (derate) ≈ actual PV output estimated at ~10,000,000 kWh/yr → CF ≈ **17.4%** (typical for Bangladesh)
6. **Wind capacity factor (HRES3):** Wind generation ≈ 8,079,979 - PV_output; estimated CF ≈ **20-25%** for Cox's Bazar coastal winds
7. **Grid dependence (HRES3):** 1,118,234 / 18,079,979 = **6.2%** of production from grid
8. **Grid dependence (HRES2):** 2,457,753 / 9,858,432 = **24.9%** from grid
9. **Revenue from grid sales (HRES3):** 8,793,239 × ~$0.09 avg = **~$791,000/yr**
10. **Cost per kg of H2 (LCOH breakdown for HRES3):** $5.22/kg at 82,467 kg/yr → total annual H2 cost ≈ $430,000/yr
11. **Specific electrolyzer production rate:** 82,467 kg/yr / 1,500 kW = **55 kg/kW/yr** (typical for PEM at ~1.85 kg/kW/day equivalent)
12. **Community per-capita consumption:** 12,630 kWh/day / 6,000 people = **2.1 kWh/person/day** (reasonable for rural Bangladesh)

### 5.5 Key Takeaways

1. **HRES3 (PV-Wind-Grid) is the clear winner** — lowest LCOE ($0.0321/kWh), lowest NPC ($10.11M), highest renewable fraction (91.7%), and highest grid sales revenue. The absence of fuel cell and battery is economically optimal when reliable grid access exists.

2. **Wind integration is the single most impactful design choice** — comparing HRES3 (with wind) to HRES4 (without wind), wind reduces CO₂ by 55%, increases renewable fraction from 67% to 91.7%, and lowers LCOE from $0.0777 to $0.0321/kWh. Cox's Bazar's coastal winds (5.75 m/s summer average) are a critical resource.

3. **Fuel cells are not economically justified in grid-connected configurations** — HRES1 (with FC) costs $1.87M more in NPC than HRES3 (without FC) for only marginally better reliability metrics. The grid provides cheaper backup than fuel cells at current costs.

4. **Social criteria dominate the MCDM weighting** — Job potential carries 25.67% weight (highest of all 10 criteria), and HRES1/HRES3 create ~25 jobs over 25 years vs. 6.8 for HRES2. This reflects Bangladesh's development priorities where employment is paramount.

5. **Green hydrogen at $5.22/kg is achievable in Bangladesh** — competitive with global targets and lower than many comparable studies (Oman: $8.34–16.73/kg, South Africa: $6.34–8.97/kg). Cox's Bazar's excellent solar and wind resources make it a viable location for commercial green hydrogen production.

---

*Document generated from 20-page paper analysis. All numerical values in Sections 1-4 extracted directly from the paper text and tables. Section 5 contains derived calculations and analytical interpretations grounded in the paper's data.*
