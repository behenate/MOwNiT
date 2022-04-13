import numpy
import numpy as np
from Spline_Interpolation.boundary_conditions import BoundaryConditions

class QuadraticSplineInterpolator:
    def __init__(self, xs: np.array, ys: np.array, boundary_condition: BoundaryConditions):
        self.__points = xs
        self.__values = ys
        self.__n = 3 * (len(xs) - 1)
        self.__known = np.zeros(self.__n)
        self.__coefficients = np.zeros(self.__n)
        self.__unknowns_matrix = np.zeros((self.__n, self.__n))
        self.__has_been_solved = False
        self.__boundary_condition = boundary_condition

    def __fill_known(self):
        for i in range(0, 2 * (len(self.__points) - 1), 2):
            self.__known[i] = self.__values[i // 2]
            self.__known[i + 1] = self.__values[i // 2 + 1]
        for i in range(2 * (len(self.__points) - 1), self.__n, 1):
            self.__known[i] = 0

        if self.__boundary_condition == BoundaryConditions.CLAMPED:
            self.__known[-1] = (self.__values[-1] - self.__values[-2]) / (self.__points[-1]-self.__points[-2])

    def __fill_unknowns_matrix(self):
        m = len(self.__points) - 1
        unknowns_matrix = self.__unknowns_matrix
        xs = self.__points
        for i in range(0, 2 * m, 2):
            for j in range(3):
                unknowns_matrix[i][i // 2 * 3 + j] = xs[i // 2] ** (2 - j)
                unknowns_matrix[i + 1][i // 2 * 3 + j] = xs[i // 2 + 1] ** (2 - j)
        for i in range(0, m - 1):
            row = 2 * m + i
            unknowns_matrix[row][i * 3] = 2 * xs[i + 1]
            unknowns_matrix[row][i * 3 + 1] = 1
            unknowns_matrix[row][i * 3 + 3] = -2 * xs[i + 1]
            unknowns_matrix[row][i * 3 + 4] = -1
        if self.__boundary_condition == BoundaryConditions.ZEROS:
            unknowns_matrix[-1][0] = 1
        elif self.__boundary_condition == BoundaryConditions.CLAMPED:
            unknowns_matrix[-1][-2] = 1
            unknowns_matrix[-1][-3] = 2 * self.__points[-1]

    def __solve(self):
        self.__fill_unknowns_matrix()
        self.__fill_known()
        self.__coefficients = np.linalg.solve(self.__unknowns_matrix, self.__known)
        self.__has_been_solved = True

    def interpolate(self, x: float):
        if not self.__has_been_solved:
            self.__solve()
        spline_idx = 0
        points = self.__points
        coefficients = self.__coefficients
        while spline_idx + 1 < len(points) and not (points[spline_idx] <= x <= points[spline_idx + 1]):
            spline_idx += 1
        if spline_idx * 3 >= self.__n:
            raise ValueError("Given X is out of bounds for provided data!")
        a = coefficients[spline_idx * 3]
        b = coefficients[spline_idx * 3 + 1]
        c = coefficients[spline_idx * 3 + 2]
        return a * x ** 2 + b * x + c

    def __str__(self):
        boundary = "zeroes" if self.__boundary_condition == BoundaryConditions.ZEROS else "clamped"
        return "Quadratic spline, {}".format(boundary)