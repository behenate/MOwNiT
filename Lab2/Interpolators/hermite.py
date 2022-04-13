# Class for a polynomial interpolator, which uses Hermite's method
import math


class Hermite:
    def __init__(self, points=None, values=None):
        self.__points = []
        # Value is a 2D array of values where values[0] is an array of lenght n, which corresponds to first n
        # derivatives of the point located in points[0]
        self.__values = []
        self.__differential_quotient = []
        for i in range(len(points)):
            self.add_node(points[i], values[i])

    # fills the last rows of the differential_quotient with given derivatives.
    def __fill_rows(self, start_row, derivatives):
        for i in range(len(derivatives)):
            for j in range(i + 1):
                factorial = math.factorial(j)
                self.__differential_quotient[start_row + i][j] = derivatives[j] / factorial

    # Adds a new x and f(x) value to the interpolator
    def add_node(self, point: float, derivatives: list):
        n = len(self.__differential_quotient)
        num_derivatives = len(derivatives)
        for i in range(len(derivatives)):
            self.__points.append(point)
        self.__values.append(derivatives)
        for _ in range(num_derivatives):
            self.__differential_quotient.append([0] * (n + num_derivatives))
        self.__fill_rows(n, derivatives)
        for i in range(num_derivatives):
            self.calculate_row(n + i, i+1)

    # Calculates given differential_quotient row
    def calculate_row(self, row, start_idx):
        for i in range(start_idx, row+1):
            dq = self.__differential_quotient
            dq[row][i] = ":)"
            dq[row][i] = (dq[row][i-1] - dq[row - 1][i-1]) / (self.__points[row] - self.__points[row - i])

    # Works basically the same as the Newtons interpolate method
    def interpolate(self, x):
        n = len(self.__points)
        dq = self.__differential_quotient
        interpolated = self.__values[0][0]
        multi_arr = [1] * n
        for i in range(1, n):
            multi_arr[i] = multi_arr[i - 1] * (x - self.__points[i - 1])
            interpolated += dq[i][i] * multi_arr[i]
        return interpolated


