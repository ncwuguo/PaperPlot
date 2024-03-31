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
@Descrip  : Fig.4 Comparison of manufacture's profit
"""

import matplotlib as mpl  # noqa: F401
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator


# initial settings
# mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "no-latex"])

# Grid data X, Y and meshgrid. X -> \rho, Y -> c_2
X, Y = np.meshgrid(np.linspace(0.6, 1, 30), np.linspace(50, 250, 30))

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

benchmark_profit_m = (
    Qa * (W - C1 - G0)
    + (V - X * V - C1 - G0 - H0) * qa
    + X * (E * qa - (E - V) * (((Qa + qa) ** 2 - Qa**2) / (2 * U)))
)
mainmodel_profit_m = (
    (W - C1 - G0) * Qg
    + (V + O - C1 - H0 - G0) * qm
    + X
    * (
        (E - V) * (qm - ((Qg + qm) ** 2 - Qg**2) / (2 * U))
        + (E - Y - G) * (qs - ((Qg + qm + qs) ** 2 - (Qg + qm) ** 2) / (2 * U))
    )
)
Z = mainmodel_profit_m - benchmark_profit_m

# Create the figure and axes objects
fig = plt.figure(figsize=(6.7, 6))
ax = plt.subplot(111)

# Plot
CS = ax.contourf(X, Y, Z, cmap=plt.get_cmap("gray_r"))

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
ax.annotate("175000", fontsize=14, xy=(0.615, 68.5), rotation=22, color="#c9c9c9")
ax.annotate("150000", fontsize=14, xy=(0.704, 67.4), rotation=12, color="#c9c9c9")
ax.annotate("125000", fontsize=14, xy=(0.799, 65.3), rotation=7)
ax.annotate("100000", fontsize=14, xy=(0.852, 58.9), rotation=4)
ax.annotate("75000", fontsize=14, xy=(0.933, 55.1), rotation=2)

# Color bar
cbar = fig.colorbar(CS, fraction=0.045, pad=0.05)
cbar.ax.tick_params(labelsize=18)

# legend
colors = ["#555555"]
legend_labels = ["$E\,\\Pi_m-E\,\\Pi_{am}$"]
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

# show
ax.set_box_aspect(1)
fig.tight_layout()
plt.show()
