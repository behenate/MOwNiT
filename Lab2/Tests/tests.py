import numpy as np
import pandas as pd

from Spline_Interpolation.boundary_conditions import BoundaryConditions
from Spline_Interpolation.cubic_spline import CubicSplineInterpolator
from Spline_Interpolation.quadratic_spline import QuadraticSplineInterpolator
from Utils.drawing import *
from Utils.generators import *
from Interpolators.newton import Newton
from Interpolators.lagrange import Lagrange
from Interpolators.hermite import Hermite

from Utils.derivative import calculate_derivative
from Tests.errors import *



# Performs a single test on a given value, function and point distance type
def single_test(f, range_start: float, range_end: float, train_samples_num: int, mode: str = "equal",
                checkpoint: bool = False):
    ys, xs = samples_from_function(mode, f, train_samples_num, range_start, range_end)
    test_ys, test_xs = samples_from_function(mode, f, 1000, range_start, range_end)

    # Create interpolators based on equally distanced nodes
    lagrange = Lagrange(xs, ys)
    newton = Newton(xs, ys)

    lagrange_max_error = test_max_error(lagrange, test_xs, test_ys)
    lagrange_mse = test_mse(lagrange, test_xs, test_ys)
    newton_max_error = test_max_error(newton, test_xs, test_ys)
    newton_mse = test_mse(newton, test_xs, test_ys)

    print(f"Type {mode}, nodes:{train_samples_num}")

    # Draw the interpolated function, show the legend and the graph
    if (checkpoint):
        draw_funct(f, range_start, range_end)
        plt.title("{}, nodes: {}".format(mode, train_samples_num))
        plt.scatter(xs, ys, marker="o", s=20)
        draw(newton, range_start, range_end, "newton {}".format(mode), samples=1000)
        draw(lagrange, range_start, range_end, "lagrange {}".format(mode), samples=1000)

        plt.legend(loc="upper right")
        plt.show()
    return lagrange_max_error, lagrange_mse, newton_max_error, newton_mse


# Performs a set of tests on a given functions, it starts from a 2nd degree polynomial and ends at the passed
# max degree polynomial. It tests a polynomial every step degrees, in all steps provided in the checkpoints array
# will display a plot when the test is performed
# The function also saves the results to text.xlsx file
def big_test(f, range_start: float, range_end: float, checkpoints: list = [], step: int = 5, max_degree: int = 30):
    polynomial_samples = max_degree
    results = np.empty(((polynomial_samples // step) * 2, 4))
    for i in range(2, polynomial_samples, step):
        l_me, l_mse, n_me, n_mse = single_test(f, range_start, range_end, i, "equal", i in checkpoints, i)
        results[i // step] = np.array([l_me, l_mse, n_me, n_mse])

    for i in range(2, polynomial_samples, step):
        l_me, l_mse, n_me, n_mse = single_test(f, range_start, range_end, i, "chebyshev", i in checkpoints, i)
        results[i // step + polynomial_samples // step] = np.array([l_me, l_mse, n_me, n_mse])

    dataframe = pd.DataFrame(results)
    dataframe.to_excel("test.xlsx", "tests")


def single_test_hermite(f, range_start: float, range_end: float, train_samples_num: int, mode: str = "equal",
                        checkpoint: bool = False, show_derivative=True):
    ys, xs = samples_for_hermite(mode, f, train_samples_num, range_start, range_end)
    test_ys, test_xs = samples_from_function(mode, f, 1000, range_start, range_end)
    nodes_function = [elem[0] for elem in ys]
    nodes_derivative = [elem[1] for elem in ys]
    # Create interpolators based on generated nodess
    hermite = Hermite(xs, ys)

    hermite_max_error = test_max_error(hermite, test_xs, test_ys)
    hermite_mse = test_mse(hermite, test_xs, test_ys)

    print(f"Hermite test: type {mode}, nodes:{train_samples_num}")

    # Draw the interpolated function, show the legend and the graph
    if checkpoint:
        if show_derivative:
            draw_funct(lambda x: calculate_derivative(f, x), range_start, range_end, label="derivative",
                       color="#dedede")
        draw_funct(f, range_start, range_end)

        plt.title("Hermite test, {} nodes count: {}".format(mode, train_samples_num))
        plt.scatter(xs, nodes_function, marker="o", s=27)

        draw(hermite, range_start, range_end, "hermite {}".format(mode), samples=1000)
        plt.tight_layout()
        plt.legend(loc="upper right")
        plt.show()
    return hermite_max_error, hermite_mse


def hermite_tests(f, range_start: float, range_end: float, checkpoints: list = [], step: int = 5, max_degree: int = 30,
                  show_derivative=True):
    polynomial_samples = max_degree
    results = np.empty(((polynomial_samples // step) * 2, 2))
    for i in range(2, polynomial_samples, step):
        h_me, h_mse = single_test_hermite(f, range_start, range_end, i, "equal", i in checkpoints,
                                          show_derivative=show_derivative)
        results[i // step] = np.array([h_me, h_mse])

    for i in range(2, polynomial_samples, step):
        h_me, h_mse = single_test_hermite(f, range_start, range_end, i, "chebyshev", i in checkpoints,
                                          show_derivative=show_derivative)
        results[i // step + polynomial_samples // step] = np.array([h_me, h_mse])

    dataframe = pd.DataFrame(results)
    dataframe.to_excel("test_hermite.xlsx", "hermite test")



