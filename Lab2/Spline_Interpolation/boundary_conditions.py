from enum import Enum


class BoundaryConditions(Enum):
    # To fill top and bottom row of the array with zeros
    ZEROS = 1
    # Top and bottom row based on cubic function from last four points
    LAST4 = 2

    CLAMPED = 3

