import numpy as np
from scipy.integrate import simpson, quad
from scipy.optimize import fsolve, root

from busy_time_meter import busy_time_meter


@busy_time_meter
def integrated_root_search_v(function, low, high) -> None:
    """
    Пошук коренів із бібліотекою scipy вектор-функції
    :param function: лямбда функція
    :param low: початкове значення інтервалу
    :param high: кінцеве значення інтервалу
    :return: None ('scipy.optimize._optimize.OptimizeResult')
    """
    print("\n Пошук коренів із бібліотекою scipy: Знайдіть корінь вектор-функції: ")
    sol = root(function, [low, high])
    print(sol.x)


@busy_time_meter
def integrated_root_search(function, low, high) -> None:
    """
    Пошук коренів із бібліотекою scipy вектор-функції
    :param function: лямбда функція
    :param low: початкове значення інтервалу
    :param high: кінцеве значення інтервалу
    :return: None (numpy.ndarray)
    """
    print("\n Пошук коренів із бібліотекою scipy: Знайдіть корені функції:")
    sol = fsolve(function, [low, high])
    print(sol)


@busy_time_meter
def integrated_iteration_quad(function, low, high) -> None:
    """
    Compute a definite integral.
    Integrate func from `a` to `b` (possibly infinite interval) using a
    technique from the Fortran library QUADPACK.
    :param function: лямбда функція
    :param low: початкове значення інтервалу
    :param high: кінцеве значення інтервалу
    :return: none
    """
    print("\n Інтегрування із бібліотекою scipy: ")
    print(quad(function, low, high))


@busy_time_meter
def integrated_iteration_np(y, x) -> None:
    """
    Інтегрування із бібліотекою numpy
    :param y: Підінтегральне рівняння
    :param x: Одновимірний масив з рівномірно розподіленими значеннями на вказаному інтервалі.
    :return: ніхт
    """
    print("\n Інтегрування із бібліотекою numpy:")
    print(np.trapezoid(y, x))


@busy_time_meter
def integrated_iteration_simpson(y, x) -> None:
    """
    Інтегрування Метод Симпсона
    Integrate y(x) using samples along the given axis and the composite
    Simpson's rule. If x is None, spacing of dx is assumed.
    :param y: Підінтегральне рівняння
    :param x: Одновимірний масив з рівномірно розподіленими значеннями на вказаному інтервалі.
    :return: nothing
    """
    print("\n Метод Симпсона: ")  # initial=0
    print(simpson(y, x=x))
