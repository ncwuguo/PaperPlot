import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator, ScalarFormatter
from mpl_toolkits.mplot3d import Axes3D

# Set the plot style
# mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "grid", "no-latex"])
# X -> \rho, Y -> c2
X = np.linspace(51 / 98, 1, 20)
Y = np.linspace(1933 / 17, 375, 80)
X, Y = np.meshgrid(X, Y)

# Define constants
U = 20000
MU = 10000
H0 = 10
H1 = 5
HG = 12
C0 = 25
C1 = 30
G0 = 20
G = 25
V = 8
S = 5
W = 150
M = 400
O = 10  # noqa: E741
E = 300

# Calculate the values for Qg, qm, qs, Qa, and qa
Qg = U * (1 - (W + HG - V) / (X * (E - V)))
qm = U * (1 - (C1 + H0 + G0 - V - O) / (X * (Y + G - V))) - Qg
qs = U * (1 - (C0 + H1 - S) / (X * (Y - S))) - qm - Qg
Qa = U * (1 - (W + HG - V) / (X * (E - V)))
qa = U * (1 - (C1 + G0 + H0 - V) / (X * (E - V))) - Qa

# 给出高度Z的值
cost_gov_benchmark = (W + HG - V + X * V) * Qa + X * (
    (-V * (Qa**2)) / (2 * U)
    - E * (((Qa + qa) ** 2 - Qa**2) / (2 * U))
    + E * qa
    + M * (MU - Qa - qa + ((Qa + qa) ** 2) / (2 * U))
)
cost_gov_mainmodel = (
    Qg * (W + HG - V)
    + X * V * Qg
    + X
    * (
        (-V * (Qg**2)) / (2 * U)
        + E * (qm + qs)
        - E * (((Qg + qm + qs) ** 2 - Qg**2) / (2 * U))
        + M * (MU - Qg - qm - qs + ((Qg + qm + qs) ** 2) / (2 * U))
    )
)
main_max = np.where(
    cost_gov_mainmodel > cost_gov_benchmark, cost_gov_mainmodel, np.nan
)
bench_max = np.where(
    cost_gov_benchmark > cost_gov_mainmodel, cost_gov_benchmark, np.nan
)
main_min = np.where(
    cost_gov_mainmodel < cost_gov_benchmark, cost_gov_mainmodel, np.nan
)
bench_min = np.where(
    cost_gov_benchmark < cost_gov_mainmodel, cost_gov_benchmark, np.nan
)

# Create the figure and axes objects
fig = plt.figure(figsize=(6.8, 5.5))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# Plot the surfaces
ax.plot_surface(X, Y, main_max, color="#222222")
ax.plot_surface(X, Y, bench_max, color="#666666")
ax.plot_surface(X, Y, main_min, color="#222222")
ax.plot_surface(X, Y, bench_min, color="#666666")
ax.invert_xaxis()
ax.set_xlabel("$\\rho $", size=26, labelpad=10)
ax.set_ylabel("$c_2$", size=26, labelpad=10)
ax.tick_params(labelsize=18)
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_locator(MultipleLocator(25))
ax.zaxis.set_minor_locator(MultipleLocator(100000))
ax.zaxis.get_offset_text().set(size=18)
z_formatter = ScalarFormatter(useOffset=None, useMathText=True, useLocale=2)
z_formatter.set_scientific(True)
z_formatter.set_powerlimits((-2, 2))
z_axis = ax.get_zaxis()
z_axis.set_major_formatter(z_formatter)

# show legend
colors = ["#79B8DF", "#EDA8A8"]
legend_labels = ["$EC_g$", "$EC_{ag}$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=15,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    bbox_to_anchor=(1.12, 0.95),
)

ax.view_init(elev=20, azim=-45)
plt.show()
