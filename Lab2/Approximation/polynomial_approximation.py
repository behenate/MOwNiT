import numpy as np


class PolynomialApproximation:
    def __init__(self, polynomial_degree, xs, ys):
        self.__m = polynomial_degree + 1
        self.__xs = xs
        self.__ys = ys
        self.__matrix = np.zeros((self.__m, self.__m))
        self.__known = np.zeros(self.__m)
        self.__weights = np.array([1 for _ in range(len(ys))])
        self.__coefficients = np.zeros(self.__m)
        self.__fill_known()
        self.__fill_unknown()
        self.__solve()

    def __fill_known(self):
        xs = self.__xs
        ys = self.__ys
        w = self.__weights
        for i in range(self.__m):
            for j in range(len(xs)):
                self.__known[i] += w[j] * ys[j] * (xs[j] ** i)

    def __fill_unknown(self):
        sums = np.zeros((2 * self.__m))
        # print(self.__xs)
        for i in range(2 * self.__m):
            for j in range(len(self.__xs)):
                sums[i] += self.__weights[j] * (self.__xs[j] ** i)

        m = self.__matrix
        for i in range(self.__m):
            for j in range(self.__m):
                m[i][j] = sums[j + i]
        # print(m)

    # Should be called approximate, but I want it to be compatible with all the
    def interpolate(self, x):
        result = 0
        for i in range(self.__m):
            result += self.__coefficients[i] * x ** i
        return result

    def __solve(self):
        self.__coefficients = np.linalg.solve(self.__matrix, self.__known)
        # print(self.__coefficients)

