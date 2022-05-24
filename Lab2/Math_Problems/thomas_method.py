import numpy as np


def solve_thomas(a: np.array, d: np.array, d_type=np.float64) -> np.array:
    n = len(d)
    c_p = np.zeros((n,), dtype=d_type)
    d_p = np.zeros((n,), dtype=d_type)
    result = np.zeros((n,), dtype=d_type)
    c_p[0] = a[0][1] / a[0][0]
    d_p[0] = d[0] / a[0][0]
    for i in range(1, n):
        if i != n - 1:
            c_p[i] = a[i][i + 1] / (a[i][i] - a[i][i - 1] * c_p[i - 1])
        d_p[i] = (d[i] - a[i][i - 1] * d_p[i - 1]) / (a[i][i] - a[i][i - 1] * c_p[i - 1])
    result[n - 1] = d_p[n - 1]
    for i in range(n - 2, -1, -1):
        result[i] = d_p[i] - c_p[i] * result[i + 1]
    return result


def get_a(a, n, m):
    idx = n * 3
    idx += m-n
    return a[idx]


def solve_thomas_1d(a: np.array, d: np.array, d_type=np.float64) -> np.array:
    n = len(d)

    c_p = np.zeros((n,), dtype=d_type)
    d_p = np.zeros((n,), dtype=d_type)

    result = np.zeros((n,), dtype=d_type)

    c_p[0] = get_a(a, 0, 1) / get_a(a, 0, 0)
    d_p[0] = d[0] / get_a(a, 0, 0)
    for i in range(1, n):
        if i != n - 1:
            c_p[i] = get_a(a, i, i + 1) / (get_a(a, i, i) - get_a(a, i, i - 1) * c_p[i - 1])
        d_p[i] = (d[i] - get_a(a, i, i - 1) * d_p[i - 1]) / (get_a(a, 1, 1) - get_a(a, i, i - 1) * c_p[i - 1])
    result[n - 1] = d_p[n - 1]
    for i in range(n - 2, -1, -1):
        result[i] = d_p[i] - c_p[i] * result[i + 1]
    return result


if __name__ == "__main__":
    test_list = [
        [2, 3, 0, 0, 0],
        [1, 2, 3, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 0, 1, 2, 3],
        [0, 0, 0, 1, 2],
    ]
    test_list_1d = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]
    test_list_d = [1, 2, 3, 4, 5]
    print(np.linalg.solve(test_list, test_list_d))
    print(solve_thomas(np.array(test_list), np.array(test_list_d)))
    print(solve_thomas_1d(np.array(test_list_1d), np.array(test_list_d)))
