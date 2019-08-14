import numpy as np
import pylab
import matplotlib.pyplot as plt

# --------------------- Class for Taylor Method ---------------------- #
class TaylorMethod:
    # Routine to initialize elements in class
    def __init__(self, n, a, b, w_init):
        # Initialize endpoints of interval 
        self.a = a
        self.b = b
        # Initialize stepsize h and number of iterations
        self.iter = n
        self.h = 1/self.iter
        # Initialize array of n+1 evenly spaced timesteps on interval [a, b]
        self.t = np.linspace(self.a, self.b, self.iter+1)
        # Initialize array to store function values
        self.w = np.zeros(self.iter+1)
        # Initialize initial function value
        self.w[0] = w_init
        # Initialize array to store previous method values for comparison
        self.w_backup = np.zeros(self.iter+1)

    # ------------------- Function evaluation routines ------------------- #    
    def y(self,t):
        # Return t^2 (e^t - e)
        return (t*t*(np.exp(t) - np.exp(1)))

    def f(self, w, t):
        temp = np.exp(t)
        temp *= t**2
        temp += 2 * (w/t)
        # Return 2w/t + t^2 e^t
        return temp #(2*w/t + t*t*np.exp(t))

    def f_p(self, w, t):
        t2 = t*t
        et = np.exp(t)

        # Return w/t^2 + t^2 e^t/2 + 2 t e^t
        return (w/t2 + t2*et/2 + 2*t*et)

    def f_pp(self, w, t):
        temp = t*t/6 + t + 1

        # Return (t^2/6 + t + 1)e^t
        return (temp * np.exp(t))

    # Routine to reset all function values in w to 0
    def reset_w(self):
        self.w = np.zeros(self.iter+1)

    # Routine to back up all function values from one method
    def backup_w(self):
        self.w_backup = np.copy(self.w)

    # Routine to determine function value at timestep i
    def update_w(self, i, order):
        # w_i = w_{i-1} + h * (2w_{i-1}/t_{i-1} + t_{i1}^2 e^t_{i-1})
        self.w[i] += self.w[i-1] + self.h * self.f(self.w[i-1], self.t[i-1])

        # Check if order > 1
        if (order > 1):
            # temp = h^2
            temp = self.h * self.h
            # Now w_i = h * (2w_{i-1}/t_{i-1} + t_{i1}^2 e^t_{i-1}) +
            # (w_{i-1}/t_{i-1}^2 + t_{i-1}^2 e^t_{i-1}/2 + 2 t e^t_{i-1}) h^2
            self.w[i] += temp * self.f_p(self.w[i-1], self.t[i-1])

            # Check if order > 2
            if (order > 2):
                # temp = h^3
                temp *= self.h
            # Now w_i = h * (2w_{i-1}/t_{i-1} + t_{i1}^2 e^t_{i-1}) +
            # (w_{i-1}/t_{i-1}^2 + t_{i-1}^2 e^t_{i-1}/2 + 2 t e^t_{i-1}) h^2
            # + h^3 (t_{i-1}^2/6 + t{i-1} + 1) e^t{i-1}
                self.w[i] += temp * self.f_pp(self.w[i-1], self.t[i-1])


    # Routine to perform order 1 Taylor Method (Euler's method)
    def eulers_method(self):
        # Perform Euler's method (order 1 update)
        for i in range(self.iter):
            self.update_w(i+1, 1)

    # Routine to perform order 2 Taylor Method
    def taylors_method_2(self):
        # Perform Euler's method (order 1 update)
        for i in range(self.iter):
            self.update_w(i+1, 2)

    # Routine to perform order 3 Taylor Method
    def taylors_method_3(self):
        # Perform Euler's method (order 1 update)
        for i in range(self.iter):
            self.update_w(i+1, 3)

    def data_plot(self, title, file_name):
        # Initialize arrays for best fit line
        x_val = []
        y_val = []
        x_plt = []
        y_plt = []

        # Generate points to compute infinity norm
        for i in np.linspace(1, 2, self.iter+1):
            x_val.append(i)
            y_val.append(self.y(i))

        # Generate points for plot of best fit line
        for i in np.arange(0.9, 2.2, .01):
            x_plt.append(i)
            y_plt.append(self.y(i))

        # Compute || y - w ||_{inf}
        print('|| Y - w ||_{inf} = ', 
              np.linalg.norm(np.subtract(y_val,self.w),np.inf))

        # Generate plot of data points and best fit line
        plt.plot(x_plt, y_plt, "b-", lw=2)
        plt.plot(self.t, self.w, 'ro', lw=3)
        #plt.plot(self.t, self.w_backup, 'go', lw=3)

        # Set and label axes and set title
        plt.axis([0.98, 2.02, -0.15, 20])
        plt.title(title)
        plt.xlabel('t')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()

        # Save plot as png file
        file_name.__add__('.png')
        plt.savefig(file_name)


def euler():
    # Initialize TaylorMethod Class of order 1
    T = TaylorMethod(1566, 1, 2, 0)

    # Perform Euler's method
    T.eulers_method()

    # Plot approximations and exact function
    T.data_plot('Plot of y = t^2 (e^t - e) and approximations generated '
                'using Euler\'s method', 'Euler')
            
def taylor():
    # Initialize TaylorMethod Class of order 1
    T = TaylorMethod(5, 1, 2, 0)

    # Perform 3rd order Taylor's method
    T.taylors_method_3()

    # Plot approximations and exact function
    T.data_plot('Plot of y = t^2 (e^t - e) and approximations generated '
                'using third order Taylor\'s method', 'Taylor3rd')

def main():
    # Run Euler's method
    euler()

    # Run Taylor's method
    taylor()

# Run main function
main()
