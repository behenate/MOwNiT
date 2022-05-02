from typing import Type

import numpy as np
import pandas as pd

from Spline_Interpolation.boundary_conditions import BoundaryConditions
from Spline_Interpolation.cubic_spline import CubicSplineInterpolator
from Spline_Interpolation.quadratic_spline import QuadraticSplineInterpolator
from Utils.drawing import *
from Utils.generators import *
from Tests.errors import *


def single_test_quadratic(f, interpolator_class: Type[QuadraticSplineInterpolator] | Type[CubicSplineInterpolator],
                          boundary_condition: BoundaryConditions,
                          range_start: float, range_end: float, train_samples_num: int,
                          checkpoint: bool = False):
    ys, xs = samples_from_function("equal", f, train_samples_num, range_start, range_end)
    test_ys, test_xs = samples_from_function("equal", f, 1000, range_start, range_end)
    # Create interpolators based on generated nodess
    interpolator = interpolator_class(xs, ys, boundary_condition)

    max_error = test_max_error(interpolator, test_xs, test_ys)
    mse = test_mse(interpolator, test_xs, test_ys)
    print(max_error, mse)
    # print(f"Quadratic intertpolation test nodes:{train_samples_num}")

    # Draw the interpolated function, show the legend and the graph
    if checkpoint:
        draw_funct(f, range_start, range_end)

        plt.title("{}, nodes count: {}".format(str(interpolator), train_samples_num))
        plt.scatter(xs, ys, marker="o", s=27)

        draw(interpolator, range_start, range_end, "Spline interpolation", samples=1000)
        plt.tight_layout()
        plt.legend(loc="upper right")
        plt.show()
    return max_error, mse


# Function that recieves two sets of interpolators and boundary conditions and then prints them
def compare_spline_test(f, interpolator_class: Type[QuadraticSplineInterpolator] | Type[CubicSplineInterpolator],
                        boundary_condition: BoundaryConditions,
                        interpolator_class2: Type[QuadraticSplineInterpolator] | Type[CubicSplineInterpolator],
                        boundary_condition2: BoundaryConditions,
                        range_start: float, range_end: float, checkpoints: list = [], step: int = 5,
                        max_degree: int = 200):
    polynomial_samples = max_degree
    results1 = np.empty(((polynomial_samples // step), 3))
    results2 = np.empty(((polynomial_samples // step), 3))
    for value in checkpoints:
        single_test_quadratic(f, interpolator_class, boundary_condition, range_start, range_end,
                              train_samples_num=value, checkpoint=True)
    for value in checkpoints:
        single_test_quadratic(f, interpolator_class2, boundary_condition2, range_start, range_end,
                              train_samples_num=value, checkpoint=True)


    for i in range(max(3,step), polynomial_samples, step):
        print("Step: ", i)
        t_me, t_mse = single_test_quadratic(f, interpolator_class, boundary_condition, range_start, range_end,
                                            train_samples_num=i)
        print(t_me, t_mse)
        results1[i // step] = np.array([i, t_me, t_mse])

    for i in range(max(3,step), polynomial_samples, step):
        t_me, t_mse = single_test_quadratic(f, interpolator_class2, boundary_condition2, range_start, range_end,
                                            train_samples_num=i)
        results2[i // step] = np.array([i, t_me, t_mse])

    dataframe = pd.DataFrame(results1)
    dataframe2 = pd.DataFrame(results2)
    iter1_instance = interpolator_class([0,1,2,3,4], [0,1,2,3,4], boundary_condition)
    iter2_instance = interpolator_class2([0,1,2,3,4], [0,1,2,3,4], boundary_condition2)
    dataframe.columns = ["Stopień", "Błąd Maksymalny", "Błąd Kwadratowy"]
    dataframe2.columns = ["Stopień", "Błąd Maksymalny", "Błąd Kwadratowy"]
    filename = str(iter1_instance) + " vs " + str(iter2_instance)

    with pd.ExcelWriter("Results_Raports_Handouts/Spline_Tests/{}.xlsx".format(filename), engine="openpyxl", mode="w+") as writer:
        dataframe.to_excel(writer, index=False, sheet_name=str(iter1_instance))
        dataframe2.to_excel(writer, index=False, sheet_name=str(iter2_instance))

