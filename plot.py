import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    plt.plot(x, y)
    plt.show()

def my_formula(x):
    return x*x

def f(x):
    x_points = [20,300,341,658,1100,2000, 2300, 8750, 71000]
    y_points = [ 1000, 185, 378, 300, 190, 312, 240, 193, 65]

    tck = interpolate.splrep(x_points, y_points)
    return interpolate.splev(x, tck)
print f(1.25)

my_data = np.array(# copy your data below this line (over the existing data).
[[  20,  1000],
[  300,  185],
[  341,  378],
[  658,  300],
[  1100,  190],
[  2000, 312],
[  2300,  240],
[  8750,  193],
[  71000, 65]]
 #copied data appears above this line
 )# end of data array creation


split_my_data = np.hsplit(my_data, 2) #create a vector of independent variables
									# and a vector of independent variables.

# Uncomment the following two lines to
# double check that the data set was correctly split:

# print split_my_data[0]
# print split_my_data[1]

# compute the max and min values of the independent and dependent data points
# to determine the window for the plot.
ind_min = np.amin(split_my_data[0])
ind_max = np.amax(split_my_data[0])

dep_min = np.amin(split_my_data[1])
dep_max = np.amax(split_my_data[1])

# plot the data
plt.figure(1)
plt.plot(split_my_data[0],split_my_data[1], 'ro')

#plt.axis([ind_min-2, ind_max + 2, dep_min-2, dep_max+2])
plt.axis([2, 72000, 0, 400])
plt.ylabel('heart rate (bpm)')
plt.xlabel('body weight (g)')
plt.xticks(range(100))
#plt.xticks(range(min(split_my_data[1]), max(split_my_data[1])+1))
#plt.show()
# plot the estimated constant of porportionality line
graph(my_formula, range(0, 25))
plt.show(block=True)
