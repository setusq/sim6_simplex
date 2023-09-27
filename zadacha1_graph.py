import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-5, 40, 100)
x2 = np.linspace(-5, 40, 100)

plt.figure(figsize=(5, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-5,15)
plt.ylim(-5,15)

plt.plot(x1, (14 + 7*x1) / 2, label='-7*x1 + 2*x2 >= 14', color='salmon', linestyle='dashed')
plt.plot(x1, (13 - x1)/11, label='x1 +11*x2 <= 13', color='pink', linestyle='dashed')
plt.plot(x1, 3 - x1, label='x1 +x2 <= 3', color='#DB7093', linestyle='dashed')
plt.plot(x1, (20 - 4 * x1) / 5, label='4*x1 + 5*x2 >= 20', color='#DB7040', linestyle='dashed')
plt.axvline(x=0, color='gray', linestyle='dashed')
plt.axhline(y=0, color='gray', linestyle='dashed')

plt.arrow(0,0,  1.4,  2, head_width=0.4, head_length=0.8, fc='black', ec='black', label='вектор z')
x1_green = np.linspace(-2, 2, 100)
plt.plot(x1_green, (-15 * x1_green)/21, linestyle='-.', color='green', label='перпендикуляр')

plt.title('Задание 1')
plt.grid(True)
plt.legend()
plt.show()
