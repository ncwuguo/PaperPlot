import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.lines import Line2D
from matplotlib.pyplot import MultipleLocator

# initial settings - set plot style
plt.style.use(["science", "no-latex"])

# define x and y axis ranges
x = np.arange(0, 1.05, 0.05)
y = np.arange(0, 1.05, 0.05)

# create 2D coordinate arrays from coordinate vectors
X, Y = np.meshgrid(x, y)

# define equations to plot
equations = [
    94 * X**2 + (-27 + X * (152 + 80.5 * X)) * Y - 89.5 * (1 + X) ** 2 * Y**2,
    93 * X**2 + (-24 + X * (154 + 81.0 * X)) * Y - 89.0 * (1 + X) ** 2 * Y**2,
    91 * X**2 + (-18 + X * (158 + 82.0 * X)) * Y - 88.0 * (1 + X) ** 2 * Y**2,
    89 * X**2 + (-12 + X * (162 + 83.0 * X)) * Y - 87.0 * (1 + X) ** 2 * Y**2,
]
# print(equations[1])

# define conditions for the contour plot
Z = np.where(X <= Y, np.where(np.where(X <= Y, equations, np.nan) > 0, 1, 0), np.nan)

# generate canvas
fig, ax1 = plt.subplots(figsize=(5, 3.8))

# define contour levels and colors
levels = np.array([-1, 0, 1])
linestyles = [":", "-.", "--", "-"]
colors = ["#999999", "#666666", "#333333", "#000000"]

# plot the contours
for i in range(len(equations)):
    ax1.contour(
        X,
        Y,
        Z[i],
        levels=levels,
        linestyles=linestyles[i],
        linewidths=1,
        colors=colors[i],
    )
# ax1.contour(X, Y, Z[i])
# plot y=x line
ax1.plot([0, 1], [0, 1], color="black")

# set plot labels, grid, and tick parameters
ax1.set_xlabel("$b_{0} $", size=16)
ax1.set_ylabel("$b_{1} $", size=16)
ax1.tick_params(labelsize=15)
ax1.xaxis.set_major_locator(MultipleLocator(0.2))
ax1.xaxis.set_minor_locator(MultipleLocator(0.1))
ax1.xaxis.set_major_locator(MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(MultipleLocator(0.1))
ax1.tick_params(which="major", length=4)
ax1.tick_params(which="minor", length=2)

# annotate the plot with text
ax1.annotate(r"$\frac{\partial q_{m}}{\partial b_{0}}>0$", fontsize=19, xy=(0.59, 0.41))
ax1.annotate(r"$\frac{\partial q_{m}}{\partial b_{0}}<0$", fontsize=19, xy=(0.13, 0.71))
ax1.annotate("", xy=(0.47, 0.57), xytext=(0.59, 0.45), arrowprops=dict(arrowstyle="->"))

# Create legend with colorbar
# legend_labels = ["$r=0.05$", "$r=0.10$", "$r=0.20$", "$r=0.30$"]
# legend_handles = [plt.Rectangle((0, 0), 1, 1, fc=color) for color in colors]

# Create legend with line style
legend_labels = ["$r=5\%$", "$r=10\%$", "$r=20\%$", "$r=30\%$"]
legend_handles = [
    Line2D([], [], linestyle=linestyle, color="black", label=label)
    for linestyle, label in zip(linestyles, legend_labels)
]

# show legend
ax1.legend(
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
ax1.set_box_aspect(1)

# show plot
fig.tight_layout()
plt.show()
