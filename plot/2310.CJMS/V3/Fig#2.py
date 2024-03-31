"""
██████╗  █████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗      ██████╗ ████████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║     ██╔═══██╗╚══██╔══╝
██████╔╝███████║██████╔╝█████╗  ██████╔╝    ██████╔╝██║     ██║   ██║   ██║
██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ██╔═══╝ ██║     ██║   ██║   ██║
██║     ██║  ██║██║     ███████╗██║  ██║    ██║     ███████╗╚██████╔╝   ██║
╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝    ╚═╝
@Title    : 混合契约下应急物资政企三级联合储备模型研究
@Author   : GUO Keting, GONG Lingjun
@Created  : 2023-10-19
@Revision : 2024-03-20
@Submit   : Nan
@Descrip  : Fig.2 Comparison of manufacturer's stock
"""

import matplotlib as mpl  # noqa: F401
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator, ScalarFormatter
from mpl_toolkits.mplot3d import Axes3D

# initial settings
# mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "grid", "no-latex"])

# Grid data X, Y and meshgrid. X -> \rho, Y -> c2
X, Y = np.meshgrid(np.linspace(51 / 98, 1, 50), np.linspace(1933 / 17, 275, 50))

# Set parameter values
U, MU = 20000, 10000
H0, H1, HG = 10, 5, 12
C0, C1 = 25, 30
G0, G = 20, 25
V, S = 8, 5
W = 150
M = 400
O = 10  # noqa: E741
W, E, M = 150, 300, 400

# Calculate the values for Qg, qm, qs, Qa, and qa
Qg = U * (1 - (W + HG - V) / (X * (E - V)))
qm = U * (1 - (C1 + H0 + G0 - V - O) / (X * (Y + G - V))) - Qg
qs = U * (1 - (C0 + H1 - S) / (X * (Y - S))) - qm - Qg
Qa = U * (1 - (W + HG - V) / (X * (E - V)))
qa = U * (1 - (C1 + G0 + H0 - V) / (X * (E - V))) - Qa

# Calculate the values for the height Z
quantity_b = qa
quantity_m = qm
benchmark_quantity_max = np.where(qa >= qm, qa, np.nan)
benchmark_quantity_min = np.where(qa <= qm, qa, np.nan)
mainmodel_quantity_max = np.where(qm >= qa, qm, np.nan)
mainmodel_quantity_min = np.where(qm <= qa, qm, np.nan)

# Create the figure and axes objects
fig = plt.figure(figsize=(7, 5.5))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# Plot the surfaces
ax.plot_surface(X, Y, benchmark_quantity_max, color="#111111", shade=False)
ax.plot_surface(X, Y, benchmark_quantity_min, color="#111111", shade=False)
ax.plot_surface(X, Y, mainmodel_quantity_max, color="#888888", shade=False)
ax.plot_surface(X, Y, mainmodel_quantity_min, color="#888888", shade=False)

ax.invert_xaxis()
ax.set_xlabel("$\\rho$", size=22, labelpad=10)
ax.set_ylabel("$c_2$", size=22, labelpad=10)
ax.tick_params(labelsize=18)
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(30))
ax.yaxis.set_minor_locator(MultipleLocator(30))
ax.zaxis.get_offset_text().set(size=18)
z_formatter = ScalarFormatter(useMathText=True)
z_formatter.set_scientific(True)
z_formatter.set_powerlimits((-2, 2))
z_axis = ax.get_zaxis()
z_axis.set_major_formatter(z_formatter)

# show the legend
colors = ["#111111", "#888888"]
legend_labels = ["$q_a$", "$q_m$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=20,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    loc="lower right",
    bbox_to_anchor=(1.15, 0.78),
)

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)
plt.setp(ax.get_zticklabels(), visible=False)

for x, text in zip(
    [0.5, 0.6, 0.7, 0.8, 0.9, 1.00], ["0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]
):
    ax.text(x=x, y=72, z=3900.06, s=text, fontsize=20)

for y, text in zip(
    [100, 130, 160, 190, 220, 250],
    ["120", "150", "180", "210", "240", "270"],
):
    ax.text(x=0.44, y=y, z=3900.06, s=text, fontsize=20)

for z, text in zip(
    [6200, 8200, 10200, 12200, 14200],
    ["0.6", "0.8", "1.0", "1.2", "1.4"],
):
    ax.text(x=0.43, y=270, z=z, s=text, fontsize=20)

# Set the view angle and display the plot
ax.view_init(elev=28, azim=-45)
plt.show()
