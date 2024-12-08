
"""
Розрахунок значення визначеного інтеграла методом трапецій - Trapezoidal Method:
Time Complexity: O(n), n - кількість інтервалів
Auxiliary Space: O(1)

"""

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
    print("\n Інтегрування методом трапецій: ")
    # ---------------------- Аналітика складності алгоритма  ---------------------------
    print(trapezoidal(function, low, high, n))






