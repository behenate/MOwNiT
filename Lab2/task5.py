import numpy as np
import matplotlib.pyplot as plt
from Math_Problems.function_roots import *
from Tests.Math_Problems.generate_zeroes_csv import generate_csv_report, generate_csv_report_secant
from Utils.drawing import draw_funct

range_start = 0.4
range_end = 2
f = lambda x: x ** 2 - 20 * (np.sin(x)) ** 10
derivative = lambda x: 2 * (x - 100 * np.sin(x) ** 10 * np.cos(x))

# df = generate_csv_report(f=f, df=derivative, ro=1e-100, mode=0, range_start=range_start, range_end=range_end)
df = generate_csv_report_secant(f, ro=1e-2, mode=0, range_start=range_start, range_end=range_end)
draw_funct(f, -2.5, 2.5, label="function")
draw_funct(f, range_start, range_end, label="function in the range")

print(df)
plt.scatter(df['x'], df['f(x)'], color='green', marker='o', s=20, zorder=100, label="zeroes")
plt.tight_layout()
plt.legend(loc="upper center")
plt.show()
