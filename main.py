"""
Виконав: Григорій Чернолуцький
Homework_14

Package                      Version
---------------------------- -----------
pip                          24.3.1
numpy                        2.1.3
matplotlib                   3.9.2

"""

import numpy as np
from matplotlib import pyplot as plt

from mathematical_algorithms import *


def graph_fun(fun, lo, hi, n) -> None:
    """
    Метод візуалізації функції
    :param fun: лямбда функція
    :param lo:
    :param hi:
    :param n:
    :return:
    """
    x = np.linspace(lo, hi, n)
    y = fun(x)
    fig, ax = plt.subplots()
    plt.grid(True)
    ax.plot(x, y)
    plt.show()


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    # ------------------------- параметри інтегрування ----------------------------
    low = -5
    high = 6
    n = 100_000

    a = 1
    b = 2
    c = -4

    # Задаємо лямбда функцію
    function = lambda x: a * x ** 2 + b * x + c

    graph_fun(function, low, high, n)

    trapezoidal_main(function, low, high, n)
    simpson_main(function, low, high, n)
    rectangle_main(function, low, high, n)

    x = np.linspace(low, high, num=n)
    y = a * x ** 2 + b * x + c
    integrated_iteration(function, low, high, y, x)

    chord_main(function, low, high, n)
    bisection_main(function, low, high, n)

    integrated_root_search(function,low,high)

"""
РЕЗУЛЬТАТ



"""
