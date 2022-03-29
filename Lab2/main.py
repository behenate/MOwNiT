import math
from tests import big_test

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Dróżdż Wojciech f3, k=1, m=3, [-2pi+1, pi+1]  = −k * x *sin(m(x −1))
    k = 1
    m = 3
    range_start = -2 * math.pi + 1
    range_end = math.pi + 1

    # Create the function
    f = lambda x: -k * x * math.sin(m * (x - 1))
    big_test(f, range_start, range_end, checkpoints=[2, 3, 5, 8, 13, 20, 30, 40, 65, 70, 100], step=5)

    # Perform the tests
