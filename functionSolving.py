import mathLib
import math


def gauss_chebyshev(functions: list, nodes_amount: int, data: list) -> float:
    result = 0
    for i in range(nodes_amount):
        w = data[i][0]
        x = data[i][1]
        result += w * mathLib.evaluate_composite(x, functions)
    return result


def approx_polynomial(n: int, x: float) -> float:
    """
    :param n: stopień wielomianu (int)
    :param x: argument funkcji (float)
    :return: Wielomian Czebyszewa dla x stopnia n
    """
    result = [1, x]
    for n in range(2, n):
        result.append(2 * x * result[n - 1] - result[n - 2])
    return result[n]


