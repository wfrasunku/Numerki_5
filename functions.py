import math
import mathLib


class Polynomial:
    def __init__(self, factors: list[float]):
        self.__factors = factors
        self.__derivativeFactors = [0.0] * (len(factors) - 1)
        for i in range(len(factors) - 1):
            self.__derivativeFactors[i] = (len(factors) - i - 1) * factors[i]

    def evaluate(self, x: float) -> float:
        return mathLib.polynomial(x, self.__factors)


class Abs:
    @staticmethod
    def evaluate(x: float) -> float:
        return abs(x)


class Sinus:
    @staticmethod
    def evaluate(x: float) -> float:
        return math.sin(x)


class Cosinus:
    @staticmethod
    def evaluate(x: float) -> float:
        return math.cos(x)


class Tangens:
    @staticmethod
    def evaluate(x: float) -> float:
        return math.tan(x)


class Cotangens:
    @staticmethod
    def evaluate(x: float) -> float:
        return 1 / math.tan(x)
