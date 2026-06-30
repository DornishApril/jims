# Paper Summary: Article 37.pdf

---

## SECTION 1: PAPER IDENTIFICATION (STRICT EXTRACTION)

- **Full paper title:** Optimal design and energy management of a hybrid PV-Wind system with hydrogen and gravity energy storage: An off-grid sustainable alternative for coal power in Morocco
- **Authors:** Mohammed Sahab, Anisa Emrani, Mohammad J. Sanjari, Jamil Abdelmajid, Asmae Berrada
- **Journal/Conference name:** Renewable Energy Focus
- **Year of publication:** 2025 (available online 30 October 2025)
- **DOI:** 10.1016/j.ref.2025.100775
- **Study location:** Safi, Morocco (replacing a 624 MW ultra-supercritical coal-fired power plant)
- **System type:** Off-grid PV-Wind-Hydrogen-GES hybrid microgrid (PV + Wind Turbines + Electrolyzer + Hydrogen Tank + Fuel Cell + Gravity Energy Storage)
- **Study type:** Simulation-based (8760-hour dispatch simulation with simultaneous optimization)
- **Software/tools used:** MATLAB (Optimization Toolbox — Fmincon solver with MultiStart)
- **Optimization method used:** Fmincon nonlinear programming solver (interior-point algorithm) with MultiStart for robustness to local minima. Seven design variables: PV capacity, wind capacity, electrolyzer power, fuel cell power, hydrogen tank capacity, GES diameter, GES height.

---

## SECTION 2: SYSTEM CONFIGURATION — EXACT EXTRACT (STRICT EXTRACTION)

### 2.1 Component List and Capacities

| Component | Model/Type | Rated Capacity | Number of Units | Key Specifications |
|-----------|-----------|---------------|-----------------|-------------------|
| PV Array | SunPower Maxeon 6 (SPR-MAX6-440-COM) | 440 W per panel | ~1005 units (total ~0.45 MW) | Monocrystalline IBC, 22.8% efficiency, 1762×1046×35 mm, temp coefficient k=−0.0029/°C |
| Wind Turbines | Vestas V164-9.5 MW | 9.5 MW per turbine | ~594 units (total ~1.88 GW) | Cut-in: 3 m/s, Rated: 13 m/s, Cut-out: 25 m/s, Rotor diameter: 164 m, Swept area: 21,124 m² |
| Electrolyzer | Alkaline | 790 MW | 1 (aggregate) | 77% efficiency (HHV basis), lifetime >80,000 hours |
| Fuel Cell | PEMFC | 650 MW | 1 (aggregate) | 60% efficiency, lifetime: 10 years |
| Hydrogen Tank | Gaseous storage | 260 tonnes | 1 | Storage pressure: 200–350 bar, lifetime: 25 years |
| Gravity Energy Storage (GES) | Piston-water hydrostatic | 37.9 MW power rating | 1 | Diameter: 5.19 m, Height: 714.96 m, round-trip efficiency: 80–85% |
| Inverter | DC-AC converter | Not explicitly stated | — | For PV array (DC output → AC) |

### 2.2 Total System Capacity

- **Total generation capacity:** ~1.88 GW wind + ~0.45 MW PV + 650 MW FC = ~1.88 GW (wind dominates)
- **Total storage capacity:** 260 tonnes hydrogen + GES (37.9 MW power, energy capacity depends on piston mass/height)
- **Total conversion capacity:** 790 MW electrolyzer + inverter (capacity not stated)

### 2.3 Component Costs (Capital, Replacement, O&M)

| Component | Capital Cost | Replacement Cost | O&M Cost | Lifetime |
|-----------|-------------|-----------------|----------|----------|
| Electrolyzer | **1000 $/kW** | Not stated | **14.48 $/kW/year** | 20 years |
| Fuel Cell | **600 $/kW** | **600 $/kW** | **13.43 $/kW/year** | 10 years |
| Hydrogen Tank | **376.4 × 1.15 = $432.86/kg** | Not stated | **2% of CapEx** | 25 years |
| Wind Turbines | **$2,850,000 per turbine** | Not stated | **3% of CapEx** | 25 years |
| PV Panels | **$765 per panel** | Not stated | **1% of CapEx** | 25 years |
| GES | **0.56 $/Wp** | Not considered | **1% of CapEx** | 25 years |

- **Salvage cost (PV):** $440/kW
- **Salvage cost (H2 Tank):** $193.23/kg
- **GES disposal/recycling:** Not considered (lack of demonstration plants)

### 2.4 Economic Parameters

| Parameter | Value |
|-----------|-------|
| Discount rate (r) | **6%** |
| Project lifetime | **25 years** |
| Inflation rate | Not reported |
| Fuel price | Not applicable (no diesel generator) |
| Grid electricity price | Not applicable (off-grid system) |
| Currency and cost year | USD (year not explicitly stated, assumed ~2023–2025) |

### 2.5 Resource Data

| Resource | Value | Source |
|----------|-------|--------|
| Solar irradiation | **~1,850–1,950 kWh/m²/year** (peak up to 1,200 W/m²) | PVGIS (European Commission) |
| Wind speed | **Average 6–8 m/s** (range 2–15 m/s) | PVGIS |
| Temperature | **15°C to 38°C** (seasonal/daily cycles) | PVGIS |
| Data source | European Commission PVGIS (satellite + reanalysis, validated against ground stations) |
| Temporal resolution | Hourly, 8,760 hours (full year) |

---

## SECTION 3: KEY PERFORMANCE RESULTS — EXACT EXTRACT (STRICT EXTRACTION)

### 3.1 Cost Metrics

| Metric | Value |
|--------|-------|
| **LCOE** | **0.239 €/kWh** (≈ 0.23 €/kWh rounded in text) |
| NPC | Not explicitly stated in € (coal LCOE benchmark: $0.18–0.34/kWh) |
| Initial capital cost | Not explicitly stated as a single figure |
| Operating cost | Not explicitly stated as annual figure |
| Payback period | Not reported |
| IRR/ROI | Not reported |

### 3.2 Reliability Metrics

| Metric | Value |
|--------|-------|
| **LPSP** | **0%** (target and achieved) |
| Unmet load | 0 kWh/year (by design at LPSP=0%) |
| System availability | 100% (LPSP = 0%) |

### 3.3 Generation Metrics

| Metric | Value |
|--------|-------|
| Total annual generation | Not explicitly stated as single figure |
| PV generation | Peak output ~4–5.5 MW (from Fig. 9) |
| Wind generation | Peaks approaching 7–8 GW (from Fig. 10) |
| Fuel cell output | Peaks at 600–650 MW (from Fig. 14) |
| GES discharge | Bursts complementing renewable drops |
| Renewable fraction | ~100% (no fossil fuel; FC runs on green H2) |
| Excess electricity | Present (spikes up to ~8 GW vs ~0.6–1.0 GW load) |
| Hydrogen production | Peaks at ~1 tonne per time step (Fig. 12) |
| Hydrogen consumption | Plateaus around 2.5–3 tonnes, declining to ~1.5 tonnes |
| Diesel consumption | Not applicable (no diesel generator) |
| Grid import/export | Not applicable (off-grid) |

### 3.4 Load Metrics

| Metric | Value |
|--------|-------|
| Total annual load demand | Not explicitly stated as single figure |
| Average load | **~550–580 MW** (mean) |
| Peak load | **~624–650 MW** (upper capacity limit) |
| Minimum load | **~450 MW** (lowest troughs) |
| Load variability | **150–200 MW** within short intervals |
| Load profile type | Industrial/utility-scale (coal plant replacement) |

### 3.5 Optimal Configuration

| Variable | Optimal Value |
|----------|--------------|
| Number of PV modules | **1005.268 units** |
| Number of Wind turbines | **594.093 units** |
| GES Height | **714.964 m** |
| GES Diameter | **5.190 m** |
| Electrolyzer power | **790 MW** |
| Fuel cell nominal power | **650 MW** |
| Hydrogen tank mass | **2.60 tonnes** |
| Minimum LCOE | **0.239 €/kWh** |

- **Objective function:** Minimize COE (Cost of Energy) using Life-Cycle Cost Analysis (LCCA)
- **Constraints:** LPSP = 0% (hard reliability constraint)
- **Sensitivity analysis:** One-at-a-time ±5% perturbation around baseline for 7 design variables
- **Convergence:** Achieved after ~180 iterations, ~2.5 hours runtime

---

## SECTION 4: POWER GENERATION ALGORITHM — EXACT EXTRACTION (STRICT EXTRACTION)

### 4.1 Dispatch Strategy

- **Type:** Priority-based rule-based dispatch with simultaneous optimization
- **Priority order (surplus):** GES charging first → Electrolyzer second → Curtailment only if both at limits
- **Priority order (deficit):** GES discharge first → Fuel cell second → If H2 tank below minimum, LPSP counted
- **Decision logic:** At each hour, compute PB(t) = (PV + Wind) − Load
  - If PB(t) = 0: exact match, no storage action
  - If PB(t) > 0: surplus → charge GES first, remaining to electrolyzer
  - If PB(t) < 0: deficit → discharge GES first, then fuel cell
- **Constraints:** GES SOC limits, H2 tank min/max, component rated power limits
- **Deadband:** Small deadband prevents rapid toggling
- **Reserve margin:** Configurable reserve margin on GES/FC for short fluctuations

### 4.2 Power Flow Logic

- **Excess renewable energy handling:** First charges GES (lifts piston), then powers electrolyzer (produces H2). Curtailment only if both storage systems at capacity.
- **Deficit handling:** GES discharges first (piston descends, generates electricity), then fuel cell runs on stored hydrogen. If H2 tank drops below minimum threshold, system cannot meet demand (LPSP counted).
- **Battery charging/discharging:** No battery in this system (GES replaces battery)
- **Hydrogen production logic:** Electrolyzer runs only after GES is fully charged. Production rate = min(PElz_rated, available_surplus_after_GES) × ηelz. H2 tank constrained between Emin_tank and Emax_tank.
- **Hydrogen consumption logic:** Fuel cell draws from H2 tank when GES alone cannot cover deficit. PFC(t) = ηFC × PTank-FC(t).
- **Diesel generator:** Not present in this system.
- **Grid interaction:** None (off-grid system).

### 4.3 Control Parameters

| Parameter | Value |
|-----------|-------|
| Electrolyzer efficiency (ηelz) | **77%** (HHV basis) |
| Fuel cell efficiency (ηFC) | **60%** |
| GES round-trip efficiency | **80–85%** |
| GES SOC minimum | **~0%** (fully discharged) |
| GES SOC maximum | **~80–100%** (frequently at 80–95%) |
| H2 tank minimum | Emin_tank (not numerically stated) |
| H2 tank maximum | Emax_tank (not numerically stated) |
| H2 higher heating value | **39.7 kWh/kg** |
| Wind turbine cut-in speed | **3 m/s** |
| Wind turbine rated speed | **13 m/s** |
| Wind turbine cut-out speed | **25 m/s** |
| PV temperature coefficient | **−0.0029 /°C** |
| PV STC temperature | **25°C** |
| PV STC irradiance | **1000 W/m²** |
| Device-level control timescale | Millisecond-to-second |
| EMS timescale | Hourly (8760 steps) |

### 4.4 Algorithm Flow

1. **Hourly power balance:** Compute PB(t) = P_PV(t) + P_WT(t) − P_load(t)
2. **If PB(t) > 0 (surplus):**
   - Charge GES: Pch(t) = min(PB(t), GES_max_charge_power)
   - Remaining surplus: Pb(t) − Pch(t) → Electrolyzer
   - H2 production: PH2(t) = min(Emax_tank − Etank(t−1), min{Pb(t)−Pch(t), PElz}) × ηelz
   - Update H2 tank: Etank(t) = Etank(t−1) + PH2(t)
3. **If PB(t) < 0 (deficit):**
   - Discharge GES: Pdisch(t) = min(|PB(t)|, GES_max_discharge_power)
   - Remaining deficit: |PB(t)| − Pdisch(t) → Fuel cell
   - FC output: PFC(t) = ηFC × PTank-FC(t)
   - Update H2 tank: Etank(t) = Etank(t−1) − PH2_consumed(t)
   - If Etank < Emin_tank: count as unmet load (LPSP contribution)
4. **If PB(t) = 0:** No storage action needed.
5. **Annual LPSP calculation:** LPSP = Σ(unmet_power) / Σ(total_load) over 8760 hours.

**Power balance equation:**
P_PV(t) + P_WT(t) + P_FC(t) + P_GES_disch(t) − P_EL(t) − P_GES_ch(t) = P_load(t)

---

## SECTION 5: ANALYTICAL INSIGHT AND SYSTEM EXPLANATION (YOUR ANALYSIS)

### 5.1 Power Generation Walkthrough

This system is designed to replace a 624 MW coal plant — a massive load by renewable standards. The average demand hovers around 550–580 MW, with peaks reaching 650 MW and troughs dipping to 450 MW. To meet this with near-zero LPSP, the system is enormously oversized: 594 wind turbines (nameplate ~5.6 GW) plus PV (~0.45 MW) produce peak outputs of 7–8 GW, far exceeding the ~1 GW peak load. This oversizing is deliberate — it ensures that even during low-resource hours, enough energy is captured and stored.

**Morning (sunrise, ~6–9 AM):** Solar irradiance ramps from zero. PV output climbs toward its 4–5 MW peak. Wind may or may not be available (the paper shows wind is highly variable, with spikes at any hour). If PV + Wind < Load, GES discharges first to cover the morning ramp. The GES, which typically sits at 80–95% SOC overnight, can respond within seconds. If GES alone is insufficient, the fuel cell ramps up, drawing hydrogen produced during previous surplus periods.

**Midday (10 AM–2 PM):** Solar peaks at 4–5 MW. Combined with wind (which can spike to 7–8 GW during strong periods), generation massively exceeds the ~550 MW average load. The surplus follows a strict hierarchy: first, GES charges (piston lifts, storing gravitational potential energy). Once GES reaches capacity, the remaining surplus powers the 790 MW electrolyzer, producing hydrogen at up to ~1 tonne per hour. The hydrogen tank (260 tonnes capacity) accumulates stored energy for long-duration deficits.

**Evening (4–7 PM):** Solar drops rapidly. Load often peaks near 600–650 MW as demand surges. The deficit is covered by GES discharge (fast response, seconds) and fuel cell (moderate response, minutes). The fuel cell operates at 500–650 MW during these transition periods. Hydrogen consumption increases as the fuel cell draws down the tank.

**Night (8 PM–6 AM):** Zero PV. Wind becomes the primary generation source. The paper shows wind output is highly variable at night — sometimes near zero, sometimes spiking to several GW. GES handles the high-frequency fluctuations (deep cycling between 0% and 80–95% SOC), while the fuel cell provides steady baseload during prolonged low-wind periods. The GES frequently reaches near-0% SOC, indicating it is heavily utilized as the primary short-term buffer.

**Seasonal variations:** The paper notes seasonal complementarity between solar and wind in Morocco (Fig. 6). Summer brings peak solar but potential calms; winter brings stronger winds but lower solar irradiation. The 260-tonne hydrogen tank provides seasonal storage — hydrogen accumulated during high-resource periods is consumed during extended low-resource periods. The fuel cell operates "intermittently at high power" particularly when wind and PV both dip simultaneously.

**Concrete numbers from the paper:**
- With 1005 PV panels at 440 W each (~0.45 MW total), peak PV output is ~4–5 MW (capacity factor ~10–12% of nameplate at peak, consistent with ~1,850–1,950 kWh/m²/year irradiation).
- With 594 Vestas V164-9.5 MW turbines, peak wind output reaches 7–8 GW (well above nameplate × count, suggesting the figure shows instantaneous fleet-wide output during strong wind events).
- The GES (37.9 MW, 714 m height, 5.19 m diameter) cycles frequently between 0% and 80–95% SOC, handling intra-day imbalances.
- The electrolyzer (790 MW) and fuel cell (650 MW) are sized to handle the majority of the load during renewable droughts, with hydrogen as the energy carrier.

### 5.2 System Behavior Analysis

**Why this configuration is optimal:** The optimizer (Fmincon) found that wind dominates the generation mix (1.88 GW vs 0.45 MW PV) because Morocco's coastal wind resource (6–8 m/s average) is more consistent and higher-capacity-factor than solar. PV contributes only ~0.02% of total generation capacity — it is essentially a minor supplement. This is unusual for hybrid systems but reflects the specific load profile (550+ MW continuous) and the availability of superior wind resources at the Safi site.

**Renewable penetration and storage sizing:** At LPSP = 0%, the system must survive the worst-case 8760-hour meteorological year without any load loss. This requires massive overbuilding: ~5.6 GW of wind nameplate to reliably deliver ~550 MW average. The storage (790 MW electrolyzer + 650 MW FC + 260 t H2 + GES) is sized to bridge the longest renewable drought in the dataset. The paper notes that relaxing LPSP to just 1% would significantly reduce costs — the last 1% of reliability is extremely expensive.

**Dispatch strategy impact on component lifetimes:** The priority dispatch (GES first, FC second) is explicitly designed to protect the fuel cell and electrolyzer from high-frequency cycling. GES handles the rapid charge/discharge cycles (it can respond in seconds and has a 50+ year cycle life), while the fuel cell operates less frequently at high power. This extends FC stack life and reduces replacement costs. The paper notes that FC stack replacement is a major cost driver (lifetime only 10 years vs 25 for other components).

**Trade-offs identified:**
- Reliability vs. cost: LPSP = 0% yields LCOE = 0.239 €/kWh; relaxing to 5% LPSP would reduce LCOE significantly
- Wind vs. PV: Wind dominates due to superior capacity factor at this location
- GES vs. Hydrogen: GES handles short-term (seconds to hours), hydrogen handles long-term (days to seasons)
- Capital intensity: Wind turbines and electrolyzers dominate total investment

**Edge cases:** The paper does not explicitly model multi-day extreme weather events beyond the single meteorological year. The 260-tonne hydrogen tank provides buffer for extended low-wind/low-solar periods, but the exact autonomy duration is not stated. Load growth is not modeled — the system is sized for the current coal plant load profile.

### 5.3 Critical Evaluation

**Reasonableness of assumptions:**
- The assumption of LPSP = 0% is extremely conservative. Real-world microgrids typically accept 1–5% LPSP for significant cost savings.
- The alkaline electrolyzer efficiency of 77% (HHV) is realistic for current commercial systems.
- The GES geometry (714 m height, 5.19 m diameter) is within modern shaft-sinking capabilities but represents a significant civil engineering challenge.
- The assumption of no battery storage is notable — GES replaces batteries entirely, which is optimistic given GES is less commercially mature.

**Limitations acknowledged by the authors:**
1. Hourly resolution omits fast transient dynamics (sub-second frequency regulation)
2. Component degradation simplified to cost assumptions (not explicitly simulated)
3. Grid dynamics not represented (assumed islanded load)
4. Hydrogen compression energy, leakage, and safety engineering simplified
5. No experimental validation of full-scale GES or integrated H2-GES systems

**Generalizability:** The findings are most applicable to coastal Morocco or similar regions with strong wind resources and high solar irradiation. The specific cost structure (wind-dominated, PV nearly irrelevant) may not transfer to regions with different resource profiles. The LCOE of 0.23 €/kWh is competitive with coal ($0.18–0.34/kWh) but higher than some PV-WT-H2 systems with relaxed reliability (e.g., 0.091 $/kWh at 5% LPSP in Xu et al.).

**What would change with different parameters:**
- Higher wind capacity factor → fewer turbines needed → lower LCOE
- Lower discount rate → lower LCOE (sensitivity shows ±5% in r changes LCOE by ≈∓2.2%)
- Relaxed LPSP → significantly lower component sizes and costs
- Higher electrolyzer cost → optimizer would favor GES over hydrogen storage

**Comparison to similar systems:** The paper's LCOE (0.23 €/kWh) is higher than PV-WT-H2 without GES (0.091 $/kWh at 5% LPSP) and PV-WT-H2-battery (0.145 $/kWh at ~95% reliability). The cost premium is attributable to the strict LPSP = 0% requirement and the inclusion of GES. The authors argue this is justified for coal replacement where reliability is paramount.

### 5.4 Derived/Inferred Values

| Derived Value | Calculation | Result |
|---------------|-------------|--------|
| **Average daily load** | ~550 MW × 24 h | **~13,200 kWh/day (13.2 MWh/day)** |
| **Annual load demand** | ~550 MW × 8760 h | **~4,818,000 MWh/year (4.82 TWh/year)** |
| **PV capacity factor** | ~4.5 MW peak / 0.44 MW nameplate → ~10% instantaneous; annual: ~1,850–1,950 kWh/m²/day suggests ~20–22% CF | **~20–22%** |
| **Wind capacity factor** | 1.88 GW nameplate delivering majority of 4.82 TWh → ~4.82 TWh / (1.88 GW × 8760 h) | **~29–30%** (reasonable for coastal Morocco) |
| **Total wind nameplate** | 594 × 9.5 MW | **5,643 MW (5.64 GW)** |
| **PV total nameplate** | 1,005 × 0.44 kW | **442.2 kW (0.442 MW)** |
| **Wind:PV capacity ratio** | 5,643 / 0.442 | **~12,770:1** (wind overwhelmingly dominates) |
| **Electrolyzer utilization** | 790 MW runs only during surplus after GES full → likely low capacity factor | **Not calculable from paper data** |
| **H2 tank energy capacity** | 260,000 kg × 39.7 kWh/kg | **~10,322,000 kWh (10.3 GWh)** |
| **H2 tank autonomy at average load** | 10.3 GWh / 550 MW | **~18.8 hours** |
| **GES energy capacity** | Not explicitly stated (depends on piston mass) | **Not calculable from paper data** |
| **Annual H2 production** | Not stated as single figure | **Not calculable from paper data** |
| **System oversizing ratio** | Peak generation (~8 GW) / Peak load (~650 MW) | **~12.3×** |

### 5.5 Key Takeaways

1. **Coal replacement at 100% reliability is technically feasible but expensive.** The LCOE of 0.23 €/kWh sits at the upper end of the coal range ($0.18–0.34/kWh), demonstrating cost-competitiveness without even accounting for carbon pricing (expected 175–375 €/t CO₂ in Germany by 2045).

2. **Hybrid storage (GES + Hydrogen) enables 100% reliability by leveraging complementary timescales.** GES handles rapid fluctuations and intra-day balancing (seconds to hours, 80–85% RTE, 50+ year life), while hydrogen handles multi-day/seasonal gaps (lower RTE but high energy density). This division of stress extends component lifetimes.

3. **Wind dominates at this location.** The 12,770:1 wind-to-PV capacity ratio is extraordinary and reflects Safi's superior wind resource. PV contributes negligibly to total energy. This is location-specific and not a generalizable finding.

4. **The last 1% of reliability is extremely costly.** The paper shows that relaxing LPSP from 0% to even 1–5% would dramatically reduce component sizes and LCOE. For practical deployment, slight reliability relaxation is likely the most impactful cost-reduction lever.

5. **GES is the critical enabler for LPSP = 0%.** Without GES, the system would need either a much larger hydrogen infrastructure (more electrolyzer, FC, and H2 storage) or would fail to meet the strict reliability target. GES absorbs the high-frequency cycling that would otherwise degrade the fuel cell and electrolyzer, making the overall system both more reliable and more economical.

---

*Document generated from analysis of: Sahab et al., "Optimal design and energy management of a hybrid PV-Wind system with hydrogen and gravity energy storage: An off-grid sustainable alternative for coal power in Morocco," Renewable Energy Focus, vol. 56, 2026, Article 100775. DOI: 10.1016/j.ref.2025.100775*
