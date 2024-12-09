
"""
Розрахунок значення визначеного інтеграла методом парабол / правило Сімпсона - parabola method - Simpson’s rule:
Time Complexity: оцінити / знайти  самостійно
Auxiliary Space: оцінити / знайти  самостійно

"""

import numpy as np
from busy_time_meter import busy_time_meter


# Інтегрування за правилом Сімпсона
@busy_time_meter
def simpson_rule(f, a, b, n):

    # розрахунок кроку
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # розрахунок інтеграла
    # https://numpy.org/doc/stable/reference/generated/numpy.sum.html
    integration = h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])

    # Похибка інтегрування - без похідної
    epsilon = ((b - a) ** 5) / (180 * (n ** 4))

    return integration, epsilon


def simpson_main(fun, low, high, n):
    print("\n Інтегрування за правилом Сімпсона: ")
    # ---------------------- Аналітика складності алгоритму  ---------------------------
    print(simpson_rule(fun, low, high, n))






