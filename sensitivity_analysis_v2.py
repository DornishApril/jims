"""
sensitivity_analysis_v2.py
==========================
Extended Sensitivity Analysis for the Hybrid Energy System Simulation.

Two main sections:
  1. T_LIFE DIAGNOSTIC  – explains why cost is non-monotonic with project lifetime
  2. FULL SENSITIVITY   – sweeps each of the 6 decision variables (N_PV, N_WT,
                          N_H2, N_FC, N_EL, N_DG) and key parameters
                          (T_life, r, Cap_DG, Cap_H2, c_DG_FUEL, eta_FC, eta_EL)
                          one at a time, holding everything else at its base value.

Usage
-----
    python sensitivity_analysis_v2.py
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from simulation import HybridEnergySystem

# All generated files go here
OUTPUT_DIR = 'outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def _crf(r, T):
    """Capital Recovery Factor."""
    if r <= 0:
        return 1.0 / T
    return (r * (1 + r) ** T) / ((1 + r) ** T - 1)


def _rep_cost_analytical(system_obj, config, T_life, r):
    """
    Call the model's replacement-cost calculator directly so the diagnostic
    uses exactly the same logic as the simulation.
    """
    return system_obj.calculate_replacement_cost(config, T_life, r)


# ─────────────────────────────────────────────────────────────────────────────
# BASE PARAMETERS & CONFIG
# ─────────────────────────────────────────────────────────────────────────────

BASE_PARAMETERS = {
    'rated_PV': 0.327, 'v_cut_in': 2.75, 'v_rated': 9.0, 'rated_power': 25.0,
    'Cap_H2': 100, 'Cap_FC': 100, 'Cap_EL': 100, 'Cap_DG': 3,
    'H_min_percentage': 0, 'H_max_percentage': 0,
    'f_0': 0.246, 'f_1': 0.08145,
    'eta_PV': 0.15, 'eta_FC': 0.50, 'eta_EL': 0.70, 'eta_INVT': 0.90, 'H2_LHV': 33.3,
    'c_PV': 1500, 'c_WT': 3000,
    'c_H2': 300, 'c_FC_cap': 1200, 'c_EL_cap': 1000, 'c_DG_cap': 400, 'c_INVT': 300,
    'c_FC': 0, 'c_DG': 0, 'c_EL': 0, 'c_DG_FUEL': 0.82,
    'om_PV': 20, 'om_WT': 50, 'om_H2': 10, 'om_FC': 30, 'om_EL': 25,
    'om_DG': 0.03, 'om_INVT': 0,
    'rc_PV': 0, 'rc_WT': 1750, 'rc_H2': 10, 'rc_FC': 30, 'rc_EL': 25,
    'rc_DG': 500, 'rc_INVT': 300,
    'e_FC': 0.0, 'e_DG': 2.6391, 'e_EL': 0.0,
    'T_life': 20, 'r': 0.05, 'p_grid': 0.08,
    'A_PV': 6.67, 'P_DG_min': 0.3,
    'life_PV': 25, 'life_WT': 20, 'life_H2': 20,
    'life_FC': 10, 'life_EL': 15, 'life_DG': 15, 'life_INVT': 15,
    'output_simulation': False,
}

BASE_CONFIG = {
    'N_PV': 596, 'N_WT': 49, 'N_H2': 59, 'N_FC': 2, 'N_EL': 2, 'N_DG': 1,
}

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 – T_LIFE DIAGNOSTIC
# ─────────────────────────────────────────────────────────────────────────────

def tlife_diagnostic(data, t_values=None):
    """
    For each T_life value, break down the total cost and LCOE into their
    components and show WHY LCOE can temporarily rise when going 20 → 25 years.

    The key insight:
        LCOE = C_total / E_served
             = [(C_cap + C_rep(T)) * CRF(T)  +  C_om  +  C_op] / E_served

    * E_served (kWh/yr actually delivered to the load) does NOT change with
      T_life – it comes from the hourly dispatch simulation.
    * CRF(T) always DECREASES as T grows  → pushes LCOE DOWN
    * C_rep(T) can JUMP at certain T values when a new replacement cycle
      is triggered (e.g. a 10-year FC gets replaced at year 10, 20 ...
      but at T=21+ a replacement at year 20 is suddenly included)
    * The net effect: LCOE is NON-MONOTONIC with T_life.

    Verdict: this is correct engineering economics behaviour.
    """
    if t_values is None:
        t_values = list(range(5, 51)) + [60, 70, 80, 90, 100]

    params = BASE_PARAMETERS.copy()
    config = BASE_CONFIG.copy()

    system = HybridEnergySystem(params)
    # Run simulation once – C_cap, C_op, C_om, E_served do NOT depend on T_life
    _, _, _, base_details = system.simulate_year(config, data)
    C_cap    = base_details['C_cap']
    C_op     = base_details['C_op']
    C_om     = base_details['C_om_annual']
    E_served = base_details['L_year'] - base_details['E_unmet']  # kWh actually served
    r        = params['r']

    rows = []
    for T in t_values:
        crf      = _crf(r, T)
        C_rep    = _rep_cost_analytical(system, config, T, r)
        annualized_cap_rep = (C_cap + C_rep) * crf
        C_total  = annualized_cap_rep + C_om + C_op
        LCOE     = C_total / E_served if E_served > 0 else float('nan')
        rows.append({
            'T_life': T,
            'CRF':    round(crf, 6),
            'C_rep (PV $)': round(C_rep, 0),
            'Annualized Cap+Rep ($/yr)': round(annualized_cap_rep, 0),
            'C_total ($/yr)': round(C_total, 0),
            'LCOE ($/kWh)': round(LCOE, 6),
        })

    df = pd.DataFrame(rows)

    print("\n" + "="*110)
    print("T_LIFE DIAGNOSTIC  –  LCOE & Cost Breakdown vs Project Lifetime")
    print("="*110)
    print(df.to_string(index=False))
    print()
    print(f"  E_served (fixed, independent of T_life): {E_served:,.0f} kWh/yr")
    print()
    print("EXPLANATION")
    print("-"*80)
    print("  LCOE = C_total / E_served")
    print("       = [(C_cap + C_rep) * CRF  +  C_om  +  C_op]  /  E_served")
    print()
    print("  E_served is constant (hourly simulation doesn't change with T_life).")
    print("  So LCOE moves exactly with C_total.")
    print()
    print("  CRF decreases monotonically with T → always pushes LCOE DOWN.")
    print()
    print("  C_rep (replacement cost PV) jumps whenever a new replacement")
    print("  cycle appears within the project window:")
    _print_replacement_schedule(system, config, max(t_values), r)
    print()
    print("  Net effect: (C_cap + C_rep) * CRF can be non-monotonic.")
    print("  T=20 → T=25 may add new replacements whose discounted cost")
    print("  exceeds the CRF saving, so LCOE temporarily rises.")
    print("  At T=100 the CRF is so small it crushes everything → LCOE drops.")
    print()
    print("  This is CORRECT engineering-economics behaviour.")
    print("="*110)

    # --- Plot (2×2): CRF, C_rep, C_total, LCOE ---
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle("T_life Diagnostic: Why LCOE is Non-Monotonic", fontsize=14, fontweight='bold')

    t_arr  = df['T_life'].values
    lcoe   = df['LCOE ($/kWh)'].values
    ctotal = df['C_total ($/yr)'].values

    axes[0, 0].plot(t_arr, df['CRF'], 'b-o', markersize=4)
    axes[0, 0].set_title('Capital Recovery Factor (CRF)')
    axes[0, 0].set_xlabel('T_life (years)'); axes[0, 0].set_ylabel('CRF')
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].plot(t_arr, df['C_rep (PV $)'] / 1e6, 'r-o', markersize=4)
    axes[0, 1].set_title('Replacement Cost PV  (step-function jumps)')
    axes[0, 1].set_xlabel('T_life (years)'); axes[0, 1].set_ylabel('C_rep (M$)')
    axes[0, 1].grid(True, alpha=0.3)

    axes[1, 0].plot(t_arr, ctotal / 1e3, 'g-o', markersize=4, linewidth=2)
    for T_ref, color in [(20, 'blue'), (25, 'orange'), (100, 'red')]:
        if T_ref in list(t_arr):
            idx   = list(t_arr).index(T_ref)
            y_val = ctotal[idx] / 1e3
            axes[1, 0].scatter([T_ref], [y_val], color=color, zorder=5, s=80,
                               label=f"T={T_ref}: {y_val:.1f} k$/yr")
    axes[1, 0].set_title('Total Annualised Cost')
    axes[1, 0].set_xlabel('T_life (years)'); axes[1, 0].set_ylabel('C_total (k$/yr)')
    axes[1, 0].legend(fontsize=8); axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].plot(t_arr, lcoe, 'm-o', markersize=4, linewidth=2)
    for T_ref, color in [(20, 'blue'), (25, 'orange'), (100, 'red')]:
        if T_ref in list(t_arr):
            idx   = list(t_arr).index(T_ref)
            y_val = lcoe[idx]
            axes[1, 1].scatter([T_ref], [y_val], color=color, zorder=5, s=80,
                               label=f"T={T_ref}: {y_val:.4f} $/kWh")
    axes[1, 1].set_title('LCOE  ← what you observed')
    axes[1, 1].set_xlabel('T_life (years)'); axes[1, 1].set_ylabel('LCOE ($/kWh)')
    axes[1, 1].legend(fontsize=8); axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    fpath = os.path.join(OUTPUT_DIR, 'tlife_diagnostic.png')
    plt.savefig(fpath, dpi=150, bbox_inches='tight')
    print(f"  → Saved: {fpath}")
    plt.close()

    return df


def _print_replacement_schedule(system_obj, config, T_max, r):
    """Print when each component gets replaced over the project window."""
    components = [
        ('N_PV',  system_obj.rated_PV,    system_obj.rc_PV,  system_obj.life_PV,  'PV'),
        ('N_WT',  system_obj.rated_power, system_obj.rc_WT,  system_obj.life_WT,  'Wind'),
        ('N_H2',  system_obj.Cap_H2,      system_obj.rc_H2,  system_obj.life_H2,  'H2 Storage'),
        ('N_FC',  system_obj.Cap_FC,      system_obj.rc_FC,  system_obj.life_FC,  'Fuel Cell'),
        ('N_EL',  system_obj.Cap_EL,      system_obj.rc_EL,  system_obj.life_EL,  'Electrolyzer'),
        ('N_DG',  system_obj.Cap_DG,      system_obj.rc_DG,  system_obj.life_DG,  'Diesel Gen'),
    ]
    print(f"  {'Component':<14} {'Life':>5} {'Replacement years (up to T={})'.format(T_max):<50}")
    print(f"  {'-'*14} {'-'*5} {'-'*50}")
    for comp_key, cap_per, rc, life, name in components:
        n = config.get(comp_key, 0)
        if n == 0 or life <= 0:
            continue
        years = list(range(life, T_max, life))
        total_rc = n * cap_per * rc
        print(f"  {name:<14} {life:>5}   {str(years):<50}  (1 event = ${total_rc:,.0f} undiscounted)")


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 – FULL SENSITIVITY ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────

def run_sweep(param_name, values, data, is_config=False, label=None, unit=''):
    """
    Sweep one parameter/decision-variable and return a results DataFrame.

    Parameters
    ----------
    param_name : str
        Key in BASE_PARAMETERS or BASE_CONFIG.
    values : list
        Values to sweep.
    data : pd.DataFrame
    is_config : bool
        True  → param_name lives in BASE_CONFIG (decision variable).
        False → param_name lives in BASE_PARAMETERS (system parameter).
    label : str, optional
        Pretty name for printing.
    unit : str, optional
        Unit for display.
    """
    label = label or param_name

    print(f"\n{'─'*100}")
    print(f"  SWEEP: {label}  [{unit}]")
    print(f"{'─'*100}")
    print(f"  {'Value':>12} | {'LCOE ($/kWh)':>13} | {'Cost ($/yr)':>13} | {'Emissions (kg CO2)':>18} | {'LPSP (%)':>9}")
    print(f"  {'-'*12}-+-{'-'*13}-+-{'-'*13}-+-{'-'*18}-+-{'-'*9}")

    rows = []
    for val in values:
        params = BASE_PARAMETERS.copy()
        cfg    = BASE_CONFIG.copy()

        if is_config:
            cfg[param_name] = val
        else:
            params[param_name] = val

        try:
            sys_obj = HybridEnergySystem(params)
            C_total, E_total, LPSP, details = sys_obj.simulate_year(cfg, data)
            E_served = details['L_year'] - details['E_unmet']
            LCOE = C_total / E_served if E_served > 0 else float('nan')
            crf  = details['CRF']
            rows.append({
                'value':   val,
                'LCOE':    LCOE,
                'C_total': C_total,
                'E_total': E_total,
                'LPSP':    LPSP * 100,
                'CRF':     crf,
            })
            val_str = f"{val:>12}" if isinstance(val, (int, float)) else f"{str(val):>12}"
            print(f"  {val_str} | {LCOE:>13.6f} | {C_total:>13,.0f} | {E_total:>18,.0f} | {LPSP*100:>9.3f}")
        except Exception as e:
            print(f"  {val:>12} |   ERROR: {e}")

    return pd.DataFrame(rows)


def full_sensitivity(data):
    """
    Run one-at-a-time (OAT) sensitivity analysis on:
      • 6 decision variables: N_PV, N_WT, N_H2, N_FC, N_EL, N_DG
      • Key parameters:      T_life, r, Cap_DG, Cap_H2, c_DG_FUEL, eta_FC, eta_EL
    """
    print("\n" + "="*90)
    print("FULL SENSITIVITY ANALYSIS  (One-At-a-Time, base config fixed for all others)")
    print("="*90)
    print(f"  Base config: {BASE_CONFIG}")
    print(f"  Base T_life={BASE_PARAMETERS['T_life']} yr, r={BASE_PARAMETERS['r']}")

    # ── DECISION VARIABLES ──────────────────────────────────────────────────
    sweeps_config = [
        # (param_name,  values,                                    label,          unit)
        ('N_PV',  [50, 100, 200, 300, 400, 500, 600, 700, 800],  'Num PV Panels',       'panels'),
        ('N_WT',  [5, 10, 20, 30, 40, 50, 60, 70, 80],           'Num Wind Turbines',   'units'),
        ('N_H2',  [10, 20, 30, 40, 50, 59, 75, 100, 150],        'Num H2 Storage Units','units'),
        ('N_FC',  [1, 2, 5, 10, 20, 50, 100],                    'Num Fuel Cells',      'units'),
        ('N_EL',  [1, 2, 5, 10, 20, 50, 100],                    'Num Electrolyzers',   'units'),
        ('N_DG',  [1, 2, 3, 5, 10, 20],                          'Num Diesel Generators','units'),
    ]

    # ── SYSTEM PARAMETERS ───────────────────────────────────────────────────
    sweeps_param = [
        # (param_name,  values,                                    label,          unit)
        ('T_life',    [5, 10, 15, 20, 25, 30, 40, 50, 75, 100],  'Project Lifetime',    'years'),
        ('r',         [0.01, 0.03, 0.05, 0.07, 0.10, 0.15],      'Discount Rate',       'fraction'),
        ('Cap_DG',    [1, 3, 5, 10, 20, 50],                      'Diesel Gen Capacity', 'kW/unit'),
        ('Cap_H2',    [10, 50, 100, 200, 500],                    'H2 Storage Cap',      'kg/unit'),
        ('c_DG_FUEL', [0.50, 0.70, 0.82, 1.00, 1.20, 1.50],      'Diesel Fuel Price',   '$/litre'),
        ('eta_FC',    [0.30, 0.40, 0.50, 0.60, 0.70],            'Fuel Cell Efficiency','fraction'),
        ('eta_EL',    [0.50, 0.60, 0.70, 0.80, 0.90],            'Electrolyzer Eff.',   'fraction'),
    ]

    all_results = {}  # param_name → DataFrame

    for param_name, values, label, unit in sweeps_config:
        df = run_sweep(param_name, values, data, is_config=True, label=label, unit=unit)
        all_results[param_name] = (df, label, unit, True)

    for param_name, values, label, unit in sweeps_param:
        df = run_sweep(param_name, values, data, is_config=False, label=label, unit=unit)
        all_results[param_name] = (df, label, unit, False)

    return all_results


# ─────────────────────────────────────────────────────────────────────────────
# PLOTTING
# ─────────────────────────────────────────────────────────────────────────────

def plot_sensitivity(all_results, output_prefix='sensitivity_v2'):
    """
    Create one figure per metric (Cost, Emissions, LPSP) with subplots for
    every swept parameter.  Each subplot shows the sensitivity curve for that
    parameter, with the base value marked.
    """
    param_names = list(all_results.keys())
    n = len(param_names)
    metrics = [
        ('LCOE',    'LCOE ($/kWh)',           'mediumseagreen'),
        ('C_total', 'Total Cost ($/yr)',       'steelblue'),
        ('E_total', 'Emissions (kg CO2/yr)',   'firebrick'),
        ('LPSP',    'LPSP (%)',                'darkorange'),
    ]

    for metric_key, metric_label, color in metrics:
        ncols = 4
        nrows = int(np.ceil(n / ncols))
        fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * 4.5, nrows * 3.5))
        axes = axes.flatten()
        fig.suptitle(f'Sensitivity Analysis – {metric_label}', fontsize=14, fontweight='bold')

        for idx, param_name in enumerate(param_names):
            df, label, unit, is_config = all_results[param_name]
            ax = axes[idx]

            if df.empty or metric_key not in df.columns:
                ax.text(0.5, 0.5, 'No data', ha='center', va='center',
                        transform=ax.transAxes)
                continue

            y = df[metric_key].values
            x = df['value'].values

            # Autoscale for large numbers
            scale, scale_label = 1, ''
            if metric_key == 'C_total':
                if y.max() > 1e6:  scale, scale_label = 1e6, ' (M$)'
                elif y.max() > 1e3: scale, scale_label = 1e3, ' (k$)'
            elif metric_key == 'E_total':
                if y.max() > 1e6:  scale, scale_label = 1e6, ' (M kg)'
                elif y.max() > 1e3: scale, scale_label = 1e3, ' (k kg)'

            ax.plot(x, y / scale, marker='o', markersize=5, linewidth=2,
                    color=color, markerfacecolor='white', markeredgewidth=1.5)

            # Mark base value
            base_val = BASE_CONFIG.get(param_name) if is_config else BASE_PARAMETERS.get(param_name)
            if base_val is not None and base_val in df['value'].values:
                b_idx = df[df['value'] == base_val].index[0]
                b_y = df.at[b_idx, metric_key] / scale
                ax.scatter([base_val], [b_y], color='black', zorder=5, s=80,
                           label=f'Base={base_val}')
                ax.legend(fontsize=7, loc='best')

            ax.set_title(f'{label}', fontsize=9, fontweight='bold')
            ax.set_xlabel(f'{param_name} ({unit})', fontsize=8)
            ax.set_ylabel(f'{metric_label}{scale_label}', fontsize=8)
            ax.grid(True, alpha=0.3)
            ax.tick_params(labelsize=7)

        # Hide unused axes
        for idx in range(n, len(axes)):
            axes[idx].set_visible(False)

        plt.tight_layout()
        fname = os.path.join(OUTPUT_DIR, f'{output_prefix}_{metric_key}.png')
        plt.savefig(fname, dpi=150, bbox_inches='tight')
        print(f"  → Saved: {fname}")
        plt.close()


def plot_tornado(all_results, metric_key='C_total', output_prefix='sensitivity_v2'):
    """
    Tornado chart: for each swept parameter, compute the range
    (max - min) of the metric.  Sort by descending range to show
    which parameters matter most.
    """
    rows = []
    for param_name, (df, label, unit, _) in all_results.items():
        if df.empty or metric_key not in df.columns:
            continue
        y = df[metric_key].values
        # Base value (from the base config/params)
        is_config = all_results[param_name][3]
        base_val  = BASE_CONFIG.get(param_name) if is_config else BASE_PARAMETERS.get(param_name)
        base_mask = df['value'] == base_val
        if base_mask.any():
            base_y = df.loc[base_mask, metric_key].values[0]
        else:
            # use middle point as proxy
            base_y = y[len(y) // 2]

        low  = y.min() - base_y
        high = y.max() - base_y
        rows.append({
            'param': f'{label}\n({param_name})',
            'low':   low,
            'high':  high,
            'range': y.max() - y.min(),
        })

    df_tornado = pd.DataFrame(rows).sort_values('range', ascending=True)

    metric_labels = {
        'LCOE':    'LCOE ($/kWh)',
        'C_total': 'Total Cost ($/yr)',
        'E_total': 'Emissions (kg CO2/yr)',
        'LPSP':    'LPSP (%)',
    }
    metric_label = metric_labels.get(metric_key, metric_key)

    scale, scale_label = 1, ''
    max_range = df_tornado['range'].max()
    if max_range > 1e6:
        scale, scale_label = 1e6, ' [M$]'
    elif max_range > 1e3:
        scale, scale_label = 1e3, ' [k$]'

    fig, ax = plt.subplots(figsize=(12, max(6, len(df_tornado) * 0.55 + 1.5)))
    y_pos = np.arange(len(df_tornado))

    bars_neg = ax.barh(y_pos, df_tornado['low'].values / scale, color='#d62728', alpha=0.8, label='Below base')
    bars_pos = ax.barh(y_pos, df_tornado['high'].values / scale, color='#1f77b4', alpha=0.8, label='Above base')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(df_tornado['param'].values, fontsize=9)
    ax.axvline(0, color='black', linewidth=1.5)
    ax.set_xlabel(f'Deviation from base {metric_label}{scale_label}', fontsize=11)
    ax.set_title(f'Tornado Chart – {metric_label}\n(sorted by total range)', fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.25, axis='x')

    plt.tight_layout()
    fname = os.path.join(OUTPUT_DIR, f'{output_prefix}_tornado_{metric_key}.png')
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    print(f"  → Saved: {fname}")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    # ── Load data ────────────────────────────────────────────────────────────
    for fpath in ['data/semi_final_load.xlsx', 'data/combined.xlsx']:
        try:
            data = pd.read_excel(fpath)
            print(f"Data loaded from: {fpath}  ({len(data)} rows)")
            break
        except FileNotFoundError:
            data = None

    if data is None:
        raise FileNotFoundError(
            "Could not find data/semi_final_load.xlsx or data/combined.xlsx. "
            "Please check file paths."
        )

    # ── Section 1: T_life diagnostic ─────────────────────────────────────────
    print("\n\n" + "█"*90)
    print("  SECTION 1 – T_LIFE DIAGNOSTIC")
    print("█"*90)
    tlife_df = tlife_diagnostic(data)

    # ── Section 2: Full sensitivity ──────────────────────────────────────────
    print("\n\n" + "█"*90)
    print("  SECTION 2 – FULL SENSITIVITY ANALYSIS")
    print("█"*90)
    all_results = full_sensitivity(data)

    # ── Plotting ─────────────────────────────────────────────────────────────
    print("\nGenerating plots …")
    plot_sensitivity(all_results)
    plot_tornado(all_results, metric_key='LCOE')
    plot_tornado(all_results, metric_key='C_total')
    plot_tornado(all_results, metric_key='E_total')
    plot_tornado(all_results, metric_key='LPSP')

    # ── Save tabular results ─────────────────────────────────────────────────
    xlsx_path = os.path.join(OUTPUT_DIR, 'sensitivity_results_v2.xlsx')
    with pd.ExcelWriter(xlsx_path) as writer:
        for param_name, (df, label, unit, _) in all_results.items():
            sname = param_name[:31]  # Excel sheet name limit
            df.to_excel(writer, sheet_name=sname, index=False)
        tlife_df.to_excel(writer, sheet_name='T_life_diagnostic', index=False)
    print(f"  → Saved: {xlsx_path}")

    print("\nDone.")
