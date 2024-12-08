
"""
Розрахунок значення визначеного інтеграла методом прямокутників - method of rectangles:
Time Complexity: O(n), n - кількість інтервалів
Auxiliary Space: O(1)

"""

from scipy import integrate

from busy_time_meter import busy_time_meter


# Інтегрування методом прямокутників (лівий прямокутник)
@busy_time_meter
def rectint_l(f, a, b, n):

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
def rectint_c(f, a, b, n):

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


def rectangle_main(fun, low, high, n):

    # параметри інтегрування
    low = 0
    high = 10
    n = 1000000


    a = 1
    b = 2
    c = 3

    fun = lambda x: a * x ** 2 + b * x + c


    # ---------------------- Аналітика складності алгоритму  ---------------------------
    print(rectint_l(fun, low, high, n))
    print(rectint_c(fun, low, high, n))

    # Інтегрування із бібліотекою scipy
    print(integrate.quad(fun, low, high))





