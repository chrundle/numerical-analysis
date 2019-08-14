import math
import numpy
import pylab
import matplotlib.pyplot as plt

# define approximating polynomial p(x)
def p(x):
    return (2.23284 * x * x - 2.10538 * x + 2.61885);

t = []
s = []
r = []

# initialize points for plot
for i in numpy.arange(0.5, 2.5, .001):
    t.append(i)
    s.append(p(i))
    r.append(numpy.exp(i))

# plot vertical lines denoting the range of values for which
# p(x) approximates e^x
plt.axvline(1, color='k', linestyle=':', lw=2)
plt.axvline(2, color='k', linestyle=':', lw=2)

# plot e^x
line1, = plt.plot(t, r, lw=3, label="e^x")

# plot p(x) = 2.23284 * x * x - 2.10538 * x + 2.61885
line2, = plt.plot(t, s, "r--", lw=3, 
                  label="2.23284 x^2 − 2.10538 x + 2.61885")

# set and label axes, set title, and legend
plt.grid(False)
plt.title("Plot of f(x) = e^x and p(x) = 2.23284 x^2 − 2.10538 x + 2.61885 "
          "on the interval [0.5, 2.5]")
plt.axis([0.5, 2.5, 1, 13])
plt.xlabel('x')
plt.ylabel('y')
plt.legend(bbox_to_anchor=(.766, .05), loc=2, borderaxespad=-1.)
plt.show()
