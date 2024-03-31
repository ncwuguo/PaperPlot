import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D

plt.style.use(["science", "no-latex"])


# 绘制画布
fig = plt.figure(figsize=(7.3, 6))
# 将默认figure图转化为3D图
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

U, w, M, p, c, p1, c1 = 20000, 60, 200, 30, 20, 25, 4
v1, v, c2, h, h1, m, e = 5, 8, 30, 10, 8, 10, 150

# 给出x，y轴的数据列表
X = np.arange(0.4, 1, 0.1)
Y = np.arange(105, 120, 1)
# 对下x,y数据执行网格化
X, Y = np.meshgrid(X, Y)
# 给出高度Z的值
QA = U * (1 - (60 + 10 - 8) / (X * (200 - 8)))
Q0 = U * (1 - (w + h - v - m) / (X * (e - v)))
Q1 = U * (1 - (c + h + v1 - v - h1) / (X * (c2 + v1 - v))) - Q0
Q2 = U * (1 - (h1 + p - v) / (X * (Y - v1))) - U * (
    1 - (c + h + v1 - v - h1) / (X * (c2 + v1 - v))
)
Q3 = U * (1 - (p1 + c1 + h1 - v1) / (X * (Y - v1))) - Q0 - Q1 - Q2
ZS = w * QA - (p + c) * QA
ZJ = (
    w * Q0
    - (p + c) * (Q0 + Q1)
    - h * Q1
    - h1 * Q2
    - p * Q2
    + (1 - X) * (v * Q1 + v1 * Q2)
    + m * (Q1 + Q2 + Q3)
    + X
    * (
        -(e - v) * ((Q0 + Q1) ** 2 - (Q0) ** 2) / 2 / U
        - (e - c2 - v1) * ((Q0 + Q1 + Q2) ** 2 - (Q0 + Q1) ** 2) / 2 / U
        - (e - Y - c2) * ((Q0 + Q1 + Q2 + Q3) ** 2 - (Q0 + Q1 + Q2) ** 2) / 2 / U
        + e * (Q1 + Q2 + Q3)
        - c2 * (Q2 + Q3)
        - Y * Q3
    )
)

surf1 = ax.plot_surface(X, Y, ZS, label="政企联合储备", color="#79B8DF", alpha=0.9)
surf2 = ax.plot_surface(X, Y, ZJ, label="政府单独储备", color="#EDA8A8", alpha=0.9)


ax.invert_xaxis()
ax.set_xlabel("$\\theta $", size=16, labelpad=10)
ax.set_ylabel("$p_2$", size=16, labelpad=10)
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
legend_labels = ["$E[\\pi_m^S]$", "$E[\\pi_m^J]$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=12,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    bbox_to_anchor=(1.1, 0.93),
    # loc=3,
    # borderaxespad=0,
)


plt.show()
