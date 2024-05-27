import mathLib
import math


def gauss_chebyshev(functions: list, nodes_amount: int, data: list, n: int) -> float:
    result = 0
    for i in range(nodes_amount):
        w = data[i][0]
        x = data[i][1]
        result += w * mathLib.evaluate_composite(x, functions) * chebyshev_polynomial(n, x)
    return result


def chebyshev_polynomial(n: int, x: float) -> float:
    result = [1, x]
    for n in range(2, n + 1):
        result.append(2 * x * result[n - 1] - result[n - 2])
    return result[n]


def chebyshev_approximation(functions: list, nodes_amount: int, data: list, n: int) -> list:
    array = []
    for i in range(n + 1):
        if i == 0:
            coef = 1 / math.pi * gauss_chebyshev(functions, nodes_amount, data, i)
        else:
            coef = 2 / math.pi * gauss_chebyshev(functions, nodes_amount, data, i)
        array.append(coef)
    return array


def approximation_evaluate(n: int, x: float, array: list) -> float:
    result = 0
    for i in range(n + 1):
        result += array[i] * chebyshev_polynomial(i, x)
    return result


def approximation_error(functions: list, nodes_amount: int, data: list, n: int, array: list):
    error = 0
    for i in range(nodes_amount):
        w = data[i][0]
        x = data[i][1]
        # x = - 1 + 2 * (x - a)/(b - a)
        error += w * (mathLib.evaluate_composite(x, functions) - approximation_evaluate(n, x, array))**2
    return error
