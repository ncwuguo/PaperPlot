import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.legend import DraggableLegend
import numpy as np

x1 = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x1)

x2 = np.arange(0, 2*np.pi, 0.1)
y2 = np.cos(x2)

fig, ax = plt.subplots()
ax.plot(x1, y1, label='line1')
ax.plot(x2, y2, label='line2')

legend = DraggableLegend(ax, ax.legend())
legend.set_loc(1)
ax.add_artist(legend)

def on_move(event):
    legend._loc_in_canvas = (event.x, event.y)
    ax.figure.canvas.draw_idle()

legend.connect('motion_notify_event', on_move)

plt.show()
