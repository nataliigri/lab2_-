import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані
mas_y1_line = [-0.2000, 0.6000, 1.4000, 2.2000, 3.0000, 3.8000, 4.6000, 5.4000, 6.2000, 7.0000]
k2 = 3
k1 = k2 * 0.01

# Визначимо масив аргументів mas_x та масив значень функції mas_y
mas_x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Аргументи
mas_y = np.array(mas_y1_line) + k1  # Значення функції з урахуванням k1

# Знаходимо оптимальні коефіцієнти A і B за методом найменших квадратів
A, B = np.polyfit(mas_x, mas_y, 1)

# Виведемо значення A і B
print("A =", A)
print("B =", B)

# Генеруємо точки для побудови прямої лінії
x_line = np.linspace(0, 9, 100)  # Від 0 до 9 з 100 точками
y_line = A * x_line + B

# Побудова графіків
plt.figure(figsize=(8, 6))
plt.scatter(mas_x, mas_y, label="Задані точки")
plt.plot(x_line, y_line, label=f"Апроксимація: y = {A:.2f}x + {B:.2f}", color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
