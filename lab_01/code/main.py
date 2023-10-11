import matplotlib.pyplot as plt
from scipy.stats import expon
import numpy as np
from math import exp


def ud_function(a, b, x_arr):
    return [(x - a) / (b - a) if a <= x < b else 0 if x < a else 1 for x in x_arr]


def ud_density(a, b, x_arr):
    return [1 / (b - a) if a <= x <= b else 0 for x in x_arr]

def expon(x, lambda_):
    return 1 - exp(lambda_ * -1 * x) if x >= 0 else 0

def hyperexpon(x, lambdas, probabilities):
    sum_arr = []
    for num in x:
        sum_arr.append(0)
        for lam, prob in zip(lambdas, probabilities):
            sum_arr[-1] += prob * expon(num, lam)
    return sum_arr

def expon_density(x, lambda_):
    return lambda_ * exp(lambda_ * -1 * x) if x >= 0 else 0

def hyperexpon_dens(x, lambdas, probabilities):
    sum_arr = []
    for num in x:
        sum_arr.append(0)
        for i in range(len(lambdas)):
            sum_arr[-1] += probabilities[i] * expon_density(num, lambdas[i])
    return sum_arr

def main():
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    delta = b - a
    x = np.linspace(a - delta / 2, b + delta / 2, 1000)
    y_function = ud_function(a, b, x)
    y_density = ud_density(a, b, x)

    # plt.subplot(221)
    plt.title('Функция равномерного распределения')
    plt.plot(x, y_function, color='r', label=r'F({0}, {1})'.format(a, b))
    plt.legend()
    plt.show()

    # plt.subplot(223)
    plt.title('Функция плотности равномерного распределения')
    plt.plot(x, y_density, color='r', label=r'f({0}, {1})'.format(a, b))
    plt.legend()
    plt.show()

    lambda_ = list(map(float, input("Введите лямбды: ").split()))
    # print(lambda_)
    probabilities = list(map(float, input("Введите вероятности соответствующих компонент: ").split()))
    if any([i for i in probabilities if i < 0]):
        print("Вероятность не может быть отрицательной")
        return
    if sum(probabilities) != 1:
        print("Сумма вероятностей должна быть равна 1")
        return
    if len(probabilities) != len(lambda_):
        print("Количество вероятностей не совпадает с количеством компонент")
        return
    x = np.linspace(0, 100, 10000)
    y_function = hyperexpon(x, lambda_, probabilities)
    y_density = hyperexpon_dens(x, lambda_, probabilities)

    # plt.subplot(222)
    plt.title('Функция гиперэкспоненциального распределения')
    plt.plot(x, y_function, color='b', label=r'f({0} {1})'.format(lambda_, probabilities))
    plt.legend()
    plt.show()

    # plt.subplot(224)
    plt.title('Функция плотности гиперэкспоненциального распределения')
    plt.plot(x, y_density, color='b', label=r'f({0} {1})'.format(lambda_, probabilities))
    plt.legend()
    plt.show()

    # plt.show()


if __name__ == '__main__':
    main()