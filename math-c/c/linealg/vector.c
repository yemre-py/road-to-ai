#include <stdio.h>
#include <math.h>

float length(float *vector, int size) {
    float _length = 0;
    for(int i = 0; i < size; i++) {
        _length += vector[i] * vector[i];
    }

    return sqrt(_length);
}

float dotProduct(float *vector1, float *vector2, int size) {
    float result = 0;
    for(int i = 0; i < size; i++) {
        result += vector1[i] * vector2[i];
    }

    return result;

    // if result is 0, the vectors are perpendicular
}

// cos? = (u • v) / (||u|| * ||v||)
float angle(float *vector1, float *vector2, int size) {
    float dot = dotProduct(vector1, vector2, size);
    float length1 = length(vector1, size);
    float length2 = length(vector2, size);

    if(length1 == 0 || length2 == 0) {
        return 0; // if one of the vectors is 0, the angle is 0
    }
    float cosine = dot / (length1 * length2);
    if(cosine > 1) { cosine = 1; }
    if(cosine < -1) { cosine = -1; }

    return acos(cosine)*(180/M_PI);
}
