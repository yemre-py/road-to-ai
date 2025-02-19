#include <stdio.h>
#include "vector.h"

int main() {
    float vector[] = {1, 0};
    float vector2[] = {1, 1};
    printf("%.2f", angle(vector, vector2, 2));
}