
"""
Розрахунок значення визначеного інтеграла методом трапецій - Trapezoidal Method:
Time Complexity: O(n), n - кількість інтервалів
Auxiliary Space: O(1)

"""

import numpy as np
from scipy import integrate

from busy_time_meter import busy_time_meter

@busy_time_meter
# Інтегрування методом трапецій
def trapezoidal(f, x0, xn, n):

    # розрахунок кроку
    h = (xn - x0) / n

    # Знаходження суми
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h
        integration = integration + 2 * f(k)

    # Знаходження кінцевого значення інтегрування
    integration = integration * h / 2

    # Похибка інтегрування - без похідної
    epsilon = ((xn - x0)**2) / (12*(n**2))

    return integration, epsilon


def trapezoidal_main(function, low, high, n):

    # ---------------------- Аналітика складності алгоритма  ---------------------------
    print(trapezoidal(function, low, high, n))

    # Інтегрування із бібліотекою scipy
    print(integrate.quad(function, low, high))

    # Інтегрування із бібліотекою numpy
    x = np.linspace(low, high, num=n)
    # y = a / (1 + x ** 2)
    # # y =  a * x ** 2 + b * x + c
    # print(np.trapz(y, x))





