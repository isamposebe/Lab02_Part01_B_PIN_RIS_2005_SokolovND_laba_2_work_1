import libe
import math
interval = [-10, 10]
def f(x):
    return x * math.exp(x) * math.pow(math.sin(x), 2)
def main():


    # Нахождение интервала экстремума
    (min_val, min_arg), (max_val, max_arg) = libe.find_extremum(f, interval)

    print(f"Минимум функции f(x) = {min_val:.4f} достигается в точке x = {min_arg:.4f}")
    print(f"Максимум функции f(x) = {max_val:.4f} достигается в точке x = {max_arg:.4f}")


    # Нахождение минимума функции на заданном интервале
    print("Минимум функции на заданном интервале, найденный методом золотого сечения:")
    print(libe.golden_section_minimize(f, interval[0], interval[1], math.pow(10, -2)))

    print("Минимум функции на заданном интервале, найденный методом дихотомии:")
    print(libe.dichotomy_minimize(f, interval[0], interval[1], math.pow(10, -2)))
    # Построение графика функции
    libe.plot_func(f, interval)
def tabl1():
    print("Минимум функции на заданном интервале, найденный методом золотого сечения:")
    print(libe.golden_section_minimize(f, interval[0], interval[1], math.pow(10, -2)))
    print(libe.golden_section_minimize(f, interval[0], interval[1], math.pow(10, -3)))
    print(libe.golden_section_minimize(f, interval[0], interval[1], math.pow(10, -4)))
    print(libe.golden_section_minimize(f, interval[0], interval[1], math.pow(10, -5)))
    print(libe.golden_section_minimize(f, interval[0], interval[1], math.pow(10, -6)))
    print(libe.golden_section_minimize(f, interval[0], interval[1], math.pow(10, -7)))

    print("Минимум функции на заданном интервале, найденный методом дихотомии:")
    print(libe.dichotomy_minimize(f, interval[0], interval[1], math.pow(10, -2)))
    print(libe.dichotomy_minimize(f, interval[0], interval[1], math.pow(10, -3)))
    print(libe.dichotomy_minimize(f, interval[0], interval[1], math.pow(10, -4)))
    print(libe.dichotomy_minimize(f, interval[0], interval[1], math.pow(10, -5)))
    print(libe.dichotomy_minimize(f, interval[0], interval[1], math.pow(10, -6)))
    print(libe.dichotomy_minimize(f, interval[0], interval[1], math.pow(10, -7)))

def test():
    print("Минимум функции на заданном интервале, найденный методом золотого сечения:")
    print(libe.golden_section_minimize(f, interval[0], interval[1], math.pow(10, -4)))

    print("Минимум функции на заданном интервале, найденный методом дихотомии:")
    print(libe.dichotomy_minimize(f, interval[0], interval[1], math.pow(10, -4)))





if __name__ == '__main__':
    main()
    tabl1()
    test()
