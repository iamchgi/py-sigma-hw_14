import numpy as np
from scipy.integrate import simpson, quad
from scipy.optimize import fsolve, root

def integrated_root_search(function,low, high):
    print("\n Пошук коренів із бібліотекою scipy: Знайдіть корінь вектор-функції: ")
    sol = root(function, [low, high])
    print(sol.x)

    print("\n Пошук коренів із бібліотекою scipy: Знайдіть корені функції:")
    sol = fsolve(function, [low, high])
    print(sol)

def integrated_iteration(function,low, high, y, x):
    print("\n Інтегрування із бібліотекою scipy: ")
    print(quad(function, low, high))

    print("\n Інтегрування із бібліотекою numpy:")
    print(np.trapezoid(y, x))

    print("\n Метод Симпсона: ")  # initial=0
    print(simpson(y, x=x))