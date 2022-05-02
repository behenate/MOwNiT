from Utils.derivative import calculate_derivative

def find_root_secant(f, x0, x1, epsilon=1e-10, max_iter=100):
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    i = 0
    while abs(x2 - x1) > epsilon and i < max_iter:
        x0 = x1
        x1 = x2
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        i += 1
    return x2


# Find function roots using Newton's method
# Limit the max number of iterations
def find_root_newton(f, x0, epsilon=1e-10, max_iter=100):
    for i in range(max_iter):
        x1 = x0 - f(x0) / calculate_derivative(f, x0)
        if abs(x1 - x0) < epsilon:
            break
        x0 = x1
    return x1

