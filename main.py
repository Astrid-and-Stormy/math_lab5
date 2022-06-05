import numpy as np
import matplotlib.pyplot as plt
import math
x = [1.10, 1.25, 1.40, 1.55, 1.70, 1.85, 2]
y = [0.2234, 1.2438, 2.2644, 3.2984, 4.3222, 5.3516, 6.3867]
x1 = 1.168
x2 = 1.463


def polynomial_Lagrange(x, y, n, x1):
    result = 0
    for i in range(n):
        power = 1
        for j in range(n):
            if i != j:
                power *= (x1-x[j])/(x[i]-x[j])
        result += y[i]*power
    return result


def polynomial_Newton(x, y, n, h, x1):
    t = (x1 - x[0])/h
    deltas_y = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n-i):
            if i == 0:
                deltas_y[j][i] = y[j]
            else:
                deltas_y[j][i] = deltas_y[j+1][i-1] - deltas_y[j][i-1]
    result = 0
    power = 1
    for i in range(n):
        result += deltas_y[0][i]*power
        power *= t/(i+1)
        t -= 1
    return result


def read_parameters():
    print("Введите количество известных параметров. Для выхода напишите exit.")
    n = input()
    if n == "exit":
        return n, None, None
    try:
        n = int(n)
    except:
        print("Ошибка. Введите число")
        return None, None, None
    x = []
    y = []
    print("Введите х и у через пробел")
    rows = 0
    while rows < n:
        try:
            row = list(map(float, input().split()))
        except:
            print("Ошибка ввода")
        if len(row) == 2:
            x.append(row[0])
            y.append(row[1])
            rows += 1
        else:
            print("Ошибка. Введите два числа через пробел")
    print("Введите аргумент, значение которого хотите найти")
    k = None
    while k is None:
        try:
            k = float(input())
        except:
            print("Че-то не то. Давай еще раз")
    return x, y, k


def main():
    print("Посчитаем интерполяции? Понятия не имею зачем это, но вот вам прога")
    while True:
        x, y, k = read_parameters()
        while x is None:
            x, y, k = read_parameters()
        if x == "exit":
            print("До свидания. Ждем вас еще")
            break
        try:
            ans = polynomial_Lagrange(x, y, len(x), k)
            print("Используя полином Лагранжа, значение функции в точке", k, "равно", ans)
        except:
            print("Невозможно составить полином. Вероятно во входных данных была ошибка")
        is_dif_equal = False
        if len(x) > 1:
            is_dif_equal = True
            dif = x[1] - x[0]
            for i in range(len(x)-1):
                is_dif_equal =  x[i+1] - x[i] == dif
                if not is_dif_equal:
                    break
            if is_dif_equal:
                try:
                    ans = polynomial_Newton(x, y, len(x), dif, k)
                    print("Используя полином Ньютона, значение функции в точке", k, "равно", ans)
                except:
                    is_dif_equal = False
                    print("Невозможно составить полином. Вероятно во входных данных была ошибка")
            else:
                print("В программе реализован полином Ньютона с конечными разностями. Введеные параметры не "
                      "соответствуют этому условию")
        plt.plot(x, y, "o")
        if is_dif_equal:
            y_Newton = []
            x_polynomial = np.arange(x[0], x[-1], (x[1] - x[0]) / 100)
            for i in x_polynomial:
                y_Newton.append(polynomial_Newton(x_polynomial, y, len(y), x[1]-x[0], i))
            plt.plot(x_polynomial, y_Newton)
        print("Чтобы продолжить, закройте график")
        plt.show()


# print(polynomial_Lagrange(x, y, len(x), x1))
# print(polynomial_Lagrange(x, y, len(x), x2))
# print(polynomial_Newton(x, y, len(x), x[1]-x[0], x1))
# print(polynomial_Newton(x, y, len(x), x[1]-x[0], x2))
# x = [0.1, 0.2, 0.3, 0.4, 0.5]
# y = [1.25, 2.38, 3.79, 5.44, 7.14]
main()


