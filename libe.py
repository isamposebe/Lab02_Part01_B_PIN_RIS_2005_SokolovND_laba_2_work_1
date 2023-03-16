import math
import matplotlib.pyplot as plt

def plot_func(f, interval):
    x_vals = [i/10 for i in range(-100, 101)]
    y_vals = [f(x) for x in x_vals]
    plt.plot(x_vals, y_vals)
    plt.xlim(interval[0], interval[1])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def find_extremum(f, interval):
    min_val = f(interval[0])
    max_val = f(interval[0])
    min_arg = interval[0]
    max_arg = interval[0]

    x_vals = [i/10 for i in range(-100, 101)]
    for x in x_vals:
        if x < interval[0] or x > interval[1]:
            continue
        y = f(x)
        if y < min_val:
            min_val = y
            min_arg = x
        if y > max_val:
            max_val = y
            max_arg = x

    return (min_val, min_arg), (max_val, max_arg)

def golden_section_minimize(f, a, b, tol=1e-6):
    phi = (1 + math.sqrt(5)) / 2 # Константа "золотого сечения"
    c = b - (b - a) / phi
    d = a + (b - a) / phi

    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        c = b - (b - a) / phi
        d = a + (b - a) / phi

    return (c + d) / 2

def dichotomy_minimize(f, a, b, tol=1e-6):
    while abs(b - a) > tol:
        c = (a + b) / 2
        d = (a + c) / 2
        if f(d) < f(c):
            b = c
        else:
            a = d
    return (a + b) / 2

def minimize(f, interval, method='golden', tol=1e-6):
    if method == 'golden':
        return golden_section_minimize(f, interval[0], interval[1], tol)
    elif method == 'dichotomy':
        return dichotomy_minimize(f, interval[0], interval[1], tol)
    else:
        raise ValueError(f"Unsupported optimization method: {method}")

def find_min(f, interval, method='golden', tol=1e-6):
    x_min = minimize(f, interval, method, tol)
    return (x_min, f(x_min))