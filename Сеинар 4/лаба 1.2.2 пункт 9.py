
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (10, 8))

# Первый набор данных
x1 = [0.006742564, 0.007484972, 0.008638481, 0.009254264]
y1 = [0.2908, 0.3352, 0.3878, 0.4322]
plt.scatter(x1, y1, label='R = 1.77 см', color='blue')
plt.errorbar(x1, y1, yerr=0.01, xerr=0.0001, color='k', linestyle='None')

# Второй набор данных
x2 = [0.005545129, 0.005833739, 0.006477246, 0.007096175]  # новые данные
y2 = [0.2759, 0.2816, 0.3321, 0.3612]  # новые данные
plt.scatter(x2, y2, label='R = 0.95 см', color='red')
plt.errorbar(x2, y2, yerr=0.01, xerr=0.0001, color='k', linestyle='None')

# Аппроксимация для первого набора
mnk1 = np.polyfit(x1, y1, 1)
z1 = np.poly1d(mnk1)

# Аппроксимация для второго набора
mnk2 = np.polyfit(x2, y2, 1)
z2 = np.poly1d(mnk2)

plt.title('Зависимость начального углового ускорения от момента силы натяжения нити')
plt.xlabel('M_нити, Н * м')
plt.ylabel('b_0, рад/с^2')
plt.xlim(0.00, 0.012)
plt.ylim(-0.1, 0.5)



x_line = np.linspace(0.00, 0.012, 100)
plt.plot(x_line, z1(x_line), 'b-', label=f'Аппроксимация 1: y = {mnk1[0]:.3f}x + {mnk1[1]:.3f}')
plt.plot(x_line, z2(x_line), 'r-', label=f'Аппроксимация 2: y = {mnk2[0]:.3f}x + {mnk2[1]:.3f}')

# Вывод уравнений
# equation_text1 = f'Набор 1: y = {mnk1[0]:.6f}·x + {mnk1[1]:.6f}'
# equation_text2 = f'Набор 2: y = {mnk2[0]:.6f}·x + {mnk2[1]:.6f}'
# plt.figtext(0.5, 0.04, equation_text1, ha='center', fontsize=10)
# plt.figtext(0.5, 0.02, equation_text2, ha='center', fontsize=10)

plt.legend()
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.show()