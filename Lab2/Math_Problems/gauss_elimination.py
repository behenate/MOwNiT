import numpy as np


def solve_gauss(a: np.array, b: np.array, d_type=np.float64) -> np.array:
    n = len(a)
    x = np.zeros(n, dtype=d_type)
    # Applying Gauss Elimination
    for i in range(n):
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n):
                a[j][k] = a[j][k] - ratio * a[i][k]
            b[j] = b[j] - ratio * b[i]

    # Back Substitution
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = b[i]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]
    return x


if __name__ == "__main__":
    mat = [[5.00000000e+00, 1.00000000e+00, 0.00000000e+00, 3.00000000e+00, -1.00000000e+00],
           [0.00000000e+00, 3.00000000e+00, 4.00000000e+00, 1.00000000e+00, 7.00000000e+00],
           [0.00000000e+00, 0.00000000e+00, 4.50000000e+00, 0.00000000e+00, 6.00000000e+00],
           [0.00000000e+00, 4.44089210e-16, 0.00000000e+00, 3.52702703e+00, 2.95945946e+00],
           [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 2.11354647e+00]]
    known = [2., 7., 4.5, 2.91891892, 1.75758075]

    print(solve_gauss(mat, known))
