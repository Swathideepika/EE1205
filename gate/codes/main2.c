#include <stdio.h>

#define LENGTH 10  // Choose appropriate length for your signal

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w");

    // Generate values for the given signal
    int n;
    for (n = 0; n < LENGTH; ++n) {
        double y = 0.0;
        if (n == 0)
            y += 1.0;
        if (n == 1)
            y -= 1.0;
        if (n == 2)
            y -= 0.5;
        if (n == 3)
            y += 2.5;
        if (n == 5)
            y -= 1.0;
        
        fprintf(fp, "%d %lf\n", n, y);
    }

    fclose(fp);
    return 0;
}

