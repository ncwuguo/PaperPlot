"""
@File     : Fig_3.6#1_Corollary3.1-lambda.py
@Created  : 2023/12/05 17:21
@Revision : 2023/12/05 17:22
@Author   : GuoKeing
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scienceplots  # noqa: F401

plt.style.use(["science", "grid", "no-latex"])
plt.rcParams["svg.fonttype"] = "none"


# 绘制画布
fig = plt.figure(figsize=(5, 4))
# 将默认figure图转化为3D图
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# 给出x，y轴的数据列表
X = np.arange(10, 15.2, 0.2)
Y = np.arange(0, 0.502, 0.02)
# 对下x,y数据执行网格化
X, Y = np.meshgrid(X, Y)
# 给出高度Z的值
Z = -0.224467 * (3 + 0.6 * (-199 + X) - 3 * Y * X)

surf = ax.plot_surface(X, Y, Z, cmap=plt.get_cmap("rainbow"), vmin=24.0, vmax=29.0)


ax.invert_xaxis()
ax.set_xlabel("$c$", size=9)
ax.set_ylabel("$r$", size=9)
# plt.colorbar(surf, shrink=0.7)
plt.tick_params(labelsize=9)

plt.show()
