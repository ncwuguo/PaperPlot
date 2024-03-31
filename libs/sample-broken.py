import numpy as np
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes


plt.style.use(['science', 'grid', 'no-latex'])
# fake data

x = np.linspace(0.2, 1, 9)
print(x)
price = (122.96 + 425.6 * x) / (1.52 + 4.76 * x)
profit = (
    178857
    + 319992 * x
    + 212064 * x**2
    + 31185 * (2 + x)
    + x * (-207 + 70688 * x)
    + x * (289014 + 141376 * x)
) / (2 * (5 + 8 * x) ** 2)


# create figure with broken axis
fig = plt.figure(figsize=(6, 6))
bax = brokenaxes(ylims=((0, 0), (84, 87.5)), hspace=.08)

# plot data on broken axis
# bax.plot(x, y1)
bax.plot(x, price, linestyle='--', marker='^', color='black', markerfacecolor='white')
# bax.plot(x, y2, label='cos(x)*1000')

# set labels and title
bax.set_xlabel('X Axis')
bax.set_ylabel('Y Axis')
bax.set_title('Broken Axis Example')
bax.grid(linestyle='-.')

# show plot
plt.show()
