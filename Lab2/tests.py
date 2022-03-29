import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from drawing import *
from generators import *
from newton import Newton
from lagrange import Lagrange


# Tests the max deviation from the correct value
def test_max_error(interpolator, xs, ys):
    max_error = 0

    for i in range(len(ys)):
        # print(abs(ys[i] - interpolator.interpolate(xs[i])))
        max_error = max(max_error, abs(ys[i] - interpolator.interpolate(xs[i])))
    return max_error


# Tests the sum of squares od deviations from the correct value
def test_mse(interpolator, xs, ys):
    mse = 0
    for i in range(len(ys)):
        mse += (ys[i] - interpolator.interpolate(xs[i])) ** 2
    return mse


def single_test_eq(f, range_start, range_end, train_samples_num, mode="equal", checkpoint=False, iteration=-1):
    ys, xs = samples_from_function(mode, f, train_samples_num, range_start, range_end)
    test_ys, test_xs = samples_from_function(mode, f, 1000, range_start, range_end)

    # Create interpolators based on equally distanced nodes
    lagrange = Lagrange(xs, ys)
    newton = Newton(xs, ys)

    lagrange_max_error = test_max_error(lagrange, test_xs, test_ys)
    lagrange_mse = test_mse(lagrange, test_xs, test_ys)
    newton_max_error = test_max_error(newton, test_xs, test_ys)
    newton_mse = test_mse(newton, test_xs, test_ys)

    print(f"Type {mode}, iteration:{iteration}")

    # Draw the interpolated function, show the legend and the graph
    if (checkpoint):
        draw_funct(f, range_start, range_end)
        plt.title("{}, iteration: {}".format(mode, iteration))
        plt.scatter(xs, ys, marker="o", s=4)
        draw(lagrange, range_start, range_end, "lagrange {}".format(mode), samples=1000)
        draw(newton, range_start, range_end, "newton {}".format(mode), samples=1000)

        plt.legend(loc="upper right")
        plt.show()
        return lagrange_max_error, lagrange_mse, newton_max_error, newton_mse
    return lagrange_max_error, lagrange_mse, newton_max_error, newton_mse


def big_test(f, range_start, range_end, checkpoints=[], step=5, samples=100):
    polynomial_samples = samples
    results = np.empty(((polynomial_samples // step) * 2, 4))
    for i in range(2, polynomial_samples, step):
        l_me, l_mse, n_me, n_mse = single_test_eq(f, range_start, range_end, i, "equal", i in checkpoints, i)
        results[i // step] = np.array([l_me, l_mse, n_me, n_mse])

    for i in range(2, polynomial_samples, step):
        l_me, l_mse, n_me, n_mse = single_test_eq(f, range_start, range_end, i, "chebyshev", i in checkpoints, i)
        results[i // step + polynomial_samples // step] = np.array([l_me, l_mse, n_me, n_mse])

    dataframe = pd.DataFrame(results)
    dataframe.to_excel("test.xlsx", "equal")
