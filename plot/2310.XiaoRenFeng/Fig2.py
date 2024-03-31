import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D

plt.style.use(["science", "no-latex"])


# 绘制画布
fig = plt.figure(figsize=(6.6, 5.5))
# 将默认figure图转化为3D图
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# 给出x，y轴的数据列表
X = np.arange(0.4, 1, 0.1)
Y = np.arange(105, 120, 1)
# 对下x,y数据执行网格化
X, Y = np.meshgrid(X, Y)
# 给出高度Z的值

ZS = 20000 * (1 - (60 + 10 - 8) / (X * (200 - 8)))
ZJ = 20000 * (1 - (60 + 10 - 8 - 10) / (X * (150 - 8)))

surf1 = ax.plot_surface(X, Y, ZJ, label="政企联合储备", color="#79B8DF", alpha=0.9)
surf2 = ax.plot_surface(X, Y, ZS, label="政府单独储备", color="#EDA8A8", alpha=0.9)


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
legend_labels = ["$Q_0$", "$Q_a$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=13,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    bbox_to_anchor=(1.12, 0.95),
    # loc=3,
    # borderaxespad=0,
)


plt.show()
