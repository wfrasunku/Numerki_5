import mathLib
import math


def gauss_chebyshev(functions: list, nodes_amount: int, data: list, n: int) -> float:
    result = 0
    for i in range(nodes_amount):
        w = data[i][0]
        x = data[i][1]
        #u = (right_boundary - left_boundary) / 2 * x + (left_boundary + right_boundary) / 2
        result += w * mathLib.evaluate_composite(x, functions) * chebyshev_polynomial(n, x)
    return result


def chebyshev_polynomial(n: int, x: float) -> float:
    result = [1, x]
    for n in range(2, n + 1):
        result.append(2 * x * result[n - 1] - result[n - 2])
    return result[n]

def wsp_wielomian(functions: list, nodes_amount: int, data: list, n: int):
    """
    :param wybor_funkcji: -//-
    :param liczba_wezlow: -//-
    :param k: -//-
    :return: lista wspołczynników wielomianu aproksymującego
    """
    wielomian = []
    for i in range(n + 1):
        if i == 0:
            wsp = 1 / math.pi * gauss_chebyshev(functions, nodes_amount, data, i)
        else:
            wsp = 2 / math.pi * gauss_chebyshev(functions, nodes_amount, data, i)
        wielomian.append(wsp)
    return wielomian


def wart_wielomian(n, x, tab_wsp):
    """
    :param n: -//-
    :param x: -//-
    :param tab_wsp: -//-
    :return: wartość wielomianu aproksymującego dla argumentu x
    """
    poly = 0
    for i in range(n + 1):
        poly += tab_wsp[i] * chebyshev_polynomial(i, x)
    return poly
