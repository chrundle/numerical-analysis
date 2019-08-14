#include <stdio.h>
#include <stdlib.h>
#include <cmath>


/* ----------------------- f ----------------------- */
/*  Given a double, y, this function returns the 
    value of 1/(1 + y^2). 
    
    Input variables:
        y  : double                                  */
double f (double y) {
    return (1/(1 + y*y));
}


/* ----------------------- nodes ----------------------- */
/*  Given a pointer to an array, the number of entries
    in that array, and an interval [low, hi], this 
    function generates evenly spaced values in the 
    interval [low, hi] and stores them in the given
    array. 
    
    Input variables:
        *node_arr: pointer to array in which to store nodes
        num_node : the number of nodes in the array
        low      : lower bound for interval
        hi       : upper bound for interval              */
void nodes (double *node_arr, int num_node, double low, double hi) {
    int i; 
    double delta;

    delta = (hi - low)/(num_node - 1);  // determine space between nodes

    /* compute and store nodes in node_arr */
    for(i = 0; i < num_node; i++) {
        node_arr[i] = i * delta + low;
    }
}


/* ----------------------- div_diff ----------------------- */
/*  Given a pointer to a pointer of arrays, a pointer to 
    an array of evenly spaced nodes, a routine for 
    evaluating a function f, and the number of nodes, this 
    function generates Newton divided differences for all
    the nodes. 
    
    Input variables:
        **F      : pointer to pointer of arrays of which 
                   the nth array should have at least 
                   n + 1 entries
        *node_arr: pointer to array in which to store nodes
        f(x)     : routine for evaluating and returning
                   function value of f at x
        num_node : the number of nodes in the array         */
void div_diff (double **F, double *node_arr, double f(double y), int num_node){
    int i, j;
    double temp;

    /* compute F[i][0] for i = 0, ..., num_node */
    for(i = 0; i < num_node; i++) {
        F[i][0] = f(node_arr[i]);
    }

    /* compute F[i][j] for 1 <= j <= i <= num_node */
    for(i = 1; i <= num_node; i++) {
        for(j = 1; j <= i; j++) {
          temp = (F[i][j-1] - F[i-1][j-1])/(node_arr[i] - node_arr[i - j]);
          F[i][j] = temp;
        }
    }
}


/* ----------------------- div_diff_data ----------------------- */
/*  This routine returns the same values as div_diff except
    instead of using a function to evaluate the points to
    determine the initial divided differences, this routine
    requires an array of data points.
    
    Input variables:
        **F      : pointer to pointer of arrays of which 
                   the nth array should have at least 
                   n + 1 entries
        *node_arr: pointer to array in which to store nodes
        *data    : pointer to array of data points correspong
                   to nodes in node_arr
        num_node : the number of nodes in the array              */
void div_diff_data (double **F, double *node_arr, 
                    double *data, int num_node){
    int i, j;
    double temp;

    /* compute F[i][0] for i = 0, ..., num_node */
    for(i = 0; i < num_node; i++) {
        F[i][0] = data[i];
    }

    /* compute F[i][j] for 1 <= j <= i <= num_node */
    for(i = 1; i <= num_node; i++) {
        for(j = 1; j <= i; j++) {
          F[i][j] = (F[i][j-1] - F[i-1][j-1])/(node_arr[i] - node_arr[i-j]);
        }
    }
}


/* ----------------------- test_routine ----------------------- */
/*  This routine tests that all of the above defined functions
    compute the correct values by computing Newton divided
    differences for Example 1 in Section 3.3 of "Numerical
    Analysis" by Burden and Faires. This routine is strictly
    for the purposes of verifying the routines are generating
    the correct values.                                         */
void test_routine () {
    int i, n;
    double fval;

    n = 5;

    /* allocate memory for interpolation nodes */
    double *x = new double[n];

    /* generate test nodes */
    nodes (x, n, 1, 2.2);

    /* generate data points */
    double z[5] = {0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623};

    /* allocate memory for Newton divided differences */
    double ** F = new double*[n + 1];
    for(i = 0; i <= n; i++) {
        F[i] = new double[i + 1];
    }

    /* generate Newton divided differences for data with nodes from x */
    div_diff_data(F, x, z, n);

    /* print problem details */
    printf("===== Test problem (Ex. 1 in Sec. 3.3 of Num. Analysis) =====\n");

    /* print nodes */
    for(i = 0; i < n; i++) {
        printf("x[%i] = %lg\n", i, x[i]);
    }

    /* print Newton divided differences */
    for(i = 0; i < n; i++) {
        printf("F[%i][%i] = %lg\n", i, i, F[i][i]);
    }

    printf("==================== END of Test Problem ====================\n");

    /* deallocate memory used for nodes and Newton divided differences */
    for(i = 0; i < n; i++) {
        delete[] F[i];
    }
    delete[] F;
    delete[] x;
}


/* ---------------------------- interp_f ---------------------------- */
/*  This routine computes the value of the interpolating
    polynomial generated using Newton divided differences.
    The value is computed through the use of the following
    recursion:
    
    p(y) = F[0][0] + sum_{i=1}^{n} F[i][i] (y - x_0)...(y - x_{i-1}).
    
    Input variables:
        **F      : pointer to pointer of arrays of which 
                   the nth array should have at least 
                   n + 1 entries
        *node_arr: pointer to array in which to store nodes
        num_node : the number of nodes in the array
        y        : double at which to evaluate interpolating 
                   polynomial                                         */
double interp_f (double **F, double *node_arr, int num_node, double y) {
    int i;
    double p_value, temp;

    p_value = F[0][0];  // set initial value of interp. poly.
    temp = 1;           // factor used for updating p_value in loop

    /* compute p_value using recursion */
    for(i = 1; i < num_node; i++) {
        temp *= (y - node_arr[i - 1]);
        p_value += temp * F[i][i];
    }

    return p_value;     // return computed value
}


/* ----------------------- div_diff_data ----------------------- */
/*  This routine computes data points of the interpolating 
    polynomial and stores them in text files so that they can
    be used to generate plots.
    
    Input variables:
        **F        : pointer to pointer of arrays of which 
                     the nth array should have at least 
                     n + 1 entries
        *node_arr  : pointer to array in which to store nodes
        num_node   : the number of nodes in the array
        num_samples: the number points to be sampled for data    */
void interp_data (double **F, double *node_arr, int num_node, int num_samples){
    int i;
    double delta, temp;
    FILE *pFile_x, *pFile_y;

    /* initialize pointers for data files */
    pFile_x = fopen("Xvalues.txt", "w");  // data file for x values
    pFile_y = fopen("Yvalues.txt", "w");  // data file for y values

    temp = node_arr[0];                   // initialize sample point

    /* determine equally spaced difference for sampling data points */
    delta = (node_arr[num_node - 1] - temp)/num_samples;

    /* compute data points and store them in x and y value files */
    for(i = 0; i < num_samples; i++) {
        fprintf(pFile_y, "%lg\n", interp_f(F, node_arr, num_node, temp));
        fprintf(pFile_x, "%lg\n", temp);
        temp += delta;
    }
}


/* --------------------------- main --------------------------- */
/*  Main routine which runs previous programs to determine 
    interpolating polynomial for f(y) = 1/(1 - y^2) and 
    evaluate at 0.4835 to compare to original function.         */
int main() {
    int i, n;
    double p, temp;

    //test_routine();

    n = 11; // set number of nodes

    /* allocate memory for interpolation nodes */
    double *x = new double[n];

    nodes (x, n, -5, 5);   // generate nodes for interval [-5, 5]

    /* allocate memory for Newton divided differences */
    double ** F = new double*[n + 1];
    for(i = 0; i <= n; i++) {
        F[i] = new double[i + 1];
    }

    /* generate Newton divided differences for f with nodes from x */
    div_diff (F, x, f, n);
    
    /* evaluate the interpolating polynomial constructed from Newton 
       divided differences at the point 0.4835 */
    p = interp_f(F, x, n, 0.4835);

    /* print fval and f(0.4835) */
    printf("p(0.4835) = %lg and f(0.4835) = %lg\n", p, f(0.4835));

    /* print absolute error |fval - f(0.4835) */
    printf("|p(0.4835) - f(0.4835)| = %lg\n", std::abs(p - f(0.4835)));

    /* generate data points for plot */
    interp_data(F, x, n, 5000);

    /* deallocate memory used for nodes and Newton divided differences */
    for(i = 0; i <= n; i++) {
        delete[] F[i];
    }
    delete[] F;
    delete[] x;

    return 0;
}
