from typing import Type

import numpy as np
import pandas as pd

from Utils.drawing import *
from Utils.generators import *
from Tests.errors import *
from Approximation.polynomial_approximation import PolynomialApproximation


def single_test(f, range_start: float, range_end: float, nodes: int, degree: int,
                checkpoint: bool = False):
    ys, xs = samples_from_function("equal", f, nodes, range_start, range_end)
    test_ys, test_xs = samples_from_function("equal", f, 1000, range_start, range_end)

    # Create interpolators based on generated nodess
    hermite = PolynomialApproximation(degree, xs, ys)

    hermite_max_error = test_max_error(hermite, test_xs, test_ys)
    hermite_mse = test_mse(hermite, test_xs, test_ys)

    print(f"Approximation test: nodes: {nodes}, degree:{degree}")

    # Draw the interpolated function, show the legend and the graph
    if checkpoint:
        draw_funct(f, range_start, range_end)

        plt.title(f"Approximation test: nodes: {nodes}, degree:{degree}")
        plt.scatter(xs, ys, marker="o", s=27)

        draw(hermite, range_start, range_end, "approximation", samples=1000)
        plt.tight_layout()
        plt.legend(loc="upper right")
        plt.show()
    return hermite_max_error, hermite_mse


def approximation_tests(f, range_start: float, range_end: float, nodes_xlsx: list,
                        nodes_display: list, degrees_display: list):
    for i, node_cnt in enumerate(nodes_display):
        for j, degree in enumerate(degrees_display):
            if degree <= node_cnt//2:
                single_test(f, range_start, range_end, node_cnt, degree, checkpoint=True)
    results = []

    for i, node_cnt in enumerate(nodes_xlsx):
        degrees_xlsx = [i for i in range(3, node_cnt//2 + 1)] #[2 + (i*node_cnt//5) for i in range(5)]
        for j, degree in enumerate(degrees_xlsx):
            if degree <= node_cnt//2:
                h_me, h_mse = single_test(f, range_start, range_end, node_cnt, degree, False)
                results.append([node_cnt, degree, h_me, h_mse])

    dataframe = pd.DataFrame(results)
    dataframe.columns = ["Ilość węzłów", "Stopień", "Błąd Maksymalny", "Błąd Kwadratowy"]
    dataframe.to_excel("Results_Raports_Handouts/Approximation_Tests/tests.xlsx", "approximation test")



