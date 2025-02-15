# 1. Algorithms

## 1.1 Sorting Algorithms

### 1.1.1 Bubble Sort

**Bubble Sort** is a simple sorting algorithm that repeatedly steps through the list, comparing current element with the next one, swapping their values if needed. These passes
through the list are repeated until the array is fully sorted.

> **Array:** `[5, 2, 9, 1, 3, 6]`
>
> **Step 1**
>
> - `[5, 2]` -> Swap -> `[2, 5]`
> - `[5, 9]` -> No swap
> - `[9, 1]` -> Swap -> `[1, 9]`
> - `[9, 3]` -> Swap -> `[3, 9]`
> - `[9, 6]` -> Swap -> `[6, 9]`
>
> > **The greatest elements (6,9) are at the end of the array**
>
> **Step 2**
>
> `[2, 5, 1, 3, 6, 9]` -> `[2, 1, 3, 5, 6, 9]`
>
> > **5 is at the last position**
>
> **Step 3**
>
> `[2, 1, 3, 5, 6, 9]` -> `[1, 2, 3, 5, 6, 9]`
>
> > **Swapped 2 and 1, completed the sorting**
