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

from mathematical_algorithms import trapezoidal_main, bisection_main, simpson_main, rectangle_main, chord_main


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
    n = 10_000

    a = 1
    b = 2
    c = -2

    # Задаємо лямбда функцію
    function = lambda x: a * x ** 2 + b * x + c

    graph_fun(function, low, high, n)

    print(" Інтегрування методом трапецій ")
    trapezoidal_main(function, low, high, n)
    print("   ділення навпіл (дихотомії) ")
    bisection_main(function, low, high, n)
    print(" Інтегрування за правилом Сімпсона ")
    simpson_main(function, low, high, n)
    print(" Інтегрування методом прямокутників ")
    rectangle_main(function, low, high, n)
    print(" hord ")
    chord_main(function, low, high, n)

"""
РЕЗУЛЬТАТ



"""
