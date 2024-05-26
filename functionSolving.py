import mathLib
import math


def newton_cotes(functions: list, left_boundary: float, right_boundary: float, precision: float) -> float:
    previous = 0
    n = 1
    while True:
        current = 0
        delta = (right_boundary - left_boundary) / n
        current += simpson_weight(left_boundary, functions) + simpson_weight(right_boundary, functions)
        for i in range(int(n / 2)):
            current += 4 * simpson_weight(left_boundary + (2 * i - 1) * delta, functions)
            current += 2 * simpson_weight(left_boundary + (2 * i) * delta, functions)
            i += 1
        current *= delta / 3
        n *= 2
        if math.fabs(previous - current) < precision:
            return current
        previous = current


def newton_cotes_limes(functions: list, precision: float) -> float:
    a = result = 0
    b = 0.5
    condition = True
    while condition:
        current = newton_cotes(functions, a, b, precision)
        result += current
        if math.fabs(current) < math.fabs(precision):
            condition = False
        a = b
        b += (1 - b)/2

    a = 0
    b = -0.5
    while True:
        current = newton_cotes(functions, b, a, precision)
        result += current
        if math.fabs(current) < precision:
            return result
        a = b
        b -= (1 - math.fabs(b)) / 2


def simpson_weight(value: float, functions: list) -> float:
    value = mathLib.evaluate_composite(value, functions) * 1 / math.sqrt(1 - value * value)
    return value


def gauss_chebyshev(functions: list, nodes_amount: int, data: list) -> float:
    result = 0
    for i in range(nodes_amount):
        w = data[i][0]
        x = data[i][1]
        result += w * mathLib.evaluate_composite(x, functions)
    return result
