# Implementation of Insertion Sort

# Key points
# Time complexity - O(n2)


def InsertionSort(A):
    n = len(A)
    for i in range(1, n):
        # elements to left i are always in sorted order
        key = A[i]
        # second pointer responsible for putting key in proper place
        j = i - 1
        while j >= 0 and key < A[j]:
            # shift elements to right
            # until it's time to place key in sorted elements to left of i
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


A = [27, 26, 3, 5, 9, 9, 0, 0, 1, 11, 8, 4, 0, 19, 2, 0]
print(InsertionSort(A))