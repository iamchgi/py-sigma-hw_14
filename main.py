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
    low = -4
    high = 4
    n = 1_000_000

    a = 6
    b = 3
    c = -5

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

    chord_main(function, low, -0.5, n)
    chord_main(function, 0, high, n)
    bisection_main(function, low, 0, n)
    bisection_main(function, 0, high, n)

    integrated_root_search(function, low, high)
    integrated_root_search_v(function, low, high)

"""
РЕЗУЛЬТАТ

 Інтегрування методом трапецій: 
Функція - trapezoidal          час виконання: 1.125002 секунд
(2417.6000000164213, 5.3333333333333335e-12)

 Інтегрування за правилом Сімпсона: 
Функція - simpson_rule         час виконання: 0.114989 секунд
(np.float64(2417.599999999999), 1.8204444444444444e-22)

 Інтегрування методом прямокутників: 
Функція - rectangle_int_l      час виконання: 0.974023 секунд
(2417.599904016421, 3.2e-05)
Функція - rectangle_int_c      час виконання: 1.317977 секунд
(2417.599999895474, 2.1333333333333334e-11)

 Інтегрування із бібліотекою scipy: 
(2417.6, 2.7018536268747952e-11)
Функція - integrated_iteration_quad час виконання: 0.000000 секунд

 Інтегрування із бібліотекою numpy:
2417.6000000163845
Функція - integrated_iteration_np час виконання: 0.020992 секунд

 Метод Симпсона: 
2417.6
Функція - integrated_iteration_simpson час виконання: 0.063028 секунд

 Пошук коренів нелінійного рівняння метод хорд: 
Функція - secant               час виконання: 0.000995 секунд
-1.0828177229851395   1e-06

 Пошук коренів нелінійного рівняння метод хорд: 
Функція - secant               час виконання: 0.000000 секунд
0.8091859671517443   1e-06

 Пошук коренів нелінійного рівняння, ділення навпіл (дихотомії):
Функція - bisection            час виконання: 0.000000 секунд
-1.0828180313110352   1e-06

 Пошук коренів нелінійного рівняння, ділення навпіл (дихотомії):
Функція - bisection            час виконання: 0.000000 секунд
0.8091859817504883   1e-06

 Пошук коренів із бібліотекою scipy: Знайдіть корені функції:
[-1.08281761  0.80918634]
Функція - integrated_root_search час виконання: 0.002001 секунд

 Пошук коренів із бібліотекою scipy: Знайдіть корінь вектор-функції: 
[-1.08281761  0.80918634]
Функція - integrated_root_search_v час виконання: 0.001007 секунд

"""
