import math

from Approximation.trigonometric_approximation import TrigonometricApproximation
from Tests.Approximation.trigonometric_approximation_tests import *
import matplotlib.pyplot as plt
from Utils.drawing import draw, draw_funct
from Utils.generators import samples_from_function

if __name__ == '__main__':
    # Dróżdż Wojciech f3, k=1, m=3, [-2pi+1, pi+1]  = −k * x *sin(m(x −1))
    k = 1
    m = 3
    range_start = -2 * math.pi + 1
    range_end = math.pi + 1
    #
    # range_start = -3 * math.pi
    # range_end = 3 * math.pi

    # Create the function
    f = lambda x: -k * x * math.sin(m * (x - 1))

    ys, xs = samples_from_function("equal", f, 1000, range_start, range_end)
    approximator = TrigonometricApproximation(6, xs, ys, range_start, range_end)
    # draw(approximator, range_start, range_end)
    approximation_tests(f, range_start, range_end, [5, 10, 20, 30], [80], [3, 4, 6, 9, 20, 40])
    generate_fancy_table(f, range_start, range_end,
                         [5, 7, 9, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100])
