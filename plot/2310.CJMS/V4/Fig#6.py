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
@Descrip  : Fig.6 Reserves of government, manufacturer and supplier
"""

import matplotlib as mpl  # noqa: F401
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
from matplotlib.collections import PathCollection
from matplotlib.legend_handler import HandlerPathCollection, HandlerLine2D


# Initial settings
# mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "grid", "no-latex"])

# Grid data
X = 0.6
Y = np.array([75, 100, 125, 150, 175, 200, 225, 250])

# Set parameter values
U, MU = 20000, 10000
HG, H0, H1 = 12, 10, 5
C0, C1 = 25, 30
G0, G = 20, 25
V, S = 8, 5
O = 10  # noqa: E741
W, E, M = 150, 300, 400

# Calculate
Qg = U * (1 - (W + HG - V) / (X * (E - V)))
qm = U * (1 - (C1 + H0 + G0 - V - O) / (X * (Y + G - V))) - U * (
    1 - (W + HG - V) / (X * (E - V))
)
qs = U * (1 - (C0 + H1 - S - O) / (X * (Y - S))) - U * (
    1 - (C1 + H0 + G0 - V - O) / (X * (Y + G - V))
)
Qg = np.full_like(Y, Qg)
qm = np.full_like(Y, qm)
qs = np.full_like(Y, qs)

# Create the figure and axes objects
fig, (ax) = plt.subplots(figsize=(5, 4.5))

# Plot
ax.plot(Y, Qg, "--D", color="black", markersize=6, markerfacecolor="white")
ax.plot(Y, qm, "--H", color="black", markersize=8, markerfacecolor="white")
ax.plot(Y, qs, "--*", color="black", markersize=10, markerfacecolor="white")
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.xaxis.set_minor_locator(MultipleLocator(12.5))
ax.yaxis.set_major_locator(MultipleLocator(2000))
ax.yaxis.set_minor_locator(MultipleLocator(1000))
ax.yaxis.get_offset_text().set(size=14)
ax.tick_params(which="major", length=4)
ax.tick_params(which="minor", length=2)
ax.set_xlabel("$c_2$", size=20)
ax.set_ylabel("储备量", size=18, font="KaiTi")
ax.tick_params(labelsize=14)
ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.grid(linestyle="-.", color="#696969")


def update_scatter(handle, orig):
    handle.update_from(orig)
    handle.set_sizes([9])


def updateline(handle, orig):
    handle.update_from(orig)
    handle.set_markersize(9)


# Legend
## Create legend with line style
marker = ["D", "H", "*"]
legend_labels = ["$Q_g$", "$q_m$", "$q_s$"]
legend_handles = [
    Line2D([], [], marker=marker, color="black", label=label, markerfacecolor="white")
    for marker, label in zip(marker, legend_labels)
]

ax.legend(
    handler_map={
        PathCollection: HandlerPathCollection(update_func=update_scatter),
        plt.Line2D: HandlerLine2D(update_func=updateline),
    },
    handles=legend_handles,
    labels=legend_labels,
    fontsize=15,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    bbox_to_anchor=(0.64, 0.33),
    loc=3,
    borderaxespad=0,
)

# Show
ax.set_box_aspect(1)
fig.tight_layout()
plt.show()
