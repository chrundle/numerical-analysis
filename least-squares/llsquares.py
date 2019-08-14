import numpy as np
import pylab
import matplotlib.pyplot as plt

def gen_data(x, y, data_size):
    # Generate data set {(x_1, y_1), ..., (x_20, y_20)}
    for k in range(1, data_size + 1):
        # Initialize x_k = k/2
        x.append(k/2)

        # Initialize eps_k as a random number uniformly distributed in [-2, 2]
        epsilon = np.random.uniform(-2, 2)
    
        # Set y_k = 5x_k + 2 + eps_k
        y.append(5*k/2 + 2 + epsilon)
    

def lls_and_data_plot(x, y, a_0, a_1):
    # Initialize arrays for best fit line
    t = []
    s = []

    # Determine maximum value in x and y
    x_inf = np.linalg.norm(x, np.inf)
    y_inf = np.linalg.norm(y, np.inf)

    # Generate points for plot of best fit line
    for k in np.arange(0, 20, .1):
        t.append(k)
        l = a_0 + a_1 * k
        s.append(l)

    # Generate plot of data points and best fit line
    plt.plot(t, s, "b-", lw=2)
    plt.plot(x, y, 'ro', markersize=7, lw=3)

    # Set and label axes and set title
    plt.axis([0, x_inf + 0.5, 0, y_inf + 1])
    plt.title('Plot of data set and best fit line y = %lg m + %lg using '
              'determined using linear least squares' %(a_1, a_0))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def lls(x, y, dim):
    # Initialize entries for matrix, A, and vector, b, for Least Squares System
    a_12 = 0
    a_22 = 0
    b_11 = 0
    b_21 = 0

    # Update values for A and b
    for k in range(dim):
        a_12 += x[k]
        a_22 += x[k] * x[k]
        b_11 += y[k]
        b_21 += x[k] * y[k]
    
    # Initialize matrix A and vector b for least squares system Az = b
    A = np.matrix( [[dim, a_12], [a_12, a_22]])
    b = np.matrix([[b_11],[b_21]])
    
    # Solve the linear least squares system Az = b
    z = np.linalg.solve(A,b)

    return z[0,0], z[1,0]


def avg_lls(data_size, n):
    # Initialize arrays for storing y-interecepts and slopes 
    intcpts = []
    slopes = []

    # Initialize arrays for data points
    x = []
    y = []

    # Generate data sets and run lin_least_squares n times
    for i in range(n):
        # Generate data set {(x_1, y_1), ..., (x_20, y_20)}
        gen_data(x, y, data_size)

        # Determine y-intercept and slope using Least linear Squares
        a_0, a_1 = lls(x, y, data_size)

        # Store y-intercept and slope in arrays
        intcpts.append(np.abs(a_0))
        slopes.append(np.abs(a_1))
    
    # Print the average error of the y-intercepts and slopes
    print('Data size: %d\n' %data_size)
    print('\nAverage error of y-intercept on %d tests: %10.8lg\nAverage '
          'error of slope on %d tests: %10.8lg\n' 
          %(n, np.mean(intcpts), n, np.mean(slopes)))

    #print('Variance of y-int: %10.8lg\nVariance of slope: %10.8lg\n'
    #      %(np.var(intcpts), np.var(slopes)))


def main():
    # ---- First run the program with the specified 20 data points ---- #
    # Initialize number of data points, m
    m = 20

    # Initialize arrays for data points
    x = []
    y = []

    # Generate m data points and store in arrays x and y
    gen_data(x, y, m)

    # Run linear least squares solver
    a_0, a_1 = lls(x, y, m)

    # Print the y-intercept and slope determined using lls
    print("\ny-int: %10.8lg\nslope: %10.8lg\n" %(a_0, a_1))

    # Plot the best fit line and the data points
    lls_and_data_plot(x, y, a_0, a_1)

    # ---- Now run the program with more data points ---- #
    # Initialize number of data points, m
    m = 20

    # Generate m data points and store in arrays x and y
    gen_data(x, y, m)

    # Run linear least squares solver
    a_0, a_1 = lls(x, y, m)

    # Print the y-intercept and slope determined using lls
    print("\ny-int: %10.8lg\nslope: %10.8lg\n" %(a_0, a_1))

    # Plot the best fit line and the data points
    lls_and_data_plot(x, y, a_0, a_1)

    # ---- Now determine the averages with more data points ---- #
#    avg_lls(20, 1000)
#    avg_lls(200, 1000)
#    avg_lls(2000, 1000)
#    avg_lls(20000, 100)

# Run main program
main()
