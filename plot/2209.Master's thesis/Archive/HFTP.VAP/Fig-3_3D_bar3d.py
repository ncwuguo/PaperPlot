import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib import ticker
import scienceplots  # noqa: F401

# initial settings - set plot style
plt.style.use(["science", "grid", "no-latex"])
plt.rcParams["svg.fonttype"] = "none"

# define axis ranges and meshgrid
_x = np.arange(10, 15.2, 0.2)
_y = np.arange(0, 0.62, 0.02)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# define axis z
bottom = 23.5
top = -0.224467 * (3 + 0.6 * (-199 + x) - 3 * y * x) - bottom

# generate canvas
fig = plt.figure(figsize=(5.6, 5), dpi=300)
ax = fig.add_subplot(111, projection="3d")

# define colors
norm = plt.Normalize(top.min(), top.max())
colors = plt.cm.gray_r(norm(top))
# colors = plt.cm.rainbow(norm(top))

# The ratio of width and depth should be the same as the ratio of x and y
width = 0.08
depth = 0.008

ax.bar3d(x, y, bottom, width, depth, top, colors, shade=True)
# ax1.invert_yaxis()
ax.invert_xaxis()
ax.set_xlabel("$c$", size=12, labelpad=-8)
ax.set_ylabel("$r$", size=12, labelpad=-8)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.zaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax.tick_params(labelsize=12)

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)
plt.setp(ax.get_zticklabels(), visible=False)

for x, text in zip([10.3, 11.3, 12.3, 13.3, 14.3, 15.3], ["10", "11", "12", "13", "14", "15"]):
    ax.text(x=x, y=-0.11, z=22.9, s=text)

for y, text in zip([-0.02, 0.15, 0.35, 0.55], ["0%", "20%", "40%", "60%"]):
    ax.text(x=9.4, y=y, z=22.9, s=text)

for z, text in zip([23.8, 25.8, 27.8, 29.8], ["24", "26", "28", "30"]):
    ax.text(x=9.4, y=0.65, z=z, s=text)


# show plot
# fig.tight_layout()
ax.view_init(elev=28, azim=-45)
plt.show()
