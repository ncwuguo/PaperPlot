"""
@File     : Fig_3.6#1_Corollary3.1-lambda.py
@Created  : 2023/12/05 17:21
@Revision : 2023/12/05 17:22
@Author   : GuoKeing
"""

import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import scienceplots  # noqa: F401
from matplotlib.ticker import MultipleLocator

# initial settings
mpl.rcParams["svg.fonttype"] = "none"
plt.style.use(["science", "no-latex"])

# define axis ranges for x and y
x = np.linspace(1.1, 2, 10)
price = 101.053 - (10.6787) / (0.672515 + x)
profit = (2079.25 + x * (5323 + 3426.7 * x)) / ((0.672515 + x) ** 2)

# set up the figure and axes
fig, (ax1, ax2) = plt.subplots(figsize=(7.5, 3.55), ncols=2)

# set props
props_font_label = fm.FontProperties("KaiTi", size=12)
# props_font_title = fm.FontProperties("SimSun", size=12)

# plot of ax1 about the x and price
ax1.plot(x, price, "--*", markersize=8, color="black", markerfacecolor="white")
# ax1.set_title("(i)$b_{1}$对市场均衡价格的影响", fontproperties=props_font_title)
ax1.set_xlabel(r"海南加工劣势系数 $\lambda$", fontproperties=props_font_label)
ax1.set_ylabel(r"市场均衡价格 $p^*$", fontproperties=props_font_label)
ax1.tick_params(labelsize=12)
ax1.xaxis.set_major_locator(MultipleLocator(0.2))
ax1.xaxis.set_minor_locator(MultipleLocator(0.1))
ax1.yaxis.set_major_locator(MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(MultipleLocator(0.25))
ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter("%.2f"))
ax1.grid(linestyle="-.", color="#696969")

# plot of ax2 about the x and profit
ax2.plot(x, profit, "--*", markersize=8, color="black", markerfacecolor="white")
# ax2.set_title("(ii)$b_{1}$对跨国公司总利润的影响", fontproperties=props_font_title)
ax2.set_xlabel(r"海南加工劣势系数 $\lambda$", fontproperties=props_font_label)
ax2.set_ylabel(r"跨国公司总利润 $\pi_M^B$", fontproperties=props_font_label)
ax2.tick_params(labelsize=12)
ax2.xaxis.set_major_locator(MultipleLocator(0.2))
ax2.xaxis.set_minor_locator(MultipleLocator(0.1))
ax2.yaxis.set_major_locator(MultipleLocator(25))
ax2.yaxis.set_minor_locator(MultipleLocator(12.5))
ax2.grid(linestyle="-.", color="#696969")

# set axes aspect ratio
ax1.set_box_aspect(1)
ax2.set_box_aspect(1)

# show plot
fig.tight_layout()
plt.show()
