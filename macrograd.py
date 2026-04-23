import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 3*x + 5

# f(3)
# print(f(3))

# xs = np.arange(-10, 10, 0.1)
# print(xs)
# ys = f(xs)
# print(ys)
# plt.plot(xs, ys)
# plt.show()

### derivative formula applied to f(x) = x^2 - 3x + 5
h = 0.0000001
x = 3
print(f(x))
print(f(x + h))
print((f(x + h) - f(x))) ### function responded in positive direction, so the slope is positive
print((f(x + h) - f(x)) / h)
