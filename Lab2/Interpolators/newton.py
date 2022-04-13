# Class that can generate interpolated function based on given points using Newtons method

class Newton:
    def __init__(self, points: list = [], values: list = []):
        self.__points = []
        self.__values = []
        self.__differential_quotient = []
        for i in range(len(points)):
            self.add_node(points[i], values[i])

    # Adds a new x and f(x) value to the interpolator
    def add_node(self, point: float, value: float):
        n = len(self.__points)
        self.__points.append(point)
        self.__values.append(value)
        self.__differential_quotient.append([0] * (n + 1))
        self.__differential_quotient[n][0] = value
        self.calculate_row(n)

    # Calculates given differential_quotient row
    def calculate_row(self, row:int):
        for i in range(row):
            dq = self.__differential_quotient
            dq[row][i + 1] = (dq[row][i] - dq[row - 1][i]) / (self.__points[row] - self.__points[row - i - 1])

    # Performs Newtons interpolation based on information from differential_quotient array
    def interpolate(self, x:float):
        n = len(self.__points)
        dq = self.__differential_quotient
        interpolated = self.__values[0]
        multi_arr = [1] * n
        for i in range(1, n):
            multi_arr[i] = multi_arr[i - 1] * (x - self.__points[i - 1])
            interpolated += dq[i][i] * multi_arr[i]
        return interpolated
