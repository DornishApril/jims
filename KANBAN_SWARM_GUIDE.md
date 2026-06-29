# Kanban Agent Swarm — Parameter Extraction Pipeline

## Overview

This document describes a **Kanban Agent Swarm** architecture where one agent is spawned per research paper in `paper_folder`. Each agent receives the **same extraction prompt** (`prompt.txt`) and works independently on its assigned paper, extracting predefined technical/economic parameters and writing results to a shared output file.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATOR                              │
│  (creates N kanban tasks, one per PDF, same prompt in body)     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                     HERMES GATEWAY                               │
│  (auto-dispatches READY tasks to workers)                        │
└──────────┬──────────┬──────────┬──────────┬─────────────────────┘
           │          │          │          │
           ▼          ▼          ▼          ▼
     ┌──────────┐┌──────────┐┌──────────┐┌──────────┐
     │ Agent 1  ││ Agent 2  ││ Agent 3  ││ Agent N  │
     │ paper_1  ││ paper_2  ││ paper_3  ││ paper_N  │
     │          ││          ││          ││          │
     │ reads    ││ reads    ││ reads    ││ reads    │
     │ prompt   ││ prompt   ││ prompt   ││ prompt   │
     │ extracts ││ extracts ││ extracts ││ extracts │
     │ writes   ││ writes   ││ writes   ││ writes   │
     └────┬─────┘└────┬─────┘└────┬─────┘└────┬─────┘
          │           │           │           │
          └───────────┴─────┬─────┴───────────┘
                            ▼
                 ┌─────────────────────┐
                 │  results/ (output)  │
                 │  results.xlsx       │
                 └─────────────────────┘
```

---

## Key Components

### 1. Working Directory

```
C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\
```

This is the **workspace boundary**. No agent may read, write, or modify files outside this directory tree.

### 2. Paper Folder (Input)

```
C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\
```

Contains 24 PDF research papers. Each agent is assigned exactly ONE paper.

### 3. Prompt File (Shared Instructions)

```
C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt
```

This is the **single prompt** injected into the body of every kanban task. It contains:
- Role definition
- Extraction rules (10 strict rules)
- Column structure (exact order)
- Output format requirements
- Quality control checklist
- Workspace and output path instructions

### 4. Output Folder

```
C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\
```

Each agent writes its extracted data here. The orchestrator merges all results into a final `results.xlsx`.

---

## Agent Lifecycle

### Step 1: Orient
Each agent reads its kanban task, identifies which paper it was assigned (from the task title), and locates the PDF in `paper_folder`.

### Step 2: Read Prompt
The agent reads `prompt.txt` to understand the exact extraction rules, column structure, and output requirements.

### Step 3: Extract
The agent reads its assigned PDF and extracts all parameters according to the 10 strict rules.

### Step 4: Write Output
The agent writes extracted data to `results/results.xlsx` in append mode (or creates a per-paper temp file that gets merged).

### Step 5: Complete
The agent calls `kanban_complete` with a summary of what it extracted.

---

## The 24 Papers (Current Inventory)

| # | Filename | Assigned Task |
|---|----------|---------------|
| 1 | 1-s2.0-S2352484723001609-main.pdf | T1 |
| 2 | Techno-Economic_Analysis_of_Hybrid_Hydrogen... | T2 |
| 3 | Article 3607.pdf | T3 |
| 4 | Article 36.pdf | T4 |
| 5 | Article 37.pdf | T5 |
| 6 | Article 38.pdf | T6 |
| 7 | Article 39.pdf | T7 |
| 8 | 1-s2.0-S0959652622033388-main.pdf | T8 |
| 9 | Article Text-19435-1-10-20260522.pdf | T9 |
| 10 | mathematics-10-03708-v2.pdf | T10 |
| 11 | 60169-194014-4-PB.pdf | T11 |
| 12 | ok58218-189848-2-PB.pdf | T12 |
| 13 | ayop2018.pdf | T13 |
| 14 | han2017.pdf | T14 |
| 15 | s41598-024-55631-3.pdf | T15 |
| 16 | 1-s2.0-S1110016820305457-main.pdf | T16 |
| 17 | file.pdf | T17 |
| 18 | (1) Design simulation of hydrogen based hybrid... | T18 |
| 19 | (10) Techno-economic and multicriteria analysis... | T19 |
| 20 | (6) Optimizing an integrated hybrid energy system... | T20 |
| 21 | (13) Solar, Wind, Hydrogen, and Bioenergy-Based... | T21 |
| 22 | (15) The Best Techno-economic Aspects... | T22 |
| 23 | (8) Hydrogen Energy Storage Based Green Power... | T23 |
| 24 | (11) [fourth paper if present] | T24 |

---

## How the .bat File Works

Running `create_kanban_swarm.bat` will:

1. Create the `results/` output directory
2. Generate one `hermes kanban create` command per PDF file
3. Each task is:
   - Named: `Param Extraction: <filename>`
   - Assigned to: `default` profile
   - Given the full prompt text as its body
   - Given workspace context (paths, rules, output location)
4. All tasks are independent (no parent links) so they run in parallel
5. After creation, start the gateway to begin dispatch

---

## Prerequisites

- Hermes Agent installed and configured
- `hermes` CLI available in PATH
- At least one profile configured (`default`)
- PDF files present in `paper_folder/`
- `prompt.txt` present in `parameters_extraction/`

---

## Running the Swarm

### Option A: Run the .bat file (Windows cmd.exe)

The `.bat` file is Windows batch syntax — it must run in `cmd.exe`, NOT in git-bash/MSYS.

**Method 1 — Double-click:**
Navigate to `C:\Users\Admin\OneDrive\Desktop\jims\` in File Explorer and double-click `create_kanban_swarm.bat`.

**Method 2 — From cmd.exe:**
```
cd C:\Users\Admin\OneDrive\Desktop\jims
create_kanban_swarm.bat
```

**Method 3 — From git-bash (calling cmd explicitly):**
```bash
cd /c/Users/Admin/OneDrive/Desktop/jims
cmd //c create_kanban_swarm.bat
```

### Option B: Run commands manually (bash/git-bash)

If you're in git-bash, run the `hermes kanban create` commands directly. See the .bat file for the full list of commands. The key steps are:

1. Create the results directory: `mkdir -p results/`
2. Run `hermes kanban create "Param Extraction: <paper.pdf>" --assignee default --body "..."` for each paper
3. Start the gateway: `hermes gateway run`

---

## Monitoring Task Progress

### View all tasks
```bash
hermes kanban list
```

### View only running tasks
```bash
hermes kanban list --status running
```

### View only done tasks
```bash
hermes kanban list --status done
```

### View a specific task's details (including summary)
```bash
hermes kanban show <task_id>
hermes kanban show <task_id> --json
```

### Check gateway status
```bash
hermes gateway status
```

### Watch live updates (poll every 10 seconds)
```bash
watch -n 10 "hermes kanban list"
```
Or in a loop:
```bash
while true; do clear; hermes kanban list; sleep 10; done
```

### Count tasks by status
```bash
hermes kanban list | grep -c "running"   # how many still working
hermes kanban list | grep -c "done"      # how many finished
hermes kanban list | grep -c "ready"     # how many waiting
hermes kanban list | grep -c "blocked"   # how many need attention
```

---

## Changing the Model for Kanban Tasks

Kanban workers use the **default profile's model**. There is no per-task `--model` flag on `hermes kanban create`.

### Check current model
```bash
hermes config show
```
Look for the `Model:` line — currently: `deepseek-v4-flash` via DeepSeek provider.

### Change the default model (affects all future kanban dispatches)

**Interactive picker:**
```bash
hermes model
```
Select provider, then model. This updates `config.yaml`.

**Non-interactive (set directly):**
```bash
# Switch to a specific provider + model
hermes config set model.provider openrouter
hermes config set model.model "anthropic/claude-sonnet-4"

# Or for DeepSeek models
hermes config set model.provider deepseek
hermes config set model.model "V3"
```

**Verify the change:**
```bash
hermes config show
```

### Important Notes on Model Choice

- All kanban workers use the **same model** (the default profile's model)
- If you want different models for different tasks, you need **multiple profiles** (see below)
- Changing the model only affects **newly dispatched** tasks — running tasks continue with whatever model they started with
- For PDF extraction, models with good document understanding (Claude Sonnet, GPT-4, DeepSeek V3) work best

### Using a Different Profile (Advanced)

If you have multiple profiles configured, you can assign tasks to different profiles:

```bash
hermes kanban create "Param Extraction: paper.pdf" --assignee <profile-name> --body "..."
```

Each profile can have its own model configured. To create a profile:
```bash
hermes profile create <name>
hermes -p <name> model   # set model for that profile
```

---

## Output Format

Each agent produces rows in `results/results.xlsx` with these columns (in exact order):

```
Paper Name | Performance Metrics | NOTES | TOTAL ANNUAL LOAD DEMAND | LCOE | LPSP | COE | Generator Configurations | rated_PV | v_cut_in | v_rated | rated_power | Cap_H2 | Cap_FC | Cap_EL | Cap_DG | H_min_percentage | H_max_percentage | Diesel Constants | f_0 | f_1 | Efficiency Parameters | eta_PV | eta_FC | eta_EL | eta_INVT | H2_LHV | Capital Costs | c_PV | c_WT | c_H2 | c_FC_cap | c_EL_cap | c_DG_cap | c_INVT | Operating Costs | c_FC | c_DG | c_EL | c_DG_FUEL | O&M Costs | om_PV | om_WT | om_H2 | om_FC | om_EL | om_DG | om_INVT | Replacement Costs | rc_PV | rc_WT | rc_H2 | rc_FC | rc_EL | rc_DG | rc_INVT | Emission Factors | e_FC | e_DG | e_EL | Economic Parameters | T_life | r | p_grid | Technical Parameters | A_PV | P_DG_min | Component Lifetimes | life_PV | life_WT | life_H2 | life_FC | life_EL | life_DG | life_INVT | System Configuration | N_PV | N_WT | N_H2 | N_FC | N_EL | N_DG
```

---

## Post-Processing (After All Agents Complete)

Once all tasks show `done`, run the merge script:

```bash
cd C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction
python merge_results.py
```

This combines all per-paper outputs into a single `results.xlsx`.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Task stuck in `running` | `hermes kanban reclaim <id>` to reset |
| Task needs human input | `hermes kanban block <id> "reason"` then `hermes kanban unblock <id>` |
| Agent wrote wrong output | Check `hermes kanban show <id>` for summary |
| Gateway not running | `hermes gateway start` |
| Too many concurrent agents | Reduce batch size (run .bat twice, half the tasks each) |

---

## Notes

- The prompt is **identical** for all agents — this ensures consistent extraction across all papers
- Each agent only touches its own paper — no cross-file interference
- The `results/` directory is the only shared write target
- If an agent fails, only that one paper is affected — re-run just that task
