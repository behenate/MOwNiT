import numpy as np
from enum import Enum

from Spline_Interpolation.boundary_conditions import BoundaryConditions

np.set_printoptions(linewidth=1000)


class CubicSplineInterpolator:
    def __init__(self, xs: np.array, ys: np.array, boundary_condition: BoundaryConditions):
        if boundary_condition != BoundaryConditions.LAST4 and boundary_condition != BoundaryConditions.ZEROS:
            raise AttributeError("Cubic interpolator only accepts ZEROS and CUBIC boundary conditions")
        self.__n = len(xs)
        self.__x = xs
        self.__y = ys
        self.__boundary_condition = boundary_condition
        self.__h = np.array([xs[i + 1] - xs[i] for i in range(len(xs) - 1)])
        self.__delta = np.array([(ys[i + 1] - ys[i]) / self.__h[i] for i in range(len(xs) - 1)])
        self.__known = np.zeros(self.__n)
        self.__sigma = np.zeros(self.__n)
        self.__unknowns_matrix = np.zeros((self.__n, self.__n))
        self.__has_been_solved = False
        self.__fill_known()
        self.__fill_unknowns_matrix()
        self.__solve_sigma()

    def __fill_known(self):
        for i in range(1, self.__n - 1):
            self.__known[i] = self.__delta[i] - self.__delta[i - 1]
        if self.__boundary_condition == BoundaryConditions.ZEROS:
            self.__known[0] = 0
            self.__known[self.__n - 1] = 0
        elif self.__boundary_condition == BoundaryConditions.LAST4:
            self.__known[0] = self.__h[0]**2 * self.get_third_delta(0)
            self.__known[-1] = (-1) * self.__h[-1]**2 * self.get_third_delta(self.__n-3)

    def __fill_unknowns_matrix(self):
        matrix = self.__unknowns_matrix
        h = self.__h
        for i in range(1, self.__n - 1):
            matrix[i][i - 1] = h[i - 1]
            matrix[i][i] = 2 * (h[i - 1] + h[i])
            matrix[i][i + 1] = h[i]
        if self.__boundary_condition == BoundaryConditions.ZEROS:
            matrix[0][0] = 1
            matrix[-1, -1] = 1
        elif self.__boundary_condition == BoundaryConditions.LAST4:
            matrix[0][0] = -self.__h[0]
            matrix[0][1] = self.__h[0]
            matrix[-1][-1] = -self.__h[-1]
            matrix[-1][-2] = self.__h[-1]
    def __solve_sigma(self):
        self.__sigma = np.linalg.solve(self.__unknowns_matrix, self.__known)

    def __find_range(self, x):
        spline_idx = 0
        points = self.__x
        while spline_idx + 1 < len(points) and not (points[spline_idx] <= x <= points[spline_idx + 1]):
            spline_idx += 1
        if spline_idx >= self.__n:
            raise ValueError("Given X is out of bounds for provided data!")
        return spline_idx

    def interpolate(self, x: float):
        i = self.__find_range(x)
        s = self.__sigma
        h = self.__h
        y = self.__y
        xs = self.__x
        return s[i] / h[i] * (xs[i + 1] - x) ** 3 + \
               s[i + 1] / h[i] * (x - xs[i]) ** 3 + \
               (y[i + 1] / h[i] - s[i + 1] * h[i]) * (x - xs[i]) + \
               (y[i] / h[i] - s[i] * h[i]) * (xs[i + 1] - x)

    def get_third_delta(self, start_idx):
        dq = np.zeros((3, 3))
        for i in range(3):
            dq[i][0] = self.__y[start_idx + i]
        for row in range(3):
            for i in range(row):
                dq[row][i + 1] = (dq[row][i] - dq[row - 1][i]) / (self.__x[row] - self.__x[row - i - 1])
        return dq[2][2]

    def __str__(self):
        boundary = "zeroes" if self.__boundary_condition == BoundaryConditions.ZEROS else "last four points"
        return "Cubic spline, {}".format(boundary)

# lol = CubicSplineInterpolator(np.array([0, 10, 15, 20, 22.5, 30]),
#                               np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67]), EdgeCases.CUBIC)

# lol.interpolate(12)
# from Utils.drawing import draw, draw_nodes
# import matplotlib.pyplot as plt
#
# draw(lol, 0, 30)
# draw_nodes([0, 10, 15, 20, 22.5, 30], [0,227.04,362.78,517.35,602.97,901.67])
# plt.show()
