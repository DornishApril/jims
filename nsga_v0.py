"""
NSGA-II Optimization for Hybrid Energy System
==============================================
Paste this file next to your HybridEnergySystem file and run:
    python nsga2_optimizer.py

Optimizes: N_PV, N_WT, N_H2, N_FC, N_EL, N_DG
"""

import numpy as np
import pandas as pd
import random
import time
import warnings
from typing import Dict, List, Tuple, Optional

warnings.filterwarnings('ignore')

# ============================================================
# IMPORT YOUR SIMULATION  (adjust path if needed)
# ============================================================
from simulation import HybridEnergySystem


# ============================================================
# ██████╗  ██████╗ ███╗   ██╗███████╗██╗ ██████╗
# ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝
# ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
# ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
# ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝
# ============================================================

# ------------------------------------------------------------
# SECTION 1: DECISION VARIABLE BOUNDS
# [min, max] integer range for each component
# ------------------------------------------------------------
BOUNDS = {
    'N_PV': (0,  1000),
    'N_WT': (0,    50),
    'N_H2': (0,   200),
    'N_FC': (0,   200),
    'N_EL': (0,   200),
    'N_DG': (0,    20),
}

# ------------------------------------------------------------
# SECTION 2: OBJECTIVES
# Format: (label, metric, direction)
#   metric    -> 'C_total' | 'E_total' | 'LPSP' | any scalar key in details{}
#   direction -> 'minimize' | 'maximize'
# ------------------------------------------------------------
OBJECTIVES = [
    ('Cost',      'C_total', 'minimize'),
    ('Emissions', 'E_total', 'minimize'),

]

# ------------------------------------------------------------
# SECTION 3: CONSTRAINTS
# Format: (label, metric, operator, limit)
#   metric   -> same keys available as objectives above
#   operator -> '<=' | '>=' | '<' | '>' | '=='
# A solution is feasible when ALL constraints hold.
# ------------------------------------------------------------
CONSTRAINTS = [
    ('reliability',   'LPSP',    '<=', 0.05),
    # ('max_cost',    'C_total', '<=', 500_000),
     ('min_re',      'renewable_fraction', '>=', 0.90),
]

# ------------------------------------------------------------
# SECTION 4: GA PARAMETERS
# ------------------------------------------------------------
POP_SIZE       = 20     # population size (keep even)
N_GENERATIONS  = 500    # number of generations
CROSSOVER_PROB = 0.9    # probability of crossover per pair
MUTATION_PROB  = 0.1    # probability of mutating each gene
TOURNAMENT_K   = 3      # tournament selection pool size
RANDOM_SEED    = 42     # set to None for non-deterministic
PRINT_EVERY    = 10     # print progress every N generations

# ------------------------------------------------------------
# SECTION 5: OUTPUT FILES
# ------------------------------------------------------------
PARETO_CSV  = 'pareto_front.csv'
HISTORY_CSV = 'optimization_history.csv'

# ------------------------------------------------------------
# SECTION 6: CUSTOM OBJECTIVE  (optional)
# Uncomment the function and set CUSTOM_OBJECTIVE_FN = custom_objective
# Add a matching entry in OBJECTIVES above.
# Must return float (or list of floats for multiple extra objectives).
# ------------------------------------------------------------
# def custom_objective(config_dict, C_total, E_total, LPSP, details):
#     """Example: total PV land use (m²)."""
#     return config_dict['N_PV'] * 6.67
CUSTOM_OBJECTIVE_FN = None

# ------------------------------------------------------------
# SECTION 7: CUSTOM CONSTRAINT  (optional)
# Uncomment the function and set CUSTOM_CONSTRAINT_FN = custom_constraint
# Add a matching entry in CONSTRAINTS above.
# Return value > 0 means the constraint is violated.
# ------------------------------------------------------------
# def custom_constraint(config_dict, C_total, E_total, LPSP, details):
#     """Non-renewable (diesel) fraction must be <= 10% of total load."""
#     L  = details.get('L_year', 1) or 1
#     dg = details.get('E_DG_total', 0)
#     return max(0.0, dg / L - 0.10)   # violated when diesel > 10% of load

CUSTOM_CONSTRAINT_FN = None


# ============================================================
# ██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ██╗ █████╗ ██╗     ███████╗
# ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔══██╗██║     ██╔════╝
# ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔██╗ ██║███████║██║     ███████╗
# ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║     ╚════██║
# ██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚████║██║  ██║███████╗███████║
# ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝
# (do not edit below unless you know what you're doing)
# ============================================================

GENE_NAMES = list(BOUNDS.keys())
N_VAR  = len(GENE_NAMES)
N_OBJ  = len(OBJECTIVES) + (1 if CUSTOM_OBJECTIVE_FN else 0)
N_CON  = len(CONSTRAINTS) + (1 if CUSTOM_CONSTRAINT_FN else 0)
LB = np.array([BOUNDS[k][0] for k in GENE_NAMES], dtype=float)
UB = np.array([BOUNDS[k][1] for k in GENE_NAMES], dtype=float)
OBJ_DIR = np.array([1.0 if d == 'minimize' else -1.0 for _, _, d in OBJECTIVES])


# ============================================================
# INDIVIDUAL
# ============================================================

class Individual:
    def __init__(self, genes: np.ndarray):
        self.genes             = genes.copy()
        self.objectives        = None
        self.constraints       = None
        self.rank              = 0
        self.crowding_distance = 0.0
        self.feasible          = True

    def copy(self):
        ind = Individual(self.genes)
        if self.objectives  is not None: ind.objectives  = self.objectives.copy()
        if self.constraints is not None: ind.constraints = self.constraints.copy()
        ind.rank              = self.rank
        ind.crowding_distance = self.crowding_distance
        ind.feasible          = self.feasible
        return ind

    def to_config(self) -> Dict:
        return {name: int(self.genes[i]) for i, name in enumerate(GENE_NAMES)}


# ============================================================
# EVALUATION
# ============================================================

def evaluate(ind: Individual, sim: 'HybridEnergySystem', data: pd.DataFrame):
    cfg = ind.to_config()
    try:
        C_total, E_total, LPSP, details = sim.simulate_year(cfg, data)
    except Exception as e:
        print(f"EVAL FAILED: {cfg}")   # <-- add this
        print(f"ERROR: {e}")           # <-- and this
        import traceback
        traceback.print_exc()          # <-- full stack trace
        ind.objectives  = np.full(N_OBJ, 1e12)
        ind.constraints = np.full(max(N_CON, 1), 1e12)
        ind.feasible    = False
        return

    L    = details.get('L_year', 1) or 1
    E_re = details.get('E_PV_total', 0) + details.get('E_WT_total', 0)
    metrics = {
        'C_total': C_total, 'E_total': E_total, 'LPSP': LPSP,
        'renewable_fraction': E_re / L,
        **{k: v for k, v in details.items() if np.isscalar(v)},
    }

    # Objectives
    obj_vals = [float(metrics.get(m, 0.0)) for _, m, _ in OBJECTIVES]
    if CUSTOM_OBJECTIVE_FN is not None:
        extra = CUSTOM_OBJECTIVE_FN(cfg, C_total, E_total, LPSP, details)
        obj_vals += [extra] if np.isscalar(extra) else list(extra)
    ind.objectives = np.array(obj_vals)

    # Constraints
    con_vals = []
    for _, m, op, limit in CONSTRAINTS:
        v = float(metrics.get(m, 0.0))
        if   op == '<=': con_vals.append(max(0.0, v - limit))
        elif op == '>=': con_vals.append(max(0.0, limit - v))
        elif op == '<' : con_vals.append(max(0.0, v - limit + 1e-9))
        elif op == '>' : con_vals.append(max(0.0, limit - v + 1e-9))
        elif op == '==': con_vals.append(abs(v - limit))
    if CUSTOM_CONSTRAINT_FN is not None:
        extra = CUSTOM_CONSTRAINT_FN(cfg, C_total, E_total, LPSP, details)
        con_vals += [extra] if np.isscalar(extra) else list(extra)
    ind.constraints = np.array(con_vals) if con_vals else np.zeros(1)
    ind.feasible    = bool(np.all(ind.constraints <= 1e-9))


# ============================================================
# NSGA-II OPERATORS
# ============================================================

def dominates(a: Individual, b: Individual) -> bool:
    a_viol = float(np.sum(np.maximum(a.constraints, 0)))
    b_viol = float(np.sum(np.maximum(b.constraints, 0)))
    if     a.feasible and not b.feasible: return True
    if not a.feasible and     b.feasible: return False
    if not a.feasible and not b.feasible: return a_viol < b_viol
    a_obj = a.objectives * OBJ_DIR
    b_obj = b.objectives * OBJ_DIR
    return bool(np.all(a_obj <= b_obj) and np.any(a_obj < b_obj))


def fast_nondominated_sort(pop: List[Individual]) -> List[List[int]]:
    n  = len(pop)
    S  = [[] for _ in range(n)]
    nd = [0] * n
    fronts = [[]]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if   dominates(pop[i], pop[j]): S[i].append(j)
            elif dominates(pop[j], pop[i]): nd[i] += 1
        if nd[i] == 0:
            pop[i].rank = 0
            fronts[0].append(i)
    f = 0
    while fronts[f]:
        nxt = []
        for i in fronts[f]:
            for j in S[i]:
                nd[j] -= 1
                if nd[j] == 0:
                    pop[j].rank = f + 1
                    nxt.append(j)
        f += 1
        fronts.append(nxt)
    return [x for x in fronts if x]


def assign_crowding(pop: List[Individual], fronts: List[List[int]]):
    for front in fronts:
        if len(front) <= 2:
            for i in front: pop[i].crowding_distance = float('inf')
            continue
        for i in front: pop[i].crowding_distance = 0.0
        for oi in range(N_OBJ):
            srt  = sorted(front, key=lambda i: pop[i].objectives[oi])
            vals = [pop[i].objectives[oi] for i in srt]
            rng  = vals[-1] - vals[0]
            pop[srt[0]].crowding_distance  = float('inf')
            pop[srt[-1]].crowding_distance = float('inf')
            if rng < 1e-10: continue
            for k in range(1, len(srt) - 1):
                pop[srt[k]].crowding_distance += (vals[k+1] - vals[k-1]) / rng


def tournament(pop: List[Individual]) -> Individual:
    cands = random.sample(pop, TOURNAMENT_K)
    best  = cands[0]
    for c in cands[1:]:
        if c.rank < best.rank or (c.rank == best.rank and c.crowding_distance > best.crowding_distance):
            best = c
    return best


def sbx_crossover(p1: Individual, p2: Individual) -> Tuple[Individual, Individual]:
    eta = 15.0
    c1, c2 = p1.copy(), p2.copy()
    for i in range(N_VAR):
        if random.random() > 0.5: continue
        x1, x2 = float(p1.genes[i]), float(p2.genes[i])
        if abs(x1 - x2) < 1e-10: continue
        xl, xu = LB[i], UB[i]
        u = random.random()
        b = (2*u)**(1/(eta+1)) if u <= 0.5 else (1/(2*(1-u)))**(1/(eta+1))
        c1.genes[i] = int(np.clip(round(0.5*((x1+x2) - b*abs(x2-x1))), xl, xu))
        c2.genes[i] = int(np.clip(round(0.5*((x1+x2) + b*abs(x2-x1))), xl, xu))
    return c1, c2


def poly_mutation(ind: Individual) -> Individual:
    eta   = 20.0
    child = ind.copy()
    for i in range(N_VAR):
        if random.random() > MUTATION_PROB: continue
        xl, xu = LB[i], UB[i]
        if xl >= xu: continue
        x   = float(child.genes[i])
        rng = xu - xl
        d   = min(x - xl, xu - x) / rng
        u   = random.random()
        dq  = (2*u + (1-2*u)*(1-d)**(eta+1))**(1/(eta+1)) - 1 if u <= 0.5 \
              else 1 - (2*(1-u) + 2*(u-0.5)*(1-d)**(eta+1))**(1/(eta+1))
        child.genes[i] = int(np.clip(round(x + dq*rng), xl, xu))
    return child


# ============================================================
# MAIN NSGA-II LOOP
# ============================================================

def run_nsga2(sim: 'HybridEnergySystem', data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:

    if RANDOM_SEED is not None:
        np.random.seed(RANDOM_SEED)
        random.seed(RANDOM_SEED)

    t0 = time.time()
    print('=' * 65)
    print('  NSGA-II  —  Hybrid Energy System Optimizer')
    print('=' * 65)
    print(f"  Pop: {POP_SIZE}  |  Generations: {N_GENERATIONS}  |  Seed: {RANDOM_SEED}")
    print(f"  Objectives : {[lbl for lbl,_,_ in OBJECTIVES]}")
    print(f"  Constraints: {[lbl for lbl,_,_,_ in CONSTRAINTS]}")
    print('-' * 65)

    # Initialize
    pop = [
        Individual(np.array([random.randint(int(LB[i]), int(UB[i])) for i in range(N_VAR)], dtype=float))
        for _ in range(POP_SIZE)
    ]
    for ind in pop:
        evaluate(ind, sim, data)
    fronts = fast_nondominated_sort(pop)
    assign_crowding(pop, fronts)

    history = []

    for gen in range(N_GENERATIONS):

        # Offspring
        offspring = []
        while len(offspring) < POP_SIZE:
            p1, p2 = tournament(pop), tournament(pop)
            c1, c2 = sbx_crossover(p1, p2) if random.random() < CROSSOVER_PROB else (p1.copy(), p2.copy())
            for c in (c1, c2):
                c = poly_mutation(c)
                c.objectives = c.constraints = None
                offspring.append(c)
        offspring = offspring[:POP_SIZE]
        for ind in offspring:
            evaluate(ind, sim, data)

        # Combine, sort, select
        combined = pop + offspring
        fronts   = fast_nondominated_sort(combined)
        assign_crowding(combined, fronts)
        pop = []
        for front in fronts:
            if len(pop) + len(front) <= POP_SIZE:
                pop += [combined[i] for i in front]
            else:
                remaining = POP_SIZE - len(pop)
                srt = sorted(front, key=lambda i: combined[i].crowding_distance, reverse=True)
                pop += [combined[i] for i in srt[:remaining]]
                break

        # Record history
        feasible = [ind for ind in pop if ind.feasible] or pop
        obj_arr  = np.array([ind.objectives for ind in feasible])
        entry    = {'generation': gen + 1, 'n_feasible': len(feasible)}
        for idx, (lbl, _, _) in enumerate(OBJECTIVES):
            entry[f'{lbl}_min']  = float(np.min(obj_arr[:, idx]))
            entry[f'{lbl}_mean'] = float(np.mean(obj_arr[:, idx]))
        history.append(entry)

        if (gen + 1) % PRINT_EVERY == 0:
            mins = '  '.join(f"{entry[f'{lbl}_min']:>12.4g}" for lbl, _, _ in OBJECTIVES)
            print(f"  Gen {gen+1:>4}  |  feasible: {len(feasible):>3}  |  {mins}  |  {time.time()-t0:.0f}s")

            # Print best individual by first objective
            best = min(feasible, key=lambda ind: ind.objectives[0])
            cfg  = best.to_config()
            print(f"    Best: N_PV={cfg['N_PV']:>4}  N_WT={cfg['N_WT']:>3}  N_H2={cfg['N_H2']:>3}  N_FC={cfg['N_FC']:>3}  N_EL={cfg['N_EL']:>3}  N_DG={cfg['N_DG']:>3}"
                f"  ->  " + "  ".join(f"{lbl}={best.objectives[i]:.4g}" for i, (lbl,_,_) in enumerate(OBJECTIVES)))


    # Extract Pareto front
    pareto = [ind for ind in pop if ind.rank == 0 and ind.feasible]
    if not pareto:
        pareto = [ind for ind in pop if ind.rank == 0]

    rows = []
    for ind in pareto:
        row = ind.to_config()
        for idx, (lbl, _, _) in enumerate(OBJECTIVES):
            row[lbl] = ind.objectives[idx]
        for idx, (lbl, _, _, _) in enumerate(CONSTRAINTS):
            row[f'viol_{lbl}'] = ind.constraints[idx]
        row['feasible'] = ind.feasible
        rows.append(row)

    pareto_df  = pd.DataFrame(rows)
    history_df = pd.DataFrame(history)
    pareto_df.to_csv(PARETO_CSV,   index=False)
    history_df.to_csv(HISTORY_CSV, index=False)

    print('=' * 65)
    print(f"  Done in {time.time()-t0:.1f}s  |  Pareto solutions: {len(pareto_df)}")
    print(f"  Saved: {PARETO_CSV}  |  {HISTORY_CSV}")
    print('=' * 65)

    return pareto_df, history_df


# ============================================================
# SYSTEM PARAMETERS
# ============================================================

PARAMETERS = {
    'rated_PV': 0.327, 'v_cut_in': 2.75, 'v_rated': 9.0, 'rated_power': 25.0,
    'Cap_H2': 6, 'Cap_FC': 2, 'Cap_EL': 2, 'Cap_DG': 50,
    'H_min_percentage': 0, 'H_max_percentage': 0,
    'f_0': 0.246, 'f_1': 0.08145,
    'eta_PV': 0.15, 'eta_FC': 0.50, 'eta_EL': 0.70, 'eta_INVT': 0.90, 'H2_LHV': 33.3,
    'c_PV': 1500, 'c_WT': 3000, 'c_H2': 500, 'c_FC_cap': 2000, 'c_EL_cap': 1500,
    'c_DG_cap': 400, 'c_INVT': 300,
    'c_FC': 0, 'c_DG': 0, 'c_EL': 0, 'c_DG_FUEL': 0.82,
    'om_PV': 20, 'om_WT': 50, 'om_H2': 10, 'om_FC': 30, 'om_EL': 25,
    'om_DG': 0.03, 'om_INVT': 0,
    'rc_PV': 0, 'rc_WT': 1750, 'rc_H2': 10, 'rc_FC': 30, 'rc_EL': 25,
    'rc_DG': 500, 'rc_INVT': 300,
    'e_FC': 0.0, 'e_DG': 2.6391, 'e_EL': 0.0,
    'T_life': 20, 'r': 0.05, 'p_grid': 0.08,
    'A_PV': 6.67, 'P_DG_min': 0.3,
    'life_PV': 25, 'life_WT': 20, 'life_H2': 20, 'life_FC': 10,
    'life_EL': 15, 'life_DG': 15, 'life_INVT': 15,
}


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == '__main__':

    # 1. Load your data
    data = pd.read_excel('data/semi_final_load.xlsx')    # <-- change filename

    # 2. Instantiate simulation
    sim = HybridEnergySystem(PARAMETERS)

    # 3. Run optimizer
    pareto_df, history_df = run_nsga2(sim, data)

    # 4. Print best per objective
    print("\nBest solution by Cost:")
    print(pareto_df.loc[pareto_df['Cost'].idxmin()])

    print("\nBest solution by Emissions:")
    print(pareto_df.loc[pareto_df['Emissions'].idxmin()])

    print("\nBest solution by LPSP:")
    print(pareto_df.loc[pareto_df['LPSP'].idxmin()])