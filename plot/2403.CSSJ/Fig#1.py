"""
██████╗  █████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗      ██████╗ ████████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║     ██╔═══██╗╚══██╔══╝
██████╔╝███████║██████╔╝█████╗  ██████╔╝    ██████╔╝██║     ██║   ██║   ██║
██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ██╔═══╝ ██║     ██║   ██║   ██║
██║     ██║  ██║██║     ███████╗██║  ██║    ██║     ███████╗╚██████╔╝   ██║
╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝    ╚═╝
@Title    : 数量柔性契约下的政企三方联合储备决策研究
@Author   : GONG Lingjun, JIANG Xingyu
@Created  : 2024-03-05
@Revision : 2024-03-05
@Submit   : Nan
@Descrip  : Fig.1 Comparison of government reserves under two models
TODO: 调整坐标刻度
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

# Grid data X, Y and meshgrid. X -> \rho, Y -> w_1
X, Y = np.meshgrid(np.linspace(7 / 16, 1, 15), np.linspace(695 / 7, 225, 15))

# Set parameter values
U, MU = 20000, 10000
M = 300
C = 25
P0, P1 = 100, 250
W0 = 30
M0, M1 = 20, 25
HG, HM, HS = 15, 10, 5
S, V = 10, 5

# Calculate the values of Q_0, Q_cm
q0 = U * (1 - (P0 + HG - S) / (X * (M - S)))
qc = U * (1 - (P0 + HG - S) / (X * (P1 - S)))

benchmark_quantity_gov = q0
mainmodel_quantity_gov = qc

# Create the figure and axes objects
fig = plt.figure(figsize=(7, 5.5))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# Plot the surfaces
ax.plot_surface(X, Y, benchmark_quantity_gov, label="benchmark", color="#222222")
ax.plot_surface(X, Y, mainmodel_quantity_gov, label="mainModel", color="#666666")

ax.invert_xaxis()
ax.set_xlabel("$\\rho$", size=22, labelpad=10)
ax.set_ylabel("$w_1$", size=22, labelpad=10)
ax.tick_params(labelsize=18)
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_minor_locator(MultipleLocator(25))
ax.zaxis.set_major_locator(MultipleLocator(2000))
ax.zaxis.get_offset_text().set(size=18)
z_formatter = ScalarFormatter(useMathText=True)
z_formatter.set_scientific(True)
z_formatter.set_powerlimits((-2, 2))
z_axis = ax.get_zaxis()
z_axis.set_major_formatter(z_formatter)

# show legend
colors = ["#222222", "#666666"]
legend_labels = ["$Q_0$", "$Q_c$"]
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
    bbox_to_anchor=(1.14, 0.8),
)

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)
plt.setp(ax.get_zticklabels(), visible=False)

for x, text in zip(
    [0.5, 0.6, 0.7, 0.8, 0.9, 1.00], ["0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]
):
    ax.text(x=x, y=65, z=-256.8, s=text, fontsize=20)

for y, text in zip(
    [85, 109, 133, 157, 181, 205],
    ["100", "125", "150", "175", "200", "225"],
):
    ax.text(x=0.34, y=y, z=-256.8, s=text, fontsize=20)

for z, text in zip(
    [-600, 1400, 3400, 5400, 7400, 9400, 11400],
    ["0", "0.2", "0.4", "0.6", "0.8", "1.0", "1.2"],
):
    ax.text(x=0.37, y=234, z=z, s=text, fontsize=20)

# # Set the view angle and display the plot
ax.view_init(elev=28, azim=-45)
plt.show()
