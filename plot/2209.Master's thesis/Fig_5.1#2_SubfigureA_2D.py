"""
@File     : Fig_3.6#1_Corollary3.1-lambda.py
@Created  : 2023/12/05 17:21
@Revision : 2023/12/05 17:25
@Author   : GuoKeing
"""

import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib import ticker
from matplotlib.ticker import MultipleLocator

# initial settings
# mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "no-latex"])

X, Y = np.meshgrid(np.arange(0, 0.7, 0.02), np.arange(10, 15.2, 0.2))
# a=200; b=0.6; t=1; lambda=4/3
Z = -0.224467 * (3 + 0.6 * (-199 + Y) - 3 * Y * X)

# set up the figure and axes
fig, ax = plt.subplots(figsize=(5.5, 5))

# set props
props_font_label = fm.FontProperties("KaiTi", size=19)
props_xlabels = [r"关税税率 $r$"]
props_ylabels = [r"原材料单位成本 $c$"]

# plot
cs = ax.contourf(X, Y, Z, cmap=plt.get_cmap("gray_r"))

ax.xaxis.set_major_locator(MultipleLocator(0.15))
ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))

ax.tick_params(which="major", length=4)
ax.tick_params(which="minor", length=2)

plt.xlabel(props_xlabels[0], fontproperties=props_font_label)
plt.ylabel(props_ylabels[0], fontproperties=props_font_label)

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# add colorbar
cbar = fig.colorbar(cs)
cbar.ax.tick_params(labelsize=18)

# show plot
fig.tight_layout()
plt.show()
