# Generate a publication-style Pareto plot from the user's data
import pandas as pd
import matplotlib.pyplot as plt

cost = [
240996.861645829,473715.40727473237,473715.40727473237,240996.861645829,
324063.9190199127,323822.07512389345,379301.09837432695,253381.35254325668,
273552.23156160617,446432.5135336431,259894.7270465049,306686.49790963234,
363733.12497846864,341268.6904356781,432566.9761704122,415169.45351630036,
285596.77695149014,285596.77695149014,415169.45351630036,310603.3715321963
]

emissions = [
270269.8143397175,38171.793680069866,38171.793680069866,270269.8143397175,
86122.57024814101,162683.93567568547,66591.10422537598,242979.16750800522,
210158.81802207758,41668.79390532631,231076.3571231491,175272.5820038882,
74467.55112632594,80499.15663030976,52641.19962743118,55309.64683505992,
201122.18000262624,201122.18000262624,55309.64683505992,170462.9970646751
]

df = pd.DataFrame({"Cost": cost, "Emissions": emissions}).drop_duplicates()

pareto_points = []
for i, row in df.iterrows():
    dominated = False
    for j, row2 in df.iterrows():
        if (row2["Cost"] <= row["Cost"] and row2["Emissions"] <= row["Emissions"]) and \
           (row2["Cost"] < row["Cost"] or row2["Emissions"] < row["Emissions"]):
            dominated = True
            break
    if not dominated:
        pareto_points.append(row)

pareto = pd.DataFrame(pareto_points).sort_values("Cost")

plt.rcParams["font.family"] = "DejaVu Sans"

plt.figure()
plt.scatter(df["Cost"], df["Emissions"], label="Candidate Solutions")
plt.plot(pareto["Cost"], pareto["Emissions"], marker="o", label="Pareto Front")

plt.xlabel("System Cost")
plt.ylabel("CO2 Emissions")
plt.title("Pareto Front for Hybrid Energy System Optimization")
plt.grid(True)
plt.legend()

plt.show()