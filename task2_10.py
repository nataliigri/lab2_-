import numpy as np
import matplotlib.pyplot as plt

# Ініціалізація вхідних даних
mas_x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
mas_y4_4_parabola = np.array([-1.9120, 1.0640, 2.6960, 3.7520, 5.0000, 7.2080, 11.1440, 17.5760, 27.2720, 41.0000])

k2 = 3
k1 = k2 * 0.01

# Визначення коефіцієнтів A, B, C, D, E за допомогою методу найменших квадратів
X4 = np.column_stack((mas_x**4, mas_x**3, mas_x**2, mas_x, np.ones_like(mas_x)))
y4 = mas_y4_4_parabola + k1
A4, B4, C4, D4, E4 = np.linalg.lstsq(X4, y4, rcond=None)[0]

# Функція полінома п’ятого степеня
def poly5_func(x):
    return A4 * x**4 + B4 * x**3 + C4 * x**2 + D4 * x + E4

# Відображення точок та функції на графіку
plt.scatter(mas_x, mas_y4_4_parabola, label='Задані точки')
x_range = np.linspace(min(mas_x), max(mas_x), 100)

plt.plot(x_range, poly5_func(x_range), color='red', label=f'y = {A4:.4f}x^4 + {B4:.4f}x^3 + {C4:.4f}x^2 + {D4:.4f}x + {E4:.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

print(f"A = {A4}, B = {B4}, C = {C4}, D = {D4}, E = {E4}")
plt.show()

