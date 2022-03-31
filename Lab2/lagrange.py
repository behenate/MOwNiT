# Class for an interpolator which uses Lagrange's method
class Lagrange:
    def __init__(self, points: list, values: list):
        self.points = points
        self.values = values

    def interpolate(self, x: float):
        points = self.points
        values = self.values
        n = len(points)
        interpolated = 0
        for i in range(n):
            numeral = values[i]
            nominator = 1
            for j in range(n):
                if i == j: continue
                numeral *= (x - points[j])
                nominator *= (points[i] - points[j])
            interpolated += numeral / nominator
        return interpolated
