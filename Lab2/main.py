import math
from tests import big_test
import matplotlib.pyplot as plt
from derivative import calculate_derivative

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Dróżdż Wojciech f3, k=1, m=3, [-2pi+1, pi+1]  = −k * x *sin(m(x −1))
    k = 1
    m = 3
    range_start = -2 * math.pi + 1
    range_end = math.pi + 1

    # Create the function
    f = lambda x: -k * x * math.sin(m * (x - 1))

    # Will run tests and display plots of the results at 3rd 5th 10th and 20th degree polynomial for both
    # equal and chebyschev nodes
    big_test(f, range_start, range_end, checkpoints=[3, 5, 10, 20], step=1, max_degree=21)

    # Commented code, uncomment and modify to quickly test interpolations

    # from generators import *
    # from drawing import *
    #
    # f = lambda x: x ** 8 + 1
    # # ys, xs = samples_from_function("equal", f, 5, range_start, range_end)
    # test_ys, test_xs = samples_from_function("equal", f, 1000, -10, 10)
    #
    # interpolator = Lagrange([-1, 0, 1], [[2, -8, 56], [1, 0, 0], [2, 8, 56]])
    #
    # draw_funct(f, -10, 10)
    # draw(interpolator, -10, 10, "Lagrange")
    print(calculate_derivative(f, 4))
    plt.show()
