import mathLib
import math


def gauss_chebyshev(functions: list, nodes_amount: int, data: list, n: int) -> float:
    result = 0
    for i in range(nodes_amount):
        w = data[i][0]
        x = data[i][1]
        result += w * mathLib.evaluate_composite(x, functions) * chebyshev_poly(n, x)
    return result


def chebyshev_poly(n: int, x: float) -> float:
    result = [1, x]
    for n in range(2, n + 1):
        result.append(2 * x * result[n - 1] - result[n - 2])
    return result[n]


def chebyshev_coef(functions: list, nodes_amount: int, data: list, n: int):
    poly = []
    for i in range(n + 1):
        if i == 0:
            wsp = 1 / math.pi * gauss_chebyshev(functions, nodes_amount, data, i)
        else:
            wsp = 2 / math.pi * gauss_chebyshev(functions, nodes_amount, data, i)
        poly.append(wsp)
    return poly


def chebyshev_calc(n, x, array):
    result = 0
    for i in range(n + 1):
        result += array[i] * chebyshev_poly(i, x)
    return result
