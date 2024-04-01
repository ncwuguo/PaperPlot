"""
██████╗  █████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗      ██████╗ ████████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║     ██╔═══██╗╚══██╔══╝
██████╔╝███████║██████╔╝█████╗  ██████╔╝    ██████╔╝██║     ██║   ██║   ██║
██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ██╔═══╝ ██║     ██║   ██║   ██║
██║     ██║  ██║██║     ███████╗██║  ██║    ██║     ███████╗╚██████╔╝   ██║
╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝    ╚═╝
@Title    : 混合契约下应急物资政企三级联合储备模型研究
@Author   : Guo Keting, Gong Lingjun*
@Created  : 2023-10-19
@Revision : 2024-03-30
@Submit   : CN [Chinese Journal of management science]
@Descrip  : Fig.3 Comparison of supplier's profit
"""

import matplotlib as mpl  # noqa: F401
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator


# Initial settings
# mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "no-latex"])

# Grid data X, Y and meshgrid. X -> \rho, Y -> c_2
X, Y = np.meshgrid(np.linspace(0.6, 1, 30), np.linspace(80, 250, 30))

# Set parameter values
U, MU = 20000, 10000
HG, H0, H1 = 12, 10, 5
C0, C1 = 25, 30
G0, G = 20, 25
V, S = 8, 5
O = 10  # noqa: E741
W, E, M = 150, 300, 400

# Calculate the values for Qg, qm, qs, Qa, and qa
Qg = U * (1 - (W + HG - V) / (X * (E - V)))
qm = U * (1 - (C1 + H0 + G0 - V - O) / (X * (Y + G - V))) - Qg
qs = U * (1 - (C0 + H1 - S - O) / (X * (Y - S))) - qm - Qg
Qa = U * (1 - (W + HG - V) / (X * (E - V)))
qa = U * (1 - (C1 + G0 + H0 - V) / (X * (E - V))) - Qa

benchmark_profit_s = (C1 - C0) * (Qa + qa)
mainmodel_profit_s = (
    (C1 - C0) * (Qg + qm)
    + (S + O - C0 - H1) * qs
    + X * (Y - S) * (qs - ((Qg + qm + qs) ** 2 - (Qg + qm) ** 2) / (2 * U))
)
Z = mainmodel_profit_s - benchmark_profit_s

# Create the figure and axes objects
fig = plt.figure(figsize=(6.7, 6))
ax = plt.subplot(111)

# Plot
CS = ax.contourf(X, Y, Z, cmap=plt.get_cmap("gray_r"))

# Ticker and labels
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(30))
ax.yaxis.set_minor_locator(MultipleLocator(15))
ax.tick_params(which="major", length=4)
ax.tick_params(which="minor", length=2)
ax.set_xlabel("$\\rho$", size=26)
ax.set_ylabel("$c_2$", size=26)
ax.tick_params(labelsize=18)

# Annotate contour labels
ax.annotate("40000", fontsize=14, xy=(0.617, 188.5), rotation=92, color="#c9c9c9")
ax.annotate("36000", fontsize=14, xy=(0.682, 165.4), rotation=87, color="#c9c9c9")
ax.annotate("32000", fontsize=14, xy=(0.754, 145.4), rotation=74, color="#c9c9c9")
ax.annotate("28000", fontsize=14, xy=(0.819, 121.6), rotation=47)
ax.annotate("24000", fontsize=14, xy=(0.859, 99.6), rotation=21)
ax.annotate("20000", fontsize=14, xy=(0.893, 86.1), rotation=12)

# Color bar
cbar = fig.colorbar(CS, fraction=0.045, pad=0.05)
cbar.ax.tick_params(labelsize=18)

# Legend
colors = ["#555555"]
legend_labels = ["$E\,\\Pi_s-E\,\\Pi_{as}$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=20,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    loc="upper center",
    bbox_to_anchor=(0.55, 1.2),
)

# Show
ax.set_box_aspect(1)
fig.tight_layout()
plt.show()
