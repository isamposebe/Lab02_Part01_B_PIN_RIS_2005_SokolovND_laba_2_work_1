import math
import matplotlib.pyplot as plt


def plot_func(f, interval):
    x_vals = [i/10 for i in range(-100, 101)]
    y_vals = [f(x) for x in x_vals]
    plt.plot(x_vals, y_vals)
    plt.xlim(interval[0], interval[1])
    plt.ylim(min(y_vals), max(y_vals))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def find_extremum(f, interval):
    min_val = f(interval[0])
    max_val = f(interval[0])
    min_arg = interval[0]
    max_arg = interval[0]

    x_vals = [i/10 for i in range(int(interval[0]*10), int(interval[1]*10) + 1)]
    for x in x_vals:
        y = f(x)
        if y < min_val:
            min_val = y
            min_arg = x
        if y > max_val:
            max_val = y
            max_arg = x


    return (min_val, min_arg), (max_val, max_arg)

def golden_section_minimize(f, a, b, tol):

    phi = (1 + math.sqrt(5)) / 2  # Константа "золотого сечения"
    c = b - (b - a) / phi
    d = a + (b - a) / phi
    n_iter = 0  # Переменная для подсчета итераций

    while abs(c - d) > tol:
        n_iter += 1
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / phi
        d = a + (b - a) / phi

    x_min = (c + d) / 2  # Найденный минимум функции
    return x_min, n_iter

def dichotomy_minimize(f, a, b, tol):
    iter_count = 0
    while abs(b - a) > tol:
        c = (a + b) / 2
        d = (a + c) / 2
        if f(d) < f(c):
            b = c
        else:
            a = d
        iter_count += 1
    return (a + b) / 2, iter_count


