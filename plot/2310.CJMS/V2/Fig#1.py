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


# X -> \rho, Y -> c2
X, Y = np.meshgrid(np.linspace(51 / 98, 1, 15), np.linspace(1933 / 17, 375, 15))  # Grid the X and Y data

# Define the constants
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

# Calculate the values for the height Z
quantity_a = qa
quantity_m = qm
zero = 0 * X * Y

# Create the figure and axes objects
fig = plt.figure(figsize=(6.8, 5.5))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# Plot the surfaces
ax.plot_surface(X, Y, zero, label="Benchmark", color="#222222")
ax.plot_surface(X, Y, quantity_m - quantity_a, color="#666666")


ax.invert_xaxis()
ax.set_xlabel("$\\rho $", size=26, labelpad=8)
ax.set_ylabel("$c_2$", size=26, labelpad=8)
ax.tick_params(labelsize=18)
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_locator(MultipleLocator(25))
ax.zaxis.get_offset_text().set(size=18)
z_formatter = ScalarFormatter(useMathText=True)
z_formatter.set_scientific(True)
z_formatter.set_powerlimits((-2, 2))
z_axis = ax.get_zaxis()
z_axis.set_major_formatter(z_formatter)

# show the legend
colors = ["#666666", "#222222"]
legend_labels = ["$q_m$", "$q_a$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=17,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    bbox_to_anchor=(1.12, 0.94),
)

# Set the view angle and display the plot
ax.view_init(elev=28, azim=-45)
plt.show()
