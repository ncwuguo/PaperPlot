"""
@File     : Fig_3.6#1_Corollary3.1-lambda.py
@Created  : 2023/12/05 17:21
@Revision : 2023/12/05 17:22
@Author   : GuoKeing
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

config = {
    "mathtext.fontset": "stix",
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "font.sans-serif": ["KaiTi"],  # 用来正常显示中文标签
    "axes.unicode_minus": False,  # 用来正常显示负号
    "xtick.direction": "in",  # 将x周的刻度线方向设置向内
    "ytick.direction": "in",  # 将y轴的刻度方向设置向内
    # "font.size": 15,
}
plt.rcParams.update(config)

# 绘制画布
fig = plt.figure()
# 将默认figure图转化为3D图
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# 给出x，y轴的数据列表
X = np.arange(10, 15.2, 0.2)
Y = np.arange(0, 0.502, 0.02)
X, Y = np.meshgrid(X, Y)

Z = -0.224467 * (3 + 0.6 * (-199 + X) - 3 * Y * X)

surf = ax.plot_surface(X, Y, Z, cmap=plt.get_cmap("rainbow"), vmin=24.0, vmax=29.6)
# zdir后的参数决定从哪个方位进行投影 offset的参数表示投影到该方位坐标的哪个点对应的坐标平面
# ax.contourf(X, Y, Z, zdir='z', offset=8, cmap='gray_r')

# 限制画图的坐标轴范围
# ax.set_zlim(8, 25)
# ax.invert_xaxis()  # x轴反向
ax.set_title("成本c与税率r对公司M在海南产量的影响", font="KaiTi")
ax.set_xlabel("$c$", fontsize=14)
ax.set_ylabel("$r$", fontsize=14)
plt.colorbar(surf, shrink=0.7)
x1_label = ax.get_xticklabels()
[x1_label_temp.set_fontname("Times New Roman") for x1_label_temp in x1_label]
y1_label = ax.get_yticklabels()
[y1_label_temp.set_fontname("Times New Roman") for y1_label_temp in y1_label]
z1_label = ax.get_zticklabels()
[z1_label_temp.set_fontname("Times New Roman") for z1_label_temp in z1_label]

plt.show()
