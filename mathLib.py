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


# def transform_function_to_minus1_1(functions: list, a: float, b: float) -> float:
#     """
#     Przekształca funkcję f z przedziału [a, b] na przedział [-1, 1].
#
#     :param f: Funkcja do przekształcenia.
#     :param a: Dolna granica oryginalnego przedziału.
#     :param b: Górna granica oryginalnego przedziału.
#     :return: Przekształcona funkcja.
#     """
#
#     alpha = (b - a) / 2
#     beta = (a + b) / 2
#     t = 1 / alpha * (functions - beta)
#     return functions
