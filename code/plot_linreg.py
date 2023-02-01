import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2
import matplotlib

# Enter x and y coordinates of points and colors
xs = [-2, -1, 1, 2]
ys = [-0.5, 1, 1, 2.5]
colors = ['m', 'g', 'r', 'b']

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -5, 5, -5, 5
ticks_frequency = 1

# Plot points
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(xs, ys, c=colors)

"""
# Draw lines connecting points to axes
ax.plot([-2, -2], [-0.5, 0], c="m", ls='--', lw=1.5, alpha=0.5)
ax.plot([-2, -1.5], [0, 0], c="m", ls='--', lw=1.5, alpha=0.5)
ax.plot([-1.5, -1.5], [-0.5, 0], c="m", ls='--', lw=1.5, alpha=0.5)
ax.plot([-2, -1.5], [-0.5, -0.5], c="m", ls='--', lw=1.5, alpha=0.5)
rect1 = matplotlib.patches.Rectangle((-2,-0.5), 0.5, 0.5, color='m', alpha=0.15)
ax.add_patch(rect1)

ax.plot([-1, -1], [1, 0.5], c="g", ls='--', lw=1.5, alpha=0.5)
ax.plot([-1, -1.5], [1, 1], c="g", ls='--', lw=1.5, alpha=0.5)
ax.plot([-1.5, -1.5], [0.5, 1], c="g", ls='--', lw=1.5, alpha=0.5)
ax.plot([-1, -1.5], [0.5, 0.5], c="g", ls='--', lw=1.5, alpha=0.5)
rect2 = matplotlib.patches.Rectangle((-1.5,0.5), 0.5, 0.5, color='g', alpha=0.15)
ax.add_patch(rect2)

ax.plot([1, 1], [1, 1.5], c="r", ls='--', lw=1.5, alpha=0.5)
ax.plot([1, 1.5], [1.5, 1.5], c="r", ls='--', lw=1.5, alpha=0.5)
ax.plot([1.5, 1.5], [1, 1.5], c="r", ls='--', lw=1.5, alpha=0.5)
ax.plot([1, 1.5], [1, 1], c="r", ls='--', lw=1.5, alpha=0.5)
rect3 = matplotlib.patches.Rectangle((1, 1), 0.5, 0.5, color='r', alpha=0.15)
ax.add_patch(rect3)

ax.plot([2, 2], [2.5, 2], c="b", ls='--', lw=1.5, alpha=0.5)
ax.plot([2, 1.5], [2.5, 2.5], c="b", ls='--', lw=1.5, alpha=0.5)
ax.plot([1.5, 1.5], [2.5, 2], c="b", ls='--', lw=1.5, alpha=0.5)
ax.plot([2, 1.5], [2, 2], c="b", ls='--', lw=1.5, alpha=0.5)
rect4 = matplotlib.patches.Rectangle((1.5,2), 0.5, 0.5, color='b', alpha=0.15)
ax.add_patch(rect4)

ax.plot([-6, 6], [-2, 4])
"""

# Set identical scales for both axes
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
ax.set_xlabel('x', size=14, labelpad=-1, x=0.98)
ax.set_ylabel('y', size=14, labelpad=-1, y=0.98, rotation=0)

# Create custom major ticks to determine position of tick labels
x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])

# Create minor ticks placed at each integer to enable drawing of minor grid
# lines: note that this has no effect in this example with ticks_frequency=1
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

# Draw major and minor grid lines
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

plt.savefig('../figures/linreg_input_illustrated.png', format="png", bbox_inches='tight')
