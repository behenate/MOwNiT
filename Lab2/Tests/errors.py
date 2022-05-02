# Tests the max deviation from the correct value
def test_max_error(interpolator, xs: list, ys: list):
    max_error = 0
    for i in range(len(ys)):
        max_error = max(max_error, abs(ys[i] - interpolator.interpolate(xs[i])))
    return max_error


# Tests the sum of squares od deviations from the correct value
def test_mse(interpolator, xs: list, ys: list):
    mse = 0
    for i in range(len(ys)):
        mse += (ys[i] - interpolator.interpolate(xs[i])) ** 2
    return mse