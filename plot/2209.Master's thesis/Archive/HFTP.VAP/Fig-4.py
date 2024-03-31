import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as mtick
import numpy as np
import scienceplots  # noqa: F401


# initial settings - set plot style
plt.style.use(["science", "no-latex"])

# define axis ranges for x
x = np.linspace(0.2, 1, 9)
# define equations for price and profit
price = (122.96 + 425.6 * x) / (1.52 + 4.76 * x)
profit = (
    178857
    + 319992 * x
    + 212064 * x**2
    + 31185 * (2 + x)
    + x * (-207 + 70688 * x)
    + x * (289014 + 141376 * x)
) / (2 * (5 + 8 * x) ** 2)

# generate canvas
fig, (ax1, ax2) = plt.subplots(figsize=(7.9, 3.5), ncols=2)

# set props
props_font_label = fm.FontProperties("Simsun", size=12)
props_font_title = fm.FontProperties("Simsun", size=12)

# plot of ax1 about the x and price
ax1.plot(x, price, linestyle="--", marker="^", color="black", markerfacecolor="white")
ax1.set_title("(i)$b_{1}$对市场均衡价格的影响", fontproperties=props_font_title)
ax1.set_xlabel(r"$b_{1}$", size=12)
ax1.set_ylabel("市场均衡价格", fontproperties=props_font_label)
ax1.tick_params(labelsize=11)
ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter("%.2f"))
# ax1.grid(linestyle='-.')
# ax1.fill_between(x, 85.5, price, facecolor='#81b8df', alpha=0.618)

# plot of ax2 about the x and profit
ax2.plot(x, profit, linestyle="--", marker="^", color="black", markerfacecolor="white")
ax2.set_title("(ii)$b_{1}$对跨国公司总利润的影响", fontproperties=props_font_title)
ax2.set_xlabel(r"$b_{1}$", size=12)
ax2.set_ylabel("跨国公司总利润", fontproperties=props_font_label)
ax2.tick_params(labelsize=11)
# ax2.grid(linestyle='-.')
# ax2.fill_between(x, 3740, profit, facecolor='#81b8df', alpha=0.618)

# set transparency for plt, axes
fig.patch.set_alpha(0)
ax1.patch.set_alpha(0)
ax2.patch.set_alpha(0)

# show plot
fig.tight_layout()
plt.show()
