import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D


plt.style.use(["science", "grid", "no-latex"])

fig = plt.figure(figsize=(6.8, 5.5))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# X -> \rho, Y -> c2
X = np.arange(51 / 98, 1, 0.1)
Y = np.arange(1933 / 17, 375, 1)
# 对下x,y数据执行网格化
X, Y = np.meshgrid(X, Y)

U = 20000
mu = 10000
h0 = 10
h1 = 5
hg = 12
c0 = 25
c1 = 30
g0 = 20
g = 25
v = 5
s = 5
w = 150
M = 400
o = 10
e = 300

Qc = U * (1 - (w + hg - v) / (X * (e - v)))
q0 = U * (1 - (c1 + h0 + g0 - v - o) / (X * (Y + g - v))) - U * (
    1 - (w + hg - v) / (X * (e - v))
)
q1 = U * (1 - (c0 + h1 - s) / (X * (Y - s))) - U * (
    1 - (c1 + h0 + g0 - v - o) / (X * (Y + g - v))
)
Qa = U * (1 - (w + hg - v) / (X * (M - v)))

# 给出高度Z的值
Zas = Qa * (c1 - c0)
Zs = (
    (c1 - c0) * Qc
    + (c1 - c0) * q0
    + (s + o - c0 - h1) * q1
    + X * (Y - s) * (q1 - ((Qc + q0 + q1) ** 2 - (Qc + q0) ** 2) / (2 * U))
)
Zam = Qa * (w - c1 - g0)
Zm = (
    (w - c1 - g0) * Qc
    + (v + o - c1 - h0 - g0) * q0
    + X
    * (
        (e - v) * (q0 - ((Qc + q0) ** 2 - (Qc) ** 2) / (2 * U))
        + (e - Y - g) * (q1 - ((Qc + q0 + q1) ** 2 - (Qc + q0) ** 2) / (2 * U))
    )
)
Zag = (w + hg - v) * Qa + X * M * mu + X * (v - M) * (Qa - (Qc**2) / (2 * U))
Zg = (
    Qc * (w + hg - v)
    + X * v * Qc
    + X
    * (
        (-v * (Qc**2)) / (2 * U)
        + e * (q0 + q1)
        - e * (((Qc + q0 + q1) ** 2 - (Qc) ** 2) / (2 * U))
        + M * (mu - Qc - q0 - q1 + ((Qc + q0 + q1) ** 2) / (2 * U))
    )
)


ax.plot_surface(X, Y, Zm, label="单独储备", color="#79B8DF", alpha=0.9)
ax.plot_surface(X, Y, Zam, label="联合储备", color="#EDA8A8", alpha=0.9)
ax.invert_xaxis()
ax.set_xlabel("$\\rho $", size=16, labelpad=10)
ax.set_ylabel("$c_2$", size=16, labelpad=10)
ax.tick_params(labelsize=15)
ax.zaxis.get_offset_text().set(size=14)
z_formatter = ScalarFormatter(useMathText=True)
z_formatter.set_scientific(True)
z_formatter.set_powerlimits((-2, 2))
z_axis = ax.get_zaxis()
z_axis.set_major_formatter(z_formatter)


# show legend
# ax.legend()
colors = ["#79B8DF", "#EDA8A8"]
legend_labels_1 = ["$E\\pi_s$", "$E\\pi_{as}$"]
legend_labels_2 = ["$E\\pi_m$", "$E\\pi_{am}$"]
legend_labels_3 = ["$EC_g$", "$EC_{ag}$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels_2,
    fontsize=13,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    bbox_to_anchor=(0.91, 0.82),
    loc=3,
    borderaxespad=0,
)

ax.view_init(elev=28, azim=-45)
plt.show()
