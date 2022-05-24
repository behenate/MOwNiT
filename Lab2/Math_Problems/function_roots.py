from Utils.derivative import calculate_derivative

def find_root_secant(f, x0, x1, epsilon=1e-10, max_iter=100):
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    i = 0
    while abs(x2 - x1) > epsilon and i < max_iter:
        x0 = x1
        x1 = x2
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        i += 1
    return x2, i

def find_root_secant_f(f, x0, x1, epsilon=1e-10, max_iter=100):
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    i = 0
    while abs(f(x1)) > epsilon and i < max_iter:
        x0 = x1
        x1 = x2
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        i += 1
    return x2, i

# Find function roots using Newton's method
# Limit the max number of iterations
def find_root_newton(f,df, x0, epsilon=1e-10, max_iter=100):
    iterations = 0
    for i in range(max_iter):
        if df(x0) == 0:
            break
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < epsilon:
            break
        x0 = x1
        iterations = i
    return x1, i


def find_root_newton_f(f,df, x0, epsilon=1e-10, max_iter=100):
    iterations = 0
    for i in range(max_iter):
        if df(x0) == 0:
            break
        x1 = x0 - f(x0) / df(x0)
        if abs(f(x1)) < epsilon:
            break
        x0 = x1
        iterations = i
    return x1, iterations
