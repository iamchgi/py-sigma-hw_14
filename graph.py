import numpy as np
from matplotlib import pyplot as plt


def graph_fun(fun, lo, hi, n) -> None:
    """
    Метод візуалізації функції
    :param fun: лямбда функція
    :param lo: початкове значення інтервалу
    :param hi: кінцеве значення інтервалу
    :param n: кількість значень в інтервалі
    :return: nothing
    """
    x = np.linspace(lo, hi, n)
    y = fun(x)
    fig, ax = plt.subplots()
    plt.grid(True)
    ax.plot(x, y)
    plt.show()


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


def main(low, high, n, a, b, c):
    # Задаємо лямбда функцію
    function = lambda x: a * x ** 4 + b * x + c
    # створення одновимірного масиву з рівномірно розподіленими значеннями на вказаному інтервалі.
    x = np.linspace(low, high, num=n)
    # Задаємо нелінійне рівняння для підінтегральної функції
    y = a * x ** 4 + b * x + c
    graph_equation(y, x)