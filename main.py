"""
Виконав: Григорій Чернолуцький
Homework_14

Package                      Version
---------------------------- -----------
pip                          24.3.1
numpy                        2.1.3
matplotlib                   3.9.2
scipy                        1.14.1
"""

import numpy as np
from matplotlib import pyplot as plt

from mathematical_algorithms import *


def graph_equation(equation, arr) -> None:
    """
    Метод візуалізації нелінійного рівняння
    :param equation: нелінійне рівняння
    :param arr: одновимірний масив з рівномірно розподіленими значеннями на вказаному інтервалі.
    :return: nothing
    """
    fig, ax = plt.subplots()
    plt.grid(True)
    ax.plot(arr, equation)
    plt.show()


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    # ------------------------- параметри інтегрування ----------------------------
    low = -5
    high = 6
    n = 1_000_000

    a = 1
    b = 2
    c = -4

    # Задаємо лямбда функцію
    function = lambda x: a * x ** 4 + b * x + c
    # створення одновимірного масиву з рівномірно розподіленими значеннями на вказаному інтервалі.
    x = np.linspace(low, high, num=n)
    # Задаємо нелінійне рівняння для підінтегральної функції
    y = a * x ** 4 + b * x + c
    graph_equation(y, x)

    trapezoidal_main(function, low, high, n)
    simpson_main(function, low, high, n)
    rectangle_main(function, low, high, n)
    integrated_iteration_quad(function, low, high)
    integrated_iteration_np(y, x)
    integrated_iteration_simpson(y, x)

    # Задаємо нелінійне рівняння для знаходження коренів
    y = a * x ** 2 + b * x + c
    graph_equation(y, x)

    chord_main(function, low, 0, n)
    chord_main(function, 0, high, n)
    bisection_main(function, low, 0, n)
    bisection_main(function, 0, high, n)

    integrated_root_search(function, low, high)
    integrated_root_search_v(function, low, high)

"""
РЕЗУЛЬТАТ

 Інтегрування методом трапецій: 
Функція - trapezoidal          час виконання: 1.420988 секунд
(2147.2000000137336, 1.0083333333333334e-11)

 Інтегрування за правилом Сімпсона: 
Функція - simpson_rule         час виконання: 0.132998 секунд
(np.float64(2147.1999999999994), 8.947277777777779e-22)

 Інтегрування методом прямокутників: 
Функція - rectangle_int_l      час виконання: 2.052001 секунд
(2147.196188513734, 6.05e-05)
Функція - rectangle_int_c      час виконання: 2.238999 секунд
(2147.185656082548, 5.5458333333333336e-11)

 Інтегрування із бібліотекою scipy: 
(2147.1999999999994, 2.4057228863397244e-11)
Функція - integrated_iteration_quad час виконання: 0.028473 секунд

 Інтегрування із бібліотекою numpy:
2147.2000000137537
Функція - integrated_iteration_np час виконання: 0.028985 секунд

 Метод Симпсона: 
2147.2000000000007
Функція - integrated_iteration_simpson час виконання: 0.082010 секунд

 Пошук коренів нелінійного рівняння метод хорд: 
Функція - secant               час виконання: 0.000000 секунд
1.1439012405504156   1e-06

 Пошук коренів нелінійного рівняння метод хорд: 
Функція - secant               час виконання: 0.000000 секунд
1.143901122528208   1e-06

 Пошук коренів нелінійного рівняння, ділення навпіл (дихотомії):
Функція - bisection            час виконання: 0.000000 секунд
-1.6429346799850464   1e-06

 Пошук коренів нелінійного рівняння, ділення навпіл (дихотомії):
Функція - bisection            час виконання: 0.000000 секунд
1.1439006328582764   1e-06

 Пошук коренів із бібліотекою scipy: Знайдіть корені функції:
[-1.64293488  1.14390111]
Функція - integrated_root_search час виконання: 0.044000 секунд

 Пошук коренів із бібліотекою scipy: Знайдіть корінь вектор-функції: 
[-1.64293488  1.14390111]
Функція - integrated_root_search_v час виконання: 0.005001 секунд

"""
