# Modified by Joshua Alexander
# Sources:
# https://stackoverflow.com/questions/32121877/how-do-i-replicate-excels-power-trendline-in-python
# https://stackoverflow.com/questions/41109122/fitting-a-curve-to-a-power-law-distribution-with-curve-fit-does-not-work

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# array of bird body weights
x = np.array([20, 300, 341, 658, 1100, 2000, 2300, 8750, 71000])
# array of bird pulse rates
y = np.array([1000, 185, 378, 300, 190, 312, 240, 193, 65])

fig = plt.figure()
ax=plt.gca()

# create scatter plot of original data
ax.scatter(x,y,c="blue",alpha=0.95,edgecolors='none', label='Actual Data')
# set the x and y scales
ax.set_yscale('linear')
ax.set_xscale('linear')
newX = np.linspace(0, 72000, 10000)

# define power function to fit line to
def myComplexFunc(x, a, b, c):
    return a * np.power(x, (-1 * b)) + c

# use curve fit function to find our model
popt, pcov = curve_fit(myComplexFunc, x, y)

# plot the model
plt.plot(newX, myComplexFunc(newX, *popt), 'g-', label="({0:.3f}*x**{1:.3f}) + {2:.3f}".format(*popt))

# print the values of a, b, and c from the model
print "Modified Exponential Fit: y = (a*(x**b)) + c"
print "\ta = popt[0] = {0}\n\tb = popt[1]* -1 = {1}\n\tc = popt[2] = {2}".format(*popt)

# use curve fit to find our model, create a lambda function of to fit our line (this one doesnt have a c)
popt, pcov = curve_fit(lambda fx,a,b: a*fx**-b,  x,  y)

# print the values of a and b from the model
print "Power Regression Fit: y = (a*(x**b)) + c"
print "\ta = popt[0] = {0}\n\tb = popt[1] = {1}\n\t".format(*popt)
power_y = popt[0]*x**-popt[1]

# plot the model
plt.plot(x, power_y, label='Power Fit')

# setup our plot
ax.grid(b='True')
plt.title('Bird Body Weight vs. Pulse Rate')
plt.xlabel("Body Weight (g)")
plt.ylabel("Pulse Rate (bpm)")
plt.legend(loc='upper right')
plt.show()

#commented out seperate plot for second model
#popt, pcov = curve_fit(lambda fx,a,b: a*fx**-b,  x,  y)
#print "Power Regression: y = (a*(x**b)) + c"
#print "\ta = popt[0] = {0}\n\tb = popt[1] = {1}\n\t".format(*popt)
#power_y = popt[0]*x**-popt[1]

#plt.scatter(x, y, label='actual data')
#plt.plot(x, power_y, label='Power Fit')
#plt.legend()
#plt.show()
