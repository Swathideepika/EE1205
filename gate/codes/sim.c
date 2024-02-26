#include <stdio.h>
#include <complex.h>
#include <math.h>

#define N 64 // Length of the sequence
#define N_VALUES 9 // Number of values of n from 0 to 8

// Function to compute the IDFT
void idft(const double complex *X, double complex *x) {
    for (int n = 0; n < N; n++) {
        x[n] = 0;
        for (int k = 0; k < N; k++) {
            x[n] += X[k] * cexp(2 * M_PI * I * k * n / N);
        }
        x[n] /= N;
    }
}

// Function to perform convolution
void convolution(const double complex *x, const double complex *h, double complex *y) {
    for (int n = 0; n < N; n++) {
        y[n] = 0;
        for (int k = 0; k <= n; k++) {
            y[n] += x[k] * h[n - k];
        }
    }
}

int main() {
    double complex X[N]; // Frequency domain representation of X(e^{j\omega})
    double complex H[N]; // Frequency domain representation of H(e^{j\omega})
    double complex x[N]; // Time domain representation of x(n)
    double complex h[N]; // Time domain representation of h(n)
    double complex y[N]; // Result sequence y(n)

    // Define X(e^{j\omega})
    for (int k = 0; k < N; k++) {
        double omega = 2 * M_PI * k / N;
        X[k] = 1 - cexp(-I * omega) + 2 * cexp(-3 * I * omega);
    }

    // Define H(e^{j\omega})
    for (int k = 0; k < N; k++) {
        double omega = 2 * M_PI * k / N;
        H[k] = 1 - 0.5 * cexp(-2 * I * omega);
    }

    // Compute IDFT of X(e^{j\omega}) and H(e^{j\omega})
    idft(X, x);
    idft(H, h);

    // Perform convolution
    convolution(x, h, y);

    // Write real part of result to file
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    for (int n = 0; n < N_VALUES; n++) {
        fprintf(file, "%f\n", creal(y[n]));
    }
    fclose(file);

    return 0;
}

