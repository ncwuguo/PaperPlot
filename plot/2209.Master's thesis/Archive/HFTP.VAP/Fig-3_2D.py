import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.pyplot import MultipleLocator
from matplotlib import ticker
import scienceplots  # noqa: F401

# initial settings - set plot style
plt.style.use(["science", "no-latex"])

# define axis ranges for x and y
x = np.arange(0, 0.602, 0.02)
y = np.arange(10, 15.2, 0.2)
# create meshgrid from x and y
X, Y = np.meshgrid(x, y)
# define axis Z
Z = -0.224467 * (3 + 0.6 * (-199 + Y) - 3 * Y * X)

# generate canvas
fig, ax1 = plt.subplots(figsize=(5.5, 5), dpi=250)

# set props
font_size = 24
props_font_label = fm.FontProperties(size=font_size)

# plot
ax1.set_xlabel(r"$r$", fontproperties=props_font_label)
ax1.set_ylabel(r"$c$", fontproperties=props_font_label)
ax1.tick_params(labelsize=20)
ax1.xaxis.set_major_locator(MultipleLocator(0.2))
ax1.xaxis.set_minor_locator(MultipleLocator(0.1))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(MultipleLocator(0.5))
ax1.tick_params(which="major", length=4)
ax1.tick_params(which="minor", length=2)
ax1.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax1.set_xlim(-0.025, 0.625)
ax1.set_ylim(9.75, 15.25)
# ax1.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"])

# levels = np.arange(24.4, 28.0, 0.2)
cs = ax1.contourf(X, Y, Z, cmap=plt.get_cmap("gray_r"))
# add colorbar
cbar = fig.colorbar(cs)
cbar.ax.tick_params(labelsize=font_size)


# show plot
fig.tight_layout()
plt.show()
