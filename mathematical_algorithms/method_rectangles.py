"""
Розрахунок значення визначеного інтеграла методом прямокутників - method of rectangles:
Time Complexity: O(n), n - кількість інтервалів
Auxiliary Space: O(1)

"""

from busy_time_meter import busy_time_meter


# Інтегрування методом прямокутників (лівий прямокутник)
@busy_time_meter
def rectangle_int_l(f, a, b, n):
    # лівий прямокутник

    total = 0.0
    # розрахунок кроку
    dx = (b - a) / float(n)

    for k in range(0, n):
        total = total + f((a + (k * dx)))

    # Знаходження кінцевого значення інтегрування
    integration = dx * total

    # Похибка інтегрування - без похідної
    epsilon = ((b - a) ** 2) / (2 * n)

    return integration, epsilon


# Інтегрування методом прямокутників
@busy_time_meter
def rectangle_int_c(f, a, b, n):
    # середній прямокутник

    integration = 0

    # розрахунок кроку
    i = (b - a) / float(n)
    trailing_x = a
    leading_x = a + i

    while (a <= leading_x <= b) or (a >= leading_x >= b):
        area = f((trailing_x + leading_x) / 2) * i
        integration += area
        leading_x += i
        trailing_x += i

    # Похибка інтегрування - без похідної
    epsilon = ((b - a) ** 3) / (24 * (n ** 2))

    return integration, epsilon


def rectangle_main(fun, low, high, n) -> None:
    """
    Виклик Інтегрування методом прямокутників
    :param fun: лямбда функція
    :param low: початкове значення інтервалу
    :param high: кінцеве значення інтервалу
    :param n: кількість значень на інтервалі
    :return: None
    """
    print("\n Інтегрування методом прямокутників: ")
    # ---------------------- Аналітика складності алгоритму ---------------------------
    print(rectangle_int_l(fun, low, high, n))
    print(rectangle_int_c(fun, low, high, n))
