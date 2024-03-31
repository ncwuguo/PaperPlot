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

# 给出高度Z的值
ZQ_a = U * (1 - (w + hg - v) / (X * (M - v)))
ZQ_c = U * (1 - (w + hg - v) / (X * (e - v)))
ZQ_c_0_1 = U * (1 - (c0 + h1 - s - o) / (X * (Y - s)))

ax.plot_surface(X, Y, ZQ_a, label="单独储备", color="#79B8DF", alpha=0.9)
ax.plot_surface(X, Y, ZQ_c_0_1, label="联合储备", color="#EDA8A8", alpha=0.9)

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
legend_labels = ["$Q_a$", "$q_0+q_1+Q_a$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=13,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    bbox_to_anchor=(1.12, 0.96),
)

ax.view_init(elev=28, azim=-45)
plt.show()
