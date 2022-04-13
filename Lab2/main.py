import math
import numpy as np
from Spline_Interpolation.cubic_spline import CubicSplineInterpolator, BoundaryConditions
from Spline_Interpolation.quadratic_spline import QuadraticSplineInterpolator
from Tests.tests import single_test_hermite, hermite_tests
from Tests.Spline.spline_tests import single_test_quadratic, compare_spline_test
import matplotlib.pyplot as plt
from Approximation.polynomial_approximation import PolynomialApproximation
# Press the green button in the gutter to run the script.
from Utils.drawing import draw, draw_funct
from Utils.generators import samples_from_function

if __name__ == '__main__':
    # Dróżdż Wojciech f3, k=1, m=3, [-2pi+1, pi+1]  = −k * x *sin(m(x −1))
    k = 1
    m = 3
    range_start = -2 * math.pi + 1
    range_end = math.pi + 1

    # Create the function
    f = lambda x: -k * x * math.sin(m * (x - 1))
    ys, xs = samples_from_function("equal", f, 5, range_start, range_end)
    # Will run tests and display plots of the results at 3rd 5th 10th and 20th degree polynomial for both
    # equal and chebyschev nodes
    # big_test(f, range_start, range_end, checkpoints=[3, 5, 10, 20], step=1, max_degree=21)

    # Commented code, uncomment and modify to quickly test interpolations

    # from generators import *
    # from drawing import *
    #
    # f = lambda x: x ** 8 + 1

    # test_ys, test_xs = samples_from_function("equal", f, 1000, -10, 10)
    #
    # interpolator = Lagrange([-1, 0, 1], [[2, -8, 56], [1, 0, 0], [2, 8, 56]])
    #
    # draw(interpolator, -10, 10, "Lagrange")
    # single_test_hermite(f, range_start, range_end, 5, checkpoint=True, mode="chebyschev")
    # hermite_tests(f, range_start, range_end, checkpoints=[3, 5, 7, 9, 11, 13, 19, 25, 30, 45], step=1,
    #               max_degree=50)
    # quadInterpolator = QuadraticSplineInterpolator(np.array(xs), np.array(ys), BoundaryConditions.ZEROS)
    # draw_funct(f, range_start, range_end)
    # single_test_quadratic(f, QuadraticSplineInterpolator, BoundaryConditions.ZEROS, range_start, range_end, 20, True)
    compare_spline_test(f,
                        QuadraticSplineInterpolator, BoundaryConditions.ZEROS,
                        CubicSplineInterpolator, BoundaryConditions.ZEROS,
                        range_start, range_end, checkpoints=[10], max_degree=205)

    # approximator = PolynomialApproximation(4, np.array([1,2,3]), np.array([1,4,9]))
    # draw(approximator, range_start, range_end, samples=100)
    # plt.show()
#
