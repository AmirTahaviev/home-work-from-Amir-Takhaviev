
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (10, 8))

# Первый набор данных
x1 = [0.0256, 0.01, 0.0025, 0.04]
y1 = [0.01114625, 0.006420328, 0.003870464, 0.014272072]
plt.scatter(x1, y1,  color='blue')
plt.errorbar(x1, y1, yerr=0.00001, xerr=0.0001, color='k', linestyle='None')


# Аппроксимация для первого набора
mnk1 = np.polyfit(x1, y1, 1)
z1 = np.poly1d(mnk1)



plt.title('Зависимость момента инерции конструкции от квадрата расстояния R')
plt.xlabel('R^2, м^2')
plt.ylabel('I, Н * м^2')
plt.xlim(0.0, 0.045)  # Максимальное значение x = 0.04
plt.ylim(0.0, 0.016)



x_line = np.linspace(0.0, 0.045, 100)
plt.plot(x_line, z1(x_line), 'b-', label=f' y = {mnk1[0]:.3f}x + {mnk1[1]:.3f}')

# Вывод уравнений
# equation_text1 = f'Набор 1: y = {mnk1[0]:.6f}·x + {mnk1[1]:.6f}'
# equation_text2 = f'Набор 2: y = {mnk2[0]:.6f}·x + {mnk2[1]:.6f}'
# plt.figtext(0.5, 0.04, equation_text1, ha='center', fontsize=10)
# plt.figtext(0.5, 0.02, equation_text2, ha='center', fontsize=10)

plt.legend()
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.show()