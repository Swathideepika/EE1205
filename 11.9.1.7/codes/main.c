#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    file = fopen("values.txt", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Generating values of x(n) and writing to file for n from 1 to 10
    for (int n = 1; n <= 10; n++) {
        int xn = 2 * n;  // Replace this with your function
        fprintf(file, "%d\n", xn);
    }

    fclose(file);
    return 0;
}

