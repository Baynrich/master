import matplotlib.pyplot as plt
import numpy as np

x_cords = np.linspace(-4, 7, num=1000)
y_cords = [np.sin(x) + 0.3*x for x in x_cords]
plt.plot(x_cords, y_cords)


plt.plot(3, 1.15, 'go')

x_deri_cords = np.linspace(2.6, 3.6, num=4)
y_deri_cords = [-0.66*x + 3.25 for x in x_deri_cords]
plt.plot(x_deri_cords, y_deri_cords)

#plt.xticks([], [])
#plt.yticks([], [])
plt.savefig('./code/img.png', format='png', dpi=400)