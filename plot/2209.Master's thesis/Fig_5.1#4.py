"""
@File     : Fig_3.6#1_Corollary3.1-lambda.py
@Created  : 2023/12/05 17:21
@Revision : 2023/12/05 17:22
@Author   : GuoKeing
"""

import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.lines import Line2D
from matplotlib.pyplot import MultipleLocator

# initial settings
mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "no-latex"])

# X: b, Y: lambda
X, Y = np.meshgrid(np.linspace(0.1, 1, 10), np.linspace(1, 3, 10))

# define equations: a=300, c=10, t=3
equations = [
    (
        291.6 * X**2
        + X * (-13.8 + 564.8 * X + 284.7 * X**2) * Y
        - 289.3 * X**2 * (1 + X) ** 2 * Y**2
    )
    / (X * (3 + 2 * X) + X * (1 + X) * (3 + X) * Y) ** 2,
    (
        290.0 * X**2
        + X * (-9 + 568 * X + 285.5 * X**2) * Y
        - 288.5 * X**2 * (1 + X) ** 2 * Y**2
    )
    / (X * (3 + 2 * X) + X * (1 + X) * (3 + X) * Y) ** 2,
    (
        287.0 * X**2
        + X * (574.0 * X + 287.0 * X**2) * Y
        - 287.0 * X**2 * (1 + X) ** 2 * Y**2
    )
    / (X * (3 + 2 * X) + X * (1 + X) * (3 + X) * Y) ** 2,
    (
        281.0 * X**2
        + X * (18 + 586 * X + 290 * X**2) * Y
        - 284 * X**2 * (1 + X) ** 2 * Y**2
    )
    / (X * (3 + 2 * X) + X * (1 + X) * (3 + X) * Y) ** 2,
]

# set up the figure and axes
fig, ax = plt.subplots(figsize=(5, 3.8))

# define contour levels and colors
levels = np.array([0])
linestyles = [":", "--", "-.", "-"]
colors = ["#999999", "#666666", "#333333", "#000000"]

# plot the contours
for i, equation in enumerate(equations):
    ax.contour(
        X,
        Y,
        equations[i],
        levels=levels,
        linestyles=linestyles[i],
        linewidths=1,
        colors=colors[i],
    )

# set plot labels, grid, and tick parameters
props_font_label = fm.FontProperties("KaiTi", size=14)
ax.set_xlabel(r"内地规模不经济系数 $b$", fontproperties=props_font_label)
ax.set_ylabel(r"海南加工劣势系数 $\lambda$", fontproperties=props_font_label)

ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

ax.tick_params(labelsize=15)
ax.tick_params(which="major", length=4)
ax.tick_params(which="minor", length=2)

# annotate the plot with text
ax.annotate(r"$\frac{\partial q_m^B}{\partial b}>0$", fontsize=19, xy=(0.2, 1.2))
ax.annotate(r"$\frac{\partial q_m^B}{\partial b}<0$", fontsize=19, xy=(0.55, 2.2))
# ax.annotate("", xy=(0.47, 0.57), xytext=(0.59, 0.45), arrowprops=dict(arrowstyle="->"))

# Create legend with colorbar
# legend_labels = ["$r=0.05$", "$r=0.10$", "$r=0.20$", "$r=0.30$"]
# legend_handles = [plt.Rectangle((0, 0), 1, 1, fc=color) for color in colors]

# Create legend with line style
legend_labels = ["$r=7\%$", "$r=15\%$", "$r=30\%$", "$r=60\%$"]
legend_handles = [
    Line2D([], [], linestyle=linestyle, color="black", label=label)
    for linestyle, label in zip(linestyles, legend_labels)
]

# show legend
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=12,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    bbox_to_anchor=(1.05, 0.3),
    loc=3,
    borderaxespad=0,
)

# set axes aspect ratio
ax.set_box_aspect(1)

# show plot
fig.tight_layout()
plt.show()
