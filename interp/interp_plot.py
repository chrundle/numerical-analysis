import pylab
from pylab import genfromtxt
import matplotlib.pyplot as plt

# Import data from Newton derived difference program
X = genfromtxt("Xvalues.txt")
Y = genfromtxt("Yvalues.txt")

# Determine points for plot of actual function
def f(x):
    return (1/(1 + x*x))

x_val = []
f_val = []

for i in range(5000):
    x_val.append(X[i])
    f_val.append(f(X[i]))

# ---- Plot intepolated polynomial and 1/(1 - x^2) ---- #
# plot for 1/(1 - x^2)
line1, = plt.plot(x_val, f_val, linestyle = "-", lw=3, label="1/(1 - x^2)")

# plot for interpolated polynomial
line2, = plt.plot(X[:], Y[:], 'r--', lw=3, label="Interpolating polynomial")

# set and label axes, set title, and legend
plt.axis([-5, 5, -0.5, 2.1])
plt.title('Plot of 1/(1 - x^2) and Newton divided difference interpolated '
          'polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(bbox_to_anchor=(.826, .05), loc=2, borderaxespad=-1.)
plt.grid(True)
plt.show()
