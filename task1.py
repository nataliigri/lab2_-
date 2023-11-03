import numpy as np
from scipy.integrate import quad
from scipy.special import legendre
import matplotlib.pyplot as plt

# Задана функція f(x)
def f(x):
    return 0.5 * np.sqrt(x) + 2 * np.sin(x)

# Кількість базових функцій
n = 4

# Побудова апроксимації
def approximation(x):
    # Заміна змінної t
    t = (2 * x - 7) / 5
    
    # Коефіцієнти c_i
    c = []
    for i in range(n+1):
        def integrand(t):
            return f((5*t + 7)/2) * legendre(i)(t)
        result, _ = quad(integrand, -1, 1)
        c.append((2*i + 1) / 2 * result)
    
    # Побудова апроксимації S(x)
    S_x = sum(c[i] * legendre(i)((2 * x - 7) / 5) for i in range(n+1))
    
    return S_x

# Генерування точок для побудови графіка
x_values = np.linspace(1, 6, 100)
y_values_exact = f(x_values)
y_values_approx = approximation(x_values)

# Дослідження точності у вузлах
nodes = np.array([1, 2, 3, 4, 5, 6])
y_values_nodes_exact = f(nodes)
y_values_nodes_approx = approximation(nodes)

# Побудова графіка
plt.plot(x_values, y_values_exact, label='f(x)')
plt.plot(x_values, y_values_approx, label='S(x)', linestyle='dashed')
plt.scatter(nodes, y_values_nodes_exact, color='red', label='f(вузли)')
plt.scatter(nodes, y_values_nodes_approx, color='blue', label='S(вузли)')
plt.legend()


# Друк числових результатів
for i in range(len(nodes)):
    print(f"Вузол {nodes[i]}:")
    print(f"f({nodes[i]}) = {y_values_nodes_exact[i]}")
    print(f"S({nodes[i]}) = {y_values_nodes_approx[i]}")
    print(f"Похибка у вузлі: {abs(y_values_nodes_exact[i] - y_values_nodes_approx[i])}\n")

plt.show()
