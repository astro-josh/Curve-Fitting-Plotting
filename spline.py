# Joshua Alexander
# Sources:
# https://stackoverflow.com/questions/43458414/python-scipy-how-to-get-cubic-spline-equations-from-cubicspline

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate

def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    plt.plot(x, y)
    plt.show()

# returns log of number
def log(x):
    return math.log1p(x)

x = np.array([20,300,341,658,1100,2000, 2300, 8750, 71000])
y = np.array([ 1000, 185, 378, 300, 190, 312, 240, 193, 65])
#x = np.array(map(log, x))

arr = np.arange(np.amin(x), np.amax(x), 0.01)
# calc cubic spline of x, y
s = interpolate.CubicSpline(x, y)

# print coefficients
ch = 'a'
index = 1
for i in s.c:
    for j in i:
        print('{}{}: {}'.format(ch, index, j))
        index+=1
    ch = chr(ord(ch) + 1)
    index = 1

# setup plot
fig, ax = plt.subplots(1, 1)
ax.set_yscale('linear')
ax.set_xscale('linear')
ax.plot(x, y, 'bo', label='Data Point')
ax.plot(arr, s(arr), 'k-', label='Cubic Spline', lw=1)

# setup plot
for i in range(x.shape[0] - 1):
    segment_x = np.linspace(x[i], x[i + 1], 100)
    # A (4, 100) array, where the rows contain (x-x[i])**3, (x-x[i])**2 etc.
    exp_x = (segment_x - x[i])[None, :] ** np.arange(4)[::-1, None]
    # Sum over the rows of exp_x weighted by coefficients in the ith column of s.c
    segment_y = s.c[:, i].dot(exp_x)
    ax.plot(segment_x, segment_y, label='Segment {}'.format(i), ls='--', lw=3)

ax.legend()
plt.title('Bird Body Weight vs. Pulse Rate')
plt.xlabel("Body Weight (g)")
plt.ylabel("Pulse Rate (bpm)")
plt.show()
