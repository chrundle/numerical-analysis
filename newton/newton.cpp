#include <stdio.h>
#include <math.h>
#include <cmath>
#include <iostream>

double f (double x) {
    return (std::cos(x) + std::sin(50 * x) * std::sin (50 * x));
}

double fprime (double x) {
    return (100 * std::sin (50 * x) * std::cos (50 * x) - std::sin(x));
}

double g (double f1 (double y), double f2 (double y), double x) {
    return (x - f1(x)/f2(x));
}

int main () {
    int i, Numstep;
    double x, xnew, TOL;

    Numstep = 25;
    TOL = 1e-6;
    x = 3;

    for (i = 0; i < Numstep; i++) {
        xnew = g(f, fprime, x);
        std::cout << x << std::endl;

        if (std::abs(x - xnew) < TOL) {
            std::cout << "Step = " << i << " and x = " << x << std::endl; 
            break;
        }

        x = xnew;
    }

    return 0;
}
