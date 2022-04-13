def calculate_derivative(f, x: float):
    h = 1e-5
    return (f(x + h) - f(x - h)) / (2 * h)
