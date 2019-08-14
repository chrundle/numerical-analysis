import numpy as np

def f(x):
  return np.cos(2*x + 0.5)

def F(x):
  return 0.5 * np.sin(2*x + 0.5)

# Routine for approximating integral using Composite Trapezoid Rule
def comp_trap(a, b, n):
  # Initialize h (mesh size)
  h = (b - a)/n
  
  # Initialize output value
  y = f(a) + f(b)
  
  # Initialize index
  i = 1

  # Compute summation in Composite Trapezoid Rule
  while (i < n):
    # Update input value
    temp = a + i * h
    
    # Compute function value
    y += 2 * f(temp)
    
    # Increase index
    i += 1
    
  # Multiply total by h/2  
  y *= h/2
  
  # Return computed approximation of integral
  return y

# Routine for approximating integral using Composite Simpon's Rule
def comp_simp(a, b, n):
  # Check if n is an odd number
  if ((n % 2) == 1):
    print("The mesh size for Composite Simpson's Rule must be an even number.")
    return 0

  # Initialize h (mesh size)
  h = (b - a)/n
  
  # Initialize output value
  y = 0
  
  # Initialize index
  i = 0

  # Compute summation in Composite Simpson's Rule
  while (i < n/2):
    # Compute evaluation points for current summand
    x_0 = a + 2 * i * h
    x_1 = a + (2 * i + 1) * h
    x_2 = a + (2 * i + 2) * h
    
    # Update approximate integral value
    y += f(x_0) + 4 * f(x_1) + f(x_2)
    
    # Update index
    i += 1

  # Multiply total by h/3    
  y *= h/3
  
  # Return computed approximation of integral
  return y

# Routine for approximating integral using Gaussian Quadrature with 5 nodes
# on the interval [-1, 1]
def gaus_quad():
    # Initialize output value
    y = 0
    
    # Initialize weights
    w = [0.5688888888888889, 0.4786286704993665, 0.4786286704993665, 
         0.2369268850561891, 0.2369268850561891]

    # Initialize abscissae
    x = [0.0000000000000000, -0.5384693101056831, 0.5384693101056831, 
         -0.9061798459386640, 0.9061798459386640]
  
    for i in range(5):
        y += w[i] * f(x[i])

    return y
  
def main():
  # Initialize interval, [a, b], over which to integrate
  a = -1.
  b = 1.
  
  # Initialize number of steps for Trapezoid Rule, Simpson's Rule, and Gaussian Quadrature
  n_trap = 517
  n_simp = 24
  n_gaus = 5
  
  exact_val = F(b) - F(a) #0.797983565
  # Print exact value of integral
  print("\n--------------------------------- Exact Value ---------------------"
        "------------")
  print(" Exact value of integral of cos(2x + .5) from -1 to 1:", exact_val, 
        "\n")
  
  # Compute error for Composite Trapezoid Rule
  trap_val = comp_trap(a, b, n_trap)
  trap_error = np.abs(trap_val - exact_val)
  print("----------------------------- Composite Trapezoid -----------------"
        "------------")
  print(" Computed value with n =", n_trap, "steps:", trap_val)
  print(" Computed error with n =", n_trap, "steps:", trap_error, "\n")
  
  # Compute error for Composite Simpson's Rule
  simp_val = comp_simp(a, b, n_simp)
  simp_error = np.abs(simp_val - exact_val)
  print("----------------------------- Composite Simpson's -----------------"
        "------------")
  print(" Computed value with n =", n_simp, "steps:", simp_val)
  print(" Computed error with n =", n_simp, "steps:", simp_error, "\n")
  
  # Compute error for Gaussian Quadrature Rule
  gaus_val = gaus_quad()
  gaus_error = np.abs(gaus_val - exact_val)
  print("----------------------------- Gaussian Quadrature -----------------"
        "------------")
  print(" Gaussian Quadrature value with n =", n_gaus, "steps:", gaus_val)
  print(" Gaussian Quadrature value with n =", n_gaus, "steps:", gaus_error,
        "\n")

# Run main program
main()
