import mathLib
import math


def gauss_chebyshev(functions: list, nodes_amount: int, data: list, n: int) -> float:
    result = 0
    for i in range(nodes_amount):
        w = data[i][0]
        x = data[i][1]
        result += w * mathLib.evaluate_composite(x, functions) * approx_polynomial(n, x)
    return result


def approx_polynomial(n: int, x: float):
    """
    :param n: stopień wielomianu (int)
    :param x: argument funkcji (float)
    :return: Wielomian Czebyszewa dla x stopnia n
    """
    result = [1, x]
    for n in range(2, n + 1):
        result.append(2 * x * result[n - 1] - result[n - 2])
    return result[n]


def wsp_apro(functions: list, nodes_amount: int, data: list, n: int):
    """
    :param wybor_funkcji: -//-
    :param liczba_wezlow: -//-
    :param n: -//-
    :return: wspołczynnik wielomianu aproksymujacego
    """
    wsp = (2 * n) / 2 * gauss_chebyshev(functions, nodes_amount, data, n)
    return wsp


def wsp_wielomian(functions: list, nodes_amount: int, data: list, n: int):
    """
    :param wybor_funkcji: -//-
    :param liczba_wezlow: -//-
    :param n: -//-
    :return: lista wspołczynników wielomianu aproksymującego
    """
    wielomian = []
    for i in range(n):
        wielomian.append(wsp_apro(functions, nodes_amount, data, i))
    return wielomian


def wart_wielomian(n, x, tab_wsp):
    """
    :param n: -//-
    :param x: -//-
    :param tab_wsp: -//-
    :return: wartość wielomianu aproksymującego dla argumentu x
    """
    poly = 0
    for i in range(n):
        poly += tab_wsp[i] * approx_polynomial(i, x)
    return poly
