# Generate points with equal intervals
import math

# Generates points at given,equal intervals
def generate_intervals(n: int, a: float, b: float):
    xs = [0] * n
    dist = (b - a) / (n - 1)
    for i in range(n):
        xs[i] = a + dist * i
    return xs


# Generate points located on chebyshev nodes
def generate_chebyshev_nodes(n: int, a: float, b: float):
    nodes = [0] * n
    for k in range(1, n + 1):
        nodes[k - 1] = 0.5 * (a + b) + 0.5 * (b - a) * math.cos((2 * k - 1) / (2 * n) * math.pi)
    return nodes


# Generates sample values on either chebyshev nodes or equal distances
def samples_from_function(dists: str, func, n: int, a: float, b: float):
    if dists == "equal":
        xs = generate_intervals(n, a, b)
    else:
        xs = generate_chebyshev_nodes(n, a, b)
    ys = [func(xs[i]) for i in range(n)]
    return ys, xs

