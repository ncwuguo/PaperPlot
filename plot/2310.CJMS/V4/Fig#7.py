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
@Descrip  : Fig.7 Reserves of manufacturer and supplier
"""

import matplotlib as mpl  # noqa: F401
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.ticker import MultipleLocator


# Initial settings
# mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "grid", "no-latex"])

# Grid data
E = np.array([250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750])
X = 0.6
Y = 150

# Set parameter values
U, MU = 20000, 10000
HG, H0, H1 = 12, 10, 5
C0, C1 = 25, 30
G0, G = 20, 25
V, S = 8, 5
O = 10  # noqa: E741
W, M = 150, 400

# Calculate
qm = U * (1 - (C1 + H0 + G0 - V - O) / (X * (Y + G - V))) - U * (
    1 - (W + HG - V) / (X * (E - V))
)
qm = np.full_like(E, qm)

# Create the figure and axes objects
fig, (ax) = plt.subplots(figsize=(5, 4.5))

# Plot
ax.plot(E, qm, "--*", color="black", markersize=8, markerfacecolor="white")
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_minor_locator(MultipleLocator(50))
ax.yaxis.set_major_locator(MultipleLocator(2500))
ax.yaxis.set_minor_locator(MultipleLocator(1250))
ax.tick_params(which="major", length=3)
ax.tick_params(which="minor", length=1)
ax.set_xlabel("$e$", size=14)
ax.set_ylabel("$q_m$", size=14)
ax.tick_params(labelsize=14)
ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.grid(linestyle="-.", color="#696969")

# Show
ax.set_box_aspect(1)
fig.tight_layout()
plt.show()
