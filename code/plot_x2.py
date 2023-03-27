import matplotlib.pyplot as plt
import numpy as np

x_cords = np.linspace(-2.5, 3.5, num=1000)
y_cords = [x*x for x in x_cords]
plt.plot(x_cords, y_cords)


plt.plot(2, 4.4, 'go')
x_deri_cords = np.linspace(1.7, 2.2, num=4)
y_deri_cords = [4*x - 3.235 for x in x_deri_cords]
plt.plot(x_deri_cords, y_deri_cords)

plt.xticks([], [])
plt.yticks([], [])
plt.savefig('./code/img.png', format='png', dpi=400)