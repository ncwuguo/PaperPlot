"""
@File     : Fig_3.6#1_Corollary3.1-lambda.py
@Created  : 2023/12/05 17:21
@Revision : 2023/12/05 17:22
@Author   : GuoKeing
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.ticker import MultipleLocator

# initial settings
mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "grid", "no-latex"])

# define axis ranges and meshgrid
_x = np.arange(10, 15.2, 0.2)
_y = np.arange(0, 0.702, 0.02)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# z is the bottom starting value of 3dbar, top is the true height of 3dbar
z = 23.5
top = -0.224467 * (3 + 0.6 * (-199 + x) - 3 * y * x) - z

# define colors
norm = plt.Normalize(top.min(), top.max())
colors = plt.cm.gray_r(norm(top))

# The ratio of width and depth should be the same as the ratio of x and y
width = 0.08
depth = 0.008

# set up the figure and axes
fig = plt.figure(figsize=(5.5, 5))
ax = fig.add_subplot(111, projection="3d")


ax.bar3d(x, y, z, width, depth, top, colors, shade=True)
ax.invert_xaxis()
ax.set_xlabel("原材料成本 $c$", size=15, font="KaiTi", labelpad=8)
ax.set_ylabel("关税税率 $r$", size=15, font="KaiTi", labelpad=8)
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.zaxis.set_minor_locator(MultipleLocator(1))
ax.tick_params(labelsize=17)

# show plot
fig.tight_layout()
plt.margins(0, 0, 0)
ax.view_init(elev=30, azim=-40)
plt.show()
