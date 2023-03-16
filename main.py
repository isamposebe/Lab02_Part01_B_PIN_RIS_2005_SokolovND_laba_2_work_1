import libe
import math
def f(x):
    return x * math.exp(x) * math.pow(math.sin(x), 2)

interval = [5, 10]


# Нахождение интервала экстремума
(min_val, min_arg), (max_val, max_arg) = libe.find_extremum(f, interval)

print(f"Минимум функции f(x) = {min_val:.4f} достигается в точке x = {min_arg:.4f}")
print(f"Максимум функции f(x) = {max_val:.4f} достигается в точке x = {max_arg:.4f}")


# Нахождение минимума функции на заданном интервале
print("Минимум функции на заданном интервале, найденный методом золотого сечения:")
print(libe.golden_section_minimize(f, interval[0], interval[1]))

print("Минимум функции на заданном интервале, найденный методом дихотомии:")
print(libe.dichotomy_minimize(f, interval[0], interval[1]))
# Построение графика функции
libe.plot_func(f, interval)