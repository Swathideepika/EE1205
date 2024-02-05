#include <stdio.h>

int main() {
    // Open a file for writing
    FILE *file = fopen("values.txt", "w");

    if (file == NULL) {
        printf("Error opening file!");
        return 1;
    }

    // Calculate and write values to the file
    for (int n = 0; n <= 25; n++) {
        int x_n = 4 * n + 1;
        fprintf(file, "x(%d) = %d\n", n, x_n);
    }

    // Close the file
    fclose(file);


    return 0;
}

