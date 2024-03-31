"""
@File     : Fig_3.6#1_Corollary3.1-lambda.py
@Created  : 2023/12/05 17:21
@Revision : 2023/12/05 17:22
@Author   : GuoKeing
"""

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from matplotlib import ticker
from matplotlib.ticker import MultipleLocator

# initial settings - set plot style
plt.style.use(["science", "no-latex"])

# create numerical sequences
# np.round(np.linspace(i, j, t), decimals=n), Avoid decimal precision issues
t = np.round(np.linspace(1, 2, 11), decimals=1)
c = np.linspace(10, 15, 6)
a = np.linspace(100, 200, 11)
r = np.array([0, 0.02, 0.03, 0.05, 0.07, 0.1, 0.17, 0.25, 0.35, 0.5, 0.7])
b0 = np.round(np.linspace(0.1, 0.9, 9), decimals=1)
b1 = np.round(np.linspace(0.2, 1.0, 9), decimals=1)

# create meshgrid from the numerical sequences
T, R, B0, B1, C, A = np.meshgrid(t, r, b0, b1, c, a, indexing="ij")

# define condition and euqation
condition = B1 > B0
# equation: quantity of firm MNC minus firm LM
equation = B0 * (A - C - T) - B1 * (A - C - C * R) + 3 * (C * R - T)

# The impact of b1 on the equilibrium quantity gap
b1_gap = np.where(condition, equation, np.nan)
b1_abs_dict = {
    b1_val: np.where(
        b1_gap[B1 == b1_val] > 0, 1, np.where(b1_gap[B1 == b1_val] < 0, 0, np.nan)
    )
    for b1_val in b1
}
b1_mean = np.array([np.nanmean(b1_abs_dict[b1_val]) for b1_val in b1_abs_dict])

# The impact of a on the equilibrium quantity gap
a_gap = np.where(condition, equation, np.nan)
a_abs_dict = {}
for a_val in a:
    a_arr = a_gap[A == a_val]
    a_abs = np.where(a_arr > 0, 1, np.where(a_arr < 0, 0, np.nan))
    a_abs_dict[a_val] = a_abs
a_mean = np.array([np.nanmean(a_abs_dict[a_val]) for a_val in a_abs_dict])

# The impact of r on the equilibrium quantity gap
r_gap = np.where(condition, equation, np.nan)
r_abs_dict = {}
for r_val in r:
    r_arr = r_gap[R == r_val]
    r_abs = np.where(r_arr > 0, 1, np.where(r_arr < 0, 0, np.nan))
    r_abs_dict[r_val] = r_abs
r_mean = np.array([np.nanmean(r_abs_dict[r_val]) for r_val in r_abs_dict])

# The impact of t on the equilibrium quantity gap
t_gap = np.where(condition, equation, np.nan)
t_abs_dict = {}
for t_val in t:
    t_arr = t_gap[T == t_val]
    t_abs = np.where(t_arr > 0, 1, np.where(t_arr < 0, 0, np.nan))
    t_abs_dict[t_val] = t_abs
t_mean = np.array([np.nanmean(t_abs_dict[t_val]) for t_val in t_abs_dict])

# generate canvas
fig, (ax1, ax2, ax3, ax4) = plt.subplots(figsize=(13.2, 3.3), nrows=1, ncols=4)

# set props
props_font_label = fm.FontProperties("KaiTi", size=12)
# props_font_title = fm.FontProperties("SimSun", size=13)
# props_title = [
#     "(i)海南规模不经济程度的变化",
#     "(ii)市场规模的变化",
#     "(iii)关税税率的变化",
#     "(iv)运输成本的变化",
# ]
props_xlabels = [
    r"规模不经济系数 $b_1$",
    r"市场规模 $a$",
    r"关税税率 $r$",
    r"运输成本 $t$",
]
props_ylabels = [r"$P\left \{ q ̃_m^*>q ̃_l^* \right \}$"]

# plot of ax1 about b1 and b1_mean
ax1.plot(b1, b1_mean, "--*", color="black", markersize=8, markerfacecolor="white")
# ax1.set_title(props_title[0], fontproperties=props_font_title)
ax1.set_xlabel(props_xlabels[0], fontproperties=props_font_label)
ax1.set_ylabel(props_ylabels[0], fontproperties=props_font_label)
ax1.yaxis.set_minor_locator(MultipleLocator(0.01))

# plot of ax2 about a and a_mean
ax2.plot(a, a_mean, "--*", color="black", markersize=8, markerfacecolor="white")
# ax2.set_title(props_title[1], fontproperties=props_font_title)
ax2.set_xlabel(props_xlabels[1], fontproperties=props_font_label)
ax2.xaxis.set_minor_locator(MultipleLocator(5))
ax2.xaxis.set_major_locator(MultipleLocator(20))
ax2.yaxis.set_minor_locator(MultipleLocator(0.005))

# plot of ax3 about r and r_mean
ax3.plot(r, r_mean, "--*", color="black", markersize=8, markerfacecolor="white")
# ax3.set_title(props_title[2], fontproperties=props_font_title)
ax3.set_xlabel(props_xlabels[2], fontproperties=props_font_label)
ax3.xaxis.set_major_locator(MultipleLocator(0.15))
ax3.yaxis.set_minor_locator(MultipleLocator(0.025))

# plot of ax4 about t and t_mean
ax4.plot(t, t_mean, "--*", color="black", markersize=8, markerfacecolor="white")
# ax4.set_title(props_title[3], fontproperties=props_font_title)
ax4.set_xlabel(props_xlabels[3], fontproperties=props_font_label)
ax4.xaxis.set_major_locator(MultipleLocator(0.2))
ax4.yaxis.set_minor_locator(MultipleLocator(0.0015))


# set same properties for axes
axes = [ax1, ax2, ax3, ax4]
for ax in axes:
    ax.set_box_aspect(1)
    ax.tick_params(labelsize=11)
    ax.grid(linestyle="-.", color="#696969")
    ax.tick_params(which="major", length=4)
    ax.tick_params(which="minor", length=2)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax3.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax4.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))

# show plot
fig.tight_layout()
plt.show()
