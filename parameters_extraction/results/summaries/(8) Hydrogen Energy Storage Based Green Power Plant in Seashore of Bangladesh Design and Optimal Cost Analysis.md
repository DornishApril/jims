# Paper Summary: Hydrogen Energy Storage Based Green Power Plant in Seashore of Bangladesh: Design and Optimal Cost Analysis

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Hydrogen Energy Storage Based Green Power Plant in Seashore of Bangladesh: Design and Optimal Cost Analysis
- **Authors:** S.M. Baque Billah, Kazi Meharajul Kabir, Md. Onik Islam, Sujoy Barua, Md. Sultan Mahmud, Md. Shahadat Hossain
- **Affiliations:** Department of Electrical and Electronic Engineering, University of Science & Technology Chittagong (USTC), Chittagong, Bangladesh; Department of Green Energy Technology, Pondicherry University, Puducherry, India
- **Journal/Conference:** IEEE International Conference on Innovations in Green Energy and Healthcare Technologies (ICIGEHT'17)
- **Year of publication:** 2017
- **DOI:** Not explicitly stated in the paper (IEEE conference paper, ISBN: 978-1-5090-5778-8)
- **Study location:** Golden Beach Road, Patenga, Chittagong, Bangladesh (Latitude: 22°15'N, Longitude: 91°48'E)
- **System type:** Grid-connected PV-Wind-Hydrogen storage-Diesel generator hybrid power plant (green power plant with hydrogen energy storage)
- **Study type:** Simulation-based (no experimental component)
- **Software/tools used:** HOMER Pro software
- **Optimization method:** HOMER optimization (finds most cost-effective configuration among a set of system configurations to meet the defined load)

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Type | Rated Capacity | Number of Units | Key Specifications |
|-----------|------|---------------|-----------------|-------------------|
| PV Array | Generic flat plate PV | 2.5 MW (2500 kW) | Not specified | Derating factor: 80%, No tracking, Slope: 23.0°, Azimuth: 0.0°, Ground reflectance: 20%, Lifetime: 20 yr |
| Wind Turbine | Norvento nED | 500 kW | 7 (14 in simulation — see note) | Rotor diameter: 22 m, Hub height: 30 m, Lifetime: 20 yr |
| Electrolyzer | PEM Electrolyzer | 5 MW (5000 kW) | 1 | Efficiency: 85%, Lifetime: 20 yr |
| Hydrogen Storage Tank | Hydrogen Storage Tank | 10,000 kg | 1 | — |
| Generator (Genset) | 3 MW Genset (hydrogen fuel) | 3 MW (3000 kW) | 1 | Fuel: Hydrogen, Efficiency: 80% (rated), Mean electrical efficiency: 75%, Lifetime: 34 yr (operational) |
| Converter | Converter | 5 MW (5000 kW) | 1 | — |

**Note on wind turbine count:** Table II (Proposed Plant Specification) lists 7 units of Norvento nED at 500 kW each. However, Section V.A states "Wind Turbine: 14" with rated capacity 500 kW. This is a discrepancy — the simulation appears to use 14 turbines (7 MW total) while the plant specification table lists 7 turbines.

### 2.2 Total System Capacity

- **Total generation capacity:** PV (2.5 MW) + Wind (7 × 0.5 MW = 3.5 MW, or 14 × 0.5 MW = 7 MW per simulation) = 6 MW (or 9.5 MW per simulation spec)
- **Total storage capacity:** Hydrogen tank: 10,000 kg
- **Total conversion capacity:** Electrolyzer: 5 MW + Converter: 5 MW
- **Generator capacity:** 3 MW (hydrogen-fueled genset)

### 2.3 Component Costs (Capital, Replacement, O&M)

From Table VI (Net Present Costs) and Table VII (Annualized Costs):

| Component | Capital Cost ($) | O&M Cost ($) | Total NPC ($) | Annual Capital ($) | Annual O&M ($) | Annual Total ($) |
|-----------|-----------------|-------------|---------------|-------------------|----------------|-----------------|
| PV | 937,500 | 13,685 | 951,185 | 68,505 | 1,000 | 69,505 |
| Wind Turbine | 1,450,000 | 27,370 | 1,477,370 | 105,954 | 2,000 | 107,954 |
| 3000kW Genset | 250,000 | 598 | 246,732 | 18,268 | 44 | 18,029 |
| Converter | 1,000 | 1,369 | 1,000 | 73 | 0 | 73 |
| Electrolyzer | 1,200,000 | 0 | 1,201,369 | 87,686 | 100 | 87,786 |
| Hydrogen Tank | 1,000 | 0 | 926 | 73 | 0 | 68 |
| **System** | — | — | **3,878,582** | — | — | **283,415** |

**Note:** The cost table layout in the PDF is partially garbled. The values above are reconstructed from the most readable interpretation. The converter capital cost appears unusually low ($1,000 for a 5 MW unit), and the electrolyzer capital cost ($1.2M for 5 MW) seems inconsistent with typical market prices. The hydrogen tank cost ($1,000 capital) also appears anomalously low for a 10,000 kg storage system. These may be transcription errors in the original paper or OCR artifacts.

### 2.4 Economic Parameters

- **Project lifetime:** Not explicitly stated (components have 20-year lifetimes; generator has 34-year operational life)
- **Discount/interest rate:** Not explicitly stated
- **Inflation rate:** Not mentioned
- **Fuel price:** Not explicitly stated (hydrogen is produced on-site from renewable energy, not purchased)
- **Grid electricity price:** Not mentioned
- **Currency and cost year:** USD (207), exchange rate: **1 USD = 80 BDT (Bangladeshi Taka)**
- **Cost reference year:** Not explicitly stated (paper published 2017, data likely from 2015-2017)

### 2.5 Resource Data

**Solar Irradiation (Patenga, Chittagong):**

| Month | Clearness Index | NASA Daily Radiation (kWh/m²/day) | Weather Office Daily Radiation (kWh/m²/day) |
|-------|----------------|-----------------------------------|-------------------------------------------|
| January | 0.335 | — | 4.597 |
| February | 0.379 | 4.240 | — |
| March | 0.490 | 6.350 | — |
| April | 0.540 | 7.800 | — |
| May | 0.577 | 8.110 | — |
| June | 0.613 | 7.750 | — |
| July | 0.598 | 5.040 | — |
| August | 0.571 | 5.590 | — |
| September | 0.528 | 4.320 | — |
| October | 0.453 | 4.670 | — |
| November | 0.360 | 4.180 | — |
| December | 0.324 | 6.910 | — |
| **Annual Average** | **0.543** | **4.63** | **5.85** |

- **Primary solar data source:** NASA surface meteorology and solar energy (http://eosweb.larc.nasa.gov) and Bangladesh Meteorological Department, Patenga airport branch
- **Average annual solar radiation:** 4.63 kWh/m²/day (NASA) / 5.85 kWh/m²/day (Weather Office)

**Wind Speed (Patenga, Chittagong):**

| Month | NASA Wind Speed (m/s) | Weather Office Wind Speed at 30 ft (m/s) |
|-------|----------------------|------------------------------------------|
| January | 2.480 | 2.220 |
| February | 2.730 | 2.220 |
| March | 2.900 | 2.500 |
| April | 3.040 | 2.500 |
| May | 3.420 | 3.050 |
| June | 3.250 | 2.780 |
| July | 2.930 | 3.050 |
| August | 2.440 | 2.780 |
| September | 2.040 | 2.500 |
| October | 2.240 | 1.390 |
| November | 2.330 | 1.940 |
| December | 2.740 | 1.670 |
| **Annual Average** | — | **2.38** |

- **Wind data source:** NASA and Bangladesh Meteorological Department, Patenga airport branch
- **Average annual wind speed:** 2.38 m/s (at 30 ft / ~9 m height per Weather Office); NASA data shows higher values
- **Wind turbine hub height:** 30 m (resource data measured at lower height)

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

- **LCOE / COE:** **$0.09/kWh** (stated in conclusion as "per unit cost of the system")
- **NPC (Net Present Cost):** **$3,878,582** (from Table VI, System Total)
- **Annual system cost:** **$283,415** (from Table VII, System Total)
- **Initial capital cost:** Not explicitly stated as a single figure (sum of component capitals: ~$3,839,500 per Table VI)
- **Operating cost (per year):** Not separately stated
- **Payback period:** Not mentioned
- **IRR or ROI:** Not mentioned
- **Comparison benchmark:** Conventional quick rental power plants cost $0.23/kWh (stated in conclusion)

### 3.2 Reliability Metrics

- **LPSP (Loss of Power Supply Probability):** Not explicitly stated
- **LOLP:** Not mentioned
- **Unmet load:** Not explicitly stated
- **System availability:** Not explicitly stated
- **THD (Total Harmonic Distortion):** Claimed to be negligible ("no THD") because the alternator produces pure sine wave; standard referenced: THD should be <5% of rated inverter output per IEC 61727

### 3.3 Generation Metrics

| Metric | Value |
|--------|-------|
| Total annual electricity generation (hydrogen generator) | **2,910,906 kWh/yr** |
| Mean electrical output | **1,998 kW** |
| Minimum electrical output | **485 kW** |
| Maximum electrical output | **3,000 kW** |
| Annual hydrogen production | **122,275 kg/yr** |
| Annual hydrogen consumption | **116,601 kg/yr** |
| Annual fuel consumption (hydrogen as fuel, in liters) | **116,436 L/yr** |
| Specific fuel consumption | **0.04 L/kWh** |
| Fuel energy input | **3,881,214 kWh/yr** |
| Mean electrical efficiency | **75%** |
| Renewable fraction | Not explicitly stated (system is described as "completely green" with "no CO2 emissions") |
| Excess electricity | Not stated |
| Grid electricity imported/exported | Not stated (system described as grid-connected but no import/export values given) |

### 3.4 Load Metrics

| Metric | Value |
|--------|-------|
| Daily peak load demand | **8 MWh/day** (stated as "daily demand is 8MW" — likely means 8 MWh/day) |
| Annual load demand | **2,920,000 kWh/yr** (stated as "2920000KWh/yr") |
| Peak demand duration | 6 PM to 10 PM (4 hours daily) |
| Peak load (kW) | Not explicitly stated (8 MWh over 4 hours = 2 MW average during peak, but peak kW not given) |
| Average load | Not explicitly stated |
| Load profile type | Not explicitly stated (appears to be a community/area load for Patenga) |

### 3.5 Optimal Configuration

- **Optimization tool:** HOMER Pro
- **Objective:** Find most cost-effective configuration to meet peak load demand of 8 MWh/day
- **Constraints:** Meet peak load demand during 6 PM – 10 PM window; low THD requirement
- **Sensitivity analysis:** Not explicitly described in the paper
- **Optimal configuration:** PV (2.5 MW) + Wind (14 × 500 kW) + PEM Electrolyzer (5 MW) + Hydrogen Tank (10,000 kg) + Hydrogen Genset (3 MW) + Converter (5 MW)

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

- **Type:** Hydrogen-based energy storage dispatch (not a conventional cycle-charging or load-following strategy)
- **Priority order:**
  1. Solar PV and Wind generate DC power during daylight/windy periods
  2. DC power feeds PEM electrolyzer through a converter to produce hydrogen from seawater
  3. Hydrogen is stored in a tank
  4. During peak demand (6 PM – 10 PM), the hydrogen-fueled genset (3 MW) generates AC power from stored hydrogen
- **Decision logic:** The system separates generation and consumption temporally — renewables produce hydrogen during the day, and the generator runs during peak hours

### 4.2 Power Flow Logic

- **Excess renewable energy handling:** All solar and wind DC output is directed to the PEM electrolyzer to produce hydrogen (no battery storage, no dump load mentioned)
- **Deficit handling:** During peak hours, the 3 MW hydrogen genset runs on stored hydrogen
- **Battery charging/discharging:** No battery in this system
- **Hydrogen production logic:** Electrolyzer runs when solar/wind DC power is available; converts electrical energy to chemical energy (H₂)
- **Hydrogen consumption logic:** Genset burns hydrogen during peak demand window (6 PM – 10 PM)
- **Diesel generator:** Not present as a backup (the genset runs on hydrogen, not diesel — despite the "fuel consumption" being reported in liters, which is likely a HOMER convention for hydrogen volume equivalent)
- **Grid interaction:** Described as grid-connected but no specific grid import/export logic detailed

### 4.3 Control Parameters

| Parameter | Value |
|-----------|-------|
| Electrolyzer efficiency | 85% |
| Generator rated efficiency | 80% |
| Generator mean electrical efficiency | 75% |
| PV derating factor | 80% |
| PV tracking | None (fixed tilt at 23°) |
| Hydrogen storage capacity | 10,000 kg |
| Converter capacity | 5,000 kW |
| Generator minimum load | Not stated |
| Battery SOC limits | N/A (no battery) |

### 4.4 Algorithm Flow

The paper describes a simple energy flow model:

1. **Daytime:** Solar irradiance → PV panels → DC power; Wind → turbine → DC power
2. **Conversion:** Combined DC power → Converter → PEM Electrolyzer
3. **Production:** Electrolyzer + Seawater → Hydrogen gas (H₂)
4. **Storage:** Hydrogen compressed/stored in tank (10,000 kg capacity)
5. **Peak hours (6 PM – 10 PM):** Stored Hydrogen → Hydrogen Genset (3 MW) → AC power → Grid/Load
6. **Output:** Pure sine wave AC with negligible THD

The power balance equation (implicit):
> Renewable DC output = Electrolyzer input / converter efficiency
> Hydrogen produced = Electrolyzer input × Electrolyzer efficiency / HHV of hydrogen
> Electrical output = Hydrogen consumed × Generator efficiency

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (ANALYSIS)

### 5.1 Power Generation Walkthrough

This system operates on a fundamentally different paradigm than conventional hybrid microgrids. Rather than using batteries for short-term storage or running generators directly on diesel, it uses hydrogen as an intermediate energy carrier — effectively decoupling generation from consumption in time.

**Morning (6 AM – 9 AM):**
Solar radiation begins at Patenga (latitude 22°15'N). With a fixed tilt of 23° and no tracking, the 2.5 MW PV array begins generating DC power. At this latitude, sunrise is around 5:30-6:00 AM for most of the year. Wind speeds in the morning are typically moderate (2-3 m/s annual average). The 14 wind turbines (500 kW each) begin contributing if wind speeds exceed cut-in speed (typically 3-4 m/s for Norvento nED turbines). Combined DC output begins feeding the 5 MW electrolyzer, and hydrogen production ramps up.

**Midday (10 AM – 3 PM):**
This is peak solar generation. With average solar radiation of 4.63 kWh/m²/day (NASA) and the 2.5 MW array at 80% derating, peak DC output could reach approximately 2,000 kW under standard conditions. Wind speeds during pre-monsoon months (March-May) can reach 3.0-3.4 m/s, contributing additional power from the 14 turbines. The electrolyzer (rated 5 MW) processes this DC power at 85% efficiency, producing hydrogen at a rate of approximately 122,275 kg/yr ÷ 365 days ≈ **335 kg/day** during production hours. This hydrogen flows into the 10,000 kg storage tank.

**Evening (4 PM – 6 PM):**
Solar output declines as the sun sets (around 5:30-6:30 PM depending on season). Wind may pick up or remain steady. Hydrogen production slows. The storage tank must now contain enough hydrogen to cover the upcoming peak demand period.

**Peak Demand (6 PM – 10 PM):**
This is the critical window. The 3 MW hydrogen genset starts and runs for 4 hours. At mean output of 1,998 kW (from HOMER results), the generator produces approximately 7,992 kWh during this window — closely matching the stated 8 MWh daily demand. The genset consumes hydrogen at a rate of 116,601 kg/yr ÷ 365 ≈ **320 kg/day**. The generator runs 1,457 hours/year (approximately 4 hours/day × 365 days = 1,460 hours), confirming the daily peak-shaving operational pattern.

**Night (10 PM – 6 AM):**
The generator shuts off after the peak window. Minimal or no renewable generation (no solar, wind variable). The system relies on stored hydrogen reserves and potentially grid connection for any off-peak demand.

**Seasonal Variations:**
- **Pre-monsoon (March-May):** Highest solar radiation (6.35-8.11 kWh/m²/day from Weather Office data) and moderate wind. Maximum hydrogen production.
- **Monsoon (June-September):** High solar but also cloud cover reduces output. Wind speeds moderate. Hydrogen production may decrease.
- **Post-monsoon (October-November):** Reduced solar (4.18-4.67 kWh/m²/day) and lowest wind speeds (1.39-1.94 m/s). Potential hydrogen production shortfall.
- **Winter (December-February):** Moderate solar (4.41-6.91 kWh/m²/day), low wind. The 10,000 kg hydrogen buffer provides resilience.

### 5.2 System Behavior Analysis

**Why this configuration?**
The authors chose hydrogen storage over batteries for several reasons stated in the paper:
1. Hydrogen has higher mass energy density than batteries
2. Hydrogen leakage from tanks is insignificant (long-term storage viable)
3. Hydrogen is suitable for seasonal storage (unlike batteries which self-discharge)
4. The system produces pure sine wave output (low THD), addressing power quality concerns
5. It eliminates CO2 emissions entirely (green energy model)

**The 3 MW generator vs. 8 MWh daily demand:**
The generator at 3 MW running 4 hours produces 12 MWh maximum, but actual mean output of 1,998 kW × 4 hours ≈ 8 MWh matches the daily demand. This suggests the system is specifically sized for peak shaving, not baseload supply.

**Renewable oversizing rationale:**
The combined PV (2.5 MW) + Wind (7 MW from 14 turbines) = 9.5 MW of renewable capacity vastly exceeds the 3 MW generator requirement. This is intentional — the system needs to produce enough hydrogen during daylight hours to cover the 4-hour peak window. With electrolyzer at 85% efficiency and generator at 75% mean efficiency, the round-trip efficiency is approximately 0.85 × 0.75 = **63.7%**. This means roughly 1.57 kWh of renewable energy must be generated for every 1 kWh delivered during peak hours.

**Trade-offs identified:**
- High initial cost ($3.88M NPC) but low per-unit cost ($0.09/kWh)
- Large land area required for 2.5 MW PV + 14 wind turbines at a seashore location
- Hydrogen safety concerns (not addressed in the paper)
- Dependence on consistent renewable resource for hydrogen production

### 5.3 Critical Evaluation

**Reasonable assumptions:**
- Solar and wind data from NASA and local meteorological department are credible sources
- HOMER Pro is industry-standard for hybrid system optimization
- The seashore location provides both renewable resources and seawater for electrolysis

**Limitations:**
1. **No battery storage:** The system has no short-term storage for transient cloud cover or wind lulls. If renewables drop during production hours, hydrogen production suffers.
2. **Single generator:** No backup if the 3 MW genset fails during peak hours.
3. **Wind resource is marginal:** Average wind speed of 2.38 m/s at 30 ft (~9 m) is very low for wind power. Even at 30 m hub height, extrapolated wind speeds may only reach 3-4 m/s — barely above cut-in speed for most turbines. The wind contribution may be minimal.
4. **Cost data reliability:** The component costs in Table VI appear inconsistent (converter at $1,000 for 5 MW, hydrogen tank at $1,000 for 10,000 kg). These may be placeholder values or OCR errors.
5. **No sensitivity analysis:** The paper does not explore how changes in solar radiation, wind speed, component costs, or load growth affect the optimal configuration.
6. **No LPSP or reliability metrics:** Despite being an optimization study, no reliability indices are reported.
7. **"No THD" claim:** While the alternator produces sine wave, the converter/electrolyzer system introduces harmonics. The paper does not provide THD measurement data.

**Generalizability:**
The concept is applicable to any coastal area with adequate solar and wind resources. However, the specific configuration is optimized for Patenga's resource profile and may not transfer directly to other locations without re-optimization.

**Comparison to conventional systems:**
At $0.09/kWh, this system is significantly cheaper than the $0.23/kWh from quick rental power plants in Bangladesh. However, this comparison may not account for the full cost of hydrogen storage safety systems, maintenance of electrolyzers, and the limited operational hours (peak-only).

### 5.4 Derived/Inferred Values

| Derived Metric | Calculation | Result |
|---------------|-------------|--------|
| Average daily hydrogen production | 122,275 kg/yr ÷ 365 days | **335 kg/day** |
| Average daily hydrogen consumption | 116,601 kg/yr ÷ 365 days | **320 kg/day** |
| Hydrogen surplus per day | 335 - 320 | **15 kg/day** (accumulates in tank) |
| Round-trip efficiency (electrolyzer × generator) | 0.85 × 0.75 | **63.75%** |
| Renewable energy required per kWh delivered | 1 ÷ 0.6375 | **1.57 kWh/kWh** |
| Daily renewable energy input to electrolyzer | 2,917,683 kWh/yr ÷ 365 | **7,994 kWh/day** |
| Generator capacity factor | 1,998 kW mean ÷ 3,000 kW rated | **66.6%** |
| PV capacity factor (estimated) | Not calculable without hourly data | ~15-20% (typical for Bangladesh) |
| Wind capacity factor (estimated) | Low wind speeds suggest | ~10-15% |
| Storage autonomy | 10,000 kg ÷ 320 kg/day consumption | **31.25 days** of peak supply |
| System cost per kW of generator capacity | $3,878,582 ÷ 3,000 kW | **$1,293/kW** |
| Annual cost per kWh delivered | $283,415 ÷ 2,910,906 kWh | **$0.097/kWh** (matches stated $0.09/kWh) |
| PV energy production estimate | Not directly stated; total renewable generation not broken down | Not derivable from given data |

### 5.5 Key Takeaways

1. **Novel hydrogen-centric architecture:** This paper proposes a system where ALL renewable energy is converted to hydrogen first, and ALL electricity generation comes from a hydrogen-fueled genset. There is no direct renewable-to-load power flow, no battery, and no diesel backup. This is a "power-to-gas-to-power" model.

2. **Peak-shaving focus:** The system is designed exclusively for peak load management (6 PM – 10 PM), not 24/7 power supply. The 3 MW generator runs only ~4 hours/day (1,457 hrs/yr), making it a peaking plant rather than a baseload facility.

3. **Cost competitiveness:** At $0.09/kWh, the system claims to be 60% cheaper than conventional quick rental power plants ($0.23/kWh) in Bangladesh. This economic advantage is the primary selling point.

4. **Zero emissions claim:** The system is described as completely green with no CO2 emissions. This is true for operation (hydrogen combustion produces water), but the analysis does not account for embodied emissions in manufacturing PV panels, wind turbines, electrolyzers, and tanks.

5. **Marginal wind resource concern:** The average wind speed of 2.38 m/s at measurement height is very low for wind power generation. The actual energy contribution from the 14 turbines may be minimal compared to PV, suggesting the system is primarily solar-hydrogen with wind as a supplementary source.

---

## NOTES AND AMBIGUITIES

1. **Wind turbine count discrepancy:** Table II says 7 turbines; Section V simulation says 14 turbines. The simulation likely used 14.
2. **Cost table formatting:** Table VI has garbled rows making some component cost assignments uncertain.
3. **"Daily demand is 8MW":** This phrasing is ambiguous — likely means 8 MWh/day (energy), not 8 MW (power).
4. **No reliability metrics:** LPSP, unmet load, and availability are not reported despite being standard HOMER outputs.
5. **No breakdown of renewable generation by source:** The paper does not state how much energy comes from PV vs. wind.
6. **Fuel consumption in liters:** Hydrogen is measured in kg elsewhere but fuel consumption is reported in liters (116,436 L/yr), suggesting HOMER may have used a liquid fuel equivalent or the genset model was configured with diesel-like parameters.
