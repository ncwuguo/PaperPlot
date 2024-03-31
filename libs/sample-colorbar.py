import numpy as np
import matplotlib.pyplot as plt

#生成绘图数据
N = 100
x, y = np.mgrid[:100, :100]
Z = np.cos(x) + np.sin(y)

# mask out the negative and positive values, respectively
Zpos = np.ma.masked_less(Z, 0)   #小于零的部分
Zneg = np.ma.masked_greater(Z, 0)  #大于零的部分

fig, (ax1, ax2, ax3) = plt.subplots(figsize=(13, 3), ncols=3)

pos = ax1.imshow(Zpos, cmap='Reds', interpolation='none')
fig.colorbar(pos, ax=ax1)  #这里使用colorbar来制定需要画颜色棒的图的轴，以及对应的cmap，与pos对应

neg = ax2.imshow(Zneg, cmap='Blues_r', interpolation='none')
fig.colorbar(neg, ax=ax2)

pos_neg_clipped = ax3.imshow(Z, cmap='jet', vmin=-2, vmax=2,interpolation='none')  #-2,2的区间
fig.colorbar(pos_neg_clipped, ax=ax3)
plt.show()

#ref:
#    https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.colorbar
#    https://matplotlib.org/gallery/color/colorbar_basics.html#sphx-glr-gallery-color-colorbar-basics-py