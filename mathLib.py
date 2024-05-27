def polynomial(x: float, factors: list[float]):
    result: float = 0
    for i in range(len(factors)):
        result = result * x + factors[i]

    return result


def evaluate_composite(x: float, functions: list):
    """
    :param x: x value
    :param functions: Functions from most inner to most outer
    :return:
    """
    result: float = functions[0].evaluate(x)
    for i in range(1, len(functions)):
        result = functions[i].evaluate(result)
    return result


def power_int(x: float, exponent: int) -> float:
    for i in range(exponent):
        x *= x
    return x
