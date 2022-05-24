import math

import numpy as np


class TrigonometricApproximation:
    def __init__(self, m, xs, ys, range_start, range_end):
        self.__m = m
        self.__n = len(xs)
        self.__xs = xs
        self.__ys = ys
        self.range_start = range_start
        self.range_end = range_end
        self.__a = np.zeros(self.__m + 1)
        self.__b = np.zeros(self.__m + 1)
        self.__scale_xs_to_2pi()
        self.__fill_a_b()
        self.__scale_xs_from_2pi()

    def __scale_xs_to_2pi(self):
        for i in range(len(self.__xs)):
            self.__xs[i] = self.__scale_to_2pi(self.__xs[i])

    def __scale_xs_from_2pi(self):
        for i in range(len(self.__xs)):
            self.__xs[i] = self.__scale_from_2pi(self.__xs[i])

    #     Scales value to a range from -pi to pi
    def __scale_to_2pi(self, value):
        range_length = self.range_end - self.range_start
        value /= range_length
        value *= 2 * math.pi
        value += -math.pi - (self.range_start/range_length * 2 * math.pi)
        return value

    def __scale_from_2pi(self, value):
        range_length = self.range_end - self.range_start
        value -= -math.pi - (self.range_start / range_length * 2 * math.pi)
        value /= 2 * math.pi
        value *= range_length
        return value

    def __calc_aj(self, j: int) -> float:
        aj = 0.0
        for i in range(self.__n):
            aj += self.__ys[i] * math.cos(j * self.__xs[i])
        return 2 * aj / self.__n

    def __calc_bj(self, j: int) -> float:
        bj = 0.0
        for i in range(self.__n):
            bj += self.__ys[i] * math.sin(j * self.__xs[i])
        return 2 * bj / self.__n

    def __fill_a_b(self):
        for i in range(self.__m + 1):
            self.__a[i] = self.__calc_aj(i)
            self.__b[i] = self.__calc_bj(i)

    def interpolate(self, x):
        x = self.__scale_to_2pi(x)
        res = self.__a[0] * 0.5
        for j in range(1, self.__m + 1):
            res += self.__a[j] * math.cos(j * x) + self.__b[j] * math.sin(j * x)
        return res

