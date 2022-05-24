import math

import numpy as np
import pandas as pd

MAX_ITERATIONS = 100000


def solve_nonlinear_diff(equations_arr, jacobian_arr, initial_guess, epsilon=0.001):
    n = m = len(initial_guess)
    diff = math.inf
    x_0 = initial_guess
    jacobian_calced = np.zeros((n, m))
    f_x0 = np.zeros(n)
    iteration = 0
    while diff > epsilon:
        if iteration > 100 and diff > 2:
            return [100, 100, 100], "~"
        for i in range(n):
            f_x0[i] = -equations_arr[i](*x_0)
            for j in range(m):
                jacobian_calced[i][j] = jacobian_arr[i][j](*x_0)
        d_x0 = np.linalg.solve(jacobian_calced, f_x0)
        prev_x0 = x_0
        x_0 = x_0 + d_x0
        diff = 0
        for i in range(n):
            diff += abs(prev_x0[i] - x_0[i])
        iteration += 1
    return x_0, iteration


def solve_nonlinear_eps(equations_arr, jacobian_arr, initial_guess, eps=0.001):
    n = m = len(initial_guess)
    x_0 = initial_guess
    jacobian_calced = np.zeros((n, m))
    f_x0 = np.zeros(n)
    iteration = 0
    while abs(test_result(equations_arr, x_0)) > eps:
        iteration += 1
        if (iteration > 100 and abs(test_result(equations_arr, x_0)) > 2):
            return [100, 100, 100], "~"
        if iteration > MAX_ITERATIONS:
            break
        for i in range(n):
            f_x0[i] = -equations_arr[i](*x_0)
            for j in range(m):
                jacobian_calced[i][j] = jacobian_arr[i][j](*x_0)
        d_x0 = np.linalg.solve(jacobian_calced, f_x0)
        x_0 = x_0 + d_x0
    return x_0, iteration


def simple_test(equations_arr: list, jacobian_arr: list, initial_guess: list, iteration: int):
    # print(solve_nonlinear_diff(equations_arr, jacobian_arr, initial_guess, iteration))
    res, iterations = solve_nonlinear_eps(equations_arr, jacobian_arr, initial_guess, iteration)
    return test_result(equations_arr, res), res, iterations


def test_result(equations_arr, guess):
    n = len(guess)
    res = 0
    for i in range(n):
        res += abs(equations_arr[i](*guess))
    return res


def test_nonlinear(equations_arr: list, jacobian_arr: list, initial_guesses: list, iterations: list):
    guesses_str = initial_guesses.copy()
    result = []
    for i in range(len(guesses_str)):
        guesses_str[i] = str(guesses_str[i])
    guesses_str.insert(0, "n/x")
    result.append(guesses_str)
    for i in range(len(iterations)):
        result_line = [str(iterations[i])]
        for j in range(len(initial_guesses)):
            test_err, xs, iterations_num = simple_test(equations_arr, jacobian_arr, initial_guesses[j], iterations[i])
            if abs(test_err) > 2:
                result_line.append("~")
            else:
                # for i in range(len(xs)):
                #     xs[i] = round(xs[i], 2)
                # result_line.append(str(xs))
                # result_line.append(test_err)
                result_line.append(str(iterations_num))

        result.append(result_line)
    df = pd.DataFrame(result)
    df.to_csv("nonlinear_test.csv", index=False, header=False)
    print(df)


equations_arr = [lambda x1, x2, x3: x1 ** 2 + x2 ** 2 - x3 ** 2 - 1,
                 lambda x1, x2, x3: x1 - 2 * x2 ** 3 + 2 * x3 ** 2 + 1,
                 lambda x1, x2, x3: 2 * x1 ** 2 + x2 ** 2 - 2 * x3 ** 2 - 1]

jacobian_arr = [[lambda x1, x2, x3: 2 * x1, lambda x1, x2, x3: 2 * x2, lambda x1, x2, x3: -2 * x3],
                [lambda x1, x2, x3: 1, lambda x1, x2, x3: -6 * x2 ** 2, lambda x1, x2, x3: 4 * x3],
                [lambda x1, x2, x3: 4 * x1, lambda x1, x2, x3: 1, lambda x1, x2, x3: -4 * x3]]

#
# equations_arr = [lambda x1, x2: x1 + 2 * x2 - 2, lambda x1, x2: x1 ** 2 + 4 * x2 ** 2 - 4]
# jacobian_arr = [[lambda x1, x2: 1, lambda x1, x2: 2],
# [lambda x1, x2: 2 * x1, lambda x1, x2: 8 * x2]]
initial_guesses = [
    [2, 2, 2],
    [2, 2, -2],
    [2, -2, 2],
    [-2, 2, 2],
    [2, -2, -2],
    [-2, 2, -2],
    [-2, -2, 2],
    [-2, -2, -2],
]
n = 3
m = 3
# print(solve_nonlinear_eq(equations_arr, jacobian_arr, [-1, 1, -1], 100))
test_nonlinear(equations_arr, jacobian_arr, initial_guesses, [2, 1, 0.1, 0.01, 0.001, 0.0001, 1e-10, 1e-100])
#
