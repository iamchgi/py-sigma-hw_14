
"""
Пошук коренів нелінійного рівняння методом метод ділення навпіл (дихотомії)  - bisection method:
Time Complexity: оцінити / знайти  самостійно
Auxiliary Space: оцінити / знайти  самостійно

"""

from busy_time_meter import busy_time_meter


@busy_time_meter
def secant(f, a, b, epsilon):
    root = None
    x1 = a
    x2 = b

    # Аналіз області пошуку рішення (ліворуч / праворуч від нуля)
    if a < 0:
        x1 = b
        x2 = a

    n = 0

    if (f(x1) * f(x2) < 0):
        while True:

            # обчислити проміжне значення
            x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))

            # перевірте, чи x0 є коренем рівняння чи ні
            c = f(x1) * f(x0)

            # оновити значення інтервалу
            x1 = x2
            x2 = x0

            # оновити номер ітерації
            n += 1

            # якщо x0 є коренем рівняння припинити розрахунки
            if (c == 0):
                break
            xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))

            # контроль точності розрахунку
            if (abs(xm - x0) < epsilon):
                break

        # корень отримано
        root = x0

    else:
        print("В заданому інтервалі корень відсутній")

    return root


def chord_main(fun, low, high, n):
    print("\n Пошук коренів нелінійного рівняння hord method: ")
    epsilon = 1/n

    # ---------------------- Аналітика складності алгоритму  ---------------------------
    print(secant(fun, low, high, epsilon), ' ', epsilon)


