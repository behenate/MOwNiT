import pandas as pd
import numpy as np
from Math_Problems.function_roots import *

MAX_ITERATIONS = 100001


def generate_csv_report(f,df, ro: float, mode: int, range_start: float, range_end: float, step_size: float = 0.1):
    current_x0 = range_start
    result = []
    while current_x0 <= range_end + step_size:
        root, iterations = find_root_newton(f,df, current_x0, ro, MAX_ITERATIONS)
        result.append([current_x0, iterations, root, f(root)])
        current_x0 += step_size
    df = pd.DataFrame(result, columns=["x0", "n", "x", "f(x)"])
    df.to_csv(f"{mode}_zeroes_report.csv", index=False, header=False)
    return df


def generate_csv_report_secant(f, ro: float, mode: int, range_start: float, range_end: float, step_size: float = 0.1):
    current_x0 = range_start + step_size
    result = []
    while current_x0 <= range_end + step_size:
        root, iterations = find_root_secant(f, range_start, current_x0, ro, MAX_ITERATIONS)
        result.append([range_start, current_x0, iterations, root, f(root)])
        current_x0 += step_size

    current_x0 = range_end - step_size
    while current_x0 >= range_start - step_size:
        root, iterations = find_root_secant(f, current_x0, range_end, ro, MAX_ITERATIONS)
        result.append([current_x0, range_end, iterations, root, f(root)])
        current_x0 -= step_size
    df = pd.DataFrame(result, columns=["a", "b", "n", "x", "f(x)"])
    df.to_csv(f"{mode}_zeroes_report.csv", index=False, header=False)
    return df
