#include <stdio.h>

void bubble_sort(int *array, int size)
{
    if (size <= 1)
        return; // if there is only one element, it is already sorted

    int n = size;

    for (int i = 0; i < n - 1; i++) // if stay a element at the end of the array, it is sorted
    {
        int swapped = 0; // optimization
        int last_swapped = 0; // keep track of the last swapped element

        for (int j = 0; j < n - i - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                swapped = 1;
                last_swapped = j;
            }
        }
        if (swapped == 0)
            break; // if no swaps are made, the array is sorted

        n = last_swapped + 1;
    }
}

int main()
{
    int array[] = {5, 2, 9, 1, 3, 6};
    bubble_sort(array, 6);

    for (int i = 0; i < 6; i++)
    {
        printf("%d ", array[i]);
    }
    return 0;
}