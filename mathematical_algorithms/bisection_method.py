
"""
Пошук коренів нелінійного рівняння методом метод ділення навпіл (дихотомії) - bisection method:
Time Complexity: оцінити / знайти самостійно
Auxiliary Space: оцінити / знайти самостійно

"""

from scipy import optimize
from scipy.optimize import fsolve

from busy_time_meter import busy_time_meter

# Пошук коренів нелінійного рівняння
#   ділення навпіл (дихотомії)
@busy_time_meter
def bisection(f, a, b, epsilon):

    # Перевірка наявності кореня на інтервалі
    if (f(a) * f(b) >= 0):
        print("Змініть межі пошуку коренів\n")
        return

    root = a

    # Контроль досяжності точності рішення
    while ((b - a) >= epsilon):

        # Ділення інтервалу навпіл
        root = (a + b) / 2

        # Перевірте, чи середня точка є коренем
        if (f(root) == 0.0):
            break

        # Вибір інтервалу пошуку коренів
        if (f(root) * f(a) < 0):
            b = root
        else:
            a = root

    return root


def bisection_main(fun, low, high, n):
    epsilon = 1/n
    print("\n Пошук коренів нелінійного рівняння, ділення навпіл (дихотомії):")
    # ---------------------- Аналітика складності алгоритму  ---------------------------
    print(bisection(fun, low, high, epsilon), ' ', epsilon)







