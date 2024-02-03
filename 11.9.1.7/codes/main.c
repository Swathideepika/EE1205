#include <stdio.h>

int main() {
    FILE *file = fopen("values.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = 1; n <= 25; ++n) {
        int x_n = 4 * n + 1;
        fprintf(file, "%d\n", x_n);
    }

    fclose(file);
    return 0;
}
