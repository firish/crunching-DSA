# Implementing the classic bubble sort

# key points
# relative ordering of same elements is preserved, so bubble sort is a stable algorithm
# Time complexity = O(n2), comparisons = O(n2), Swaps = O(n2) (worst case)
# Best case complexity (sorted array) = O(n)


def BubbleSort(A):
    n = len(A)
    for i in range(n):
        # swaps var tracks swaps made in a pass
        swaps = 0

        # in each iteration, the largest element is placed in extreme right
        # last i elements are already sorted, so go only till n-i
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swaps += 1

        # if swaps are 0 for any pass, it means that the array is already sorted
        # This lets us break early
        if swaps == 0:
            break
    return A


A = [3, 5, 9, 9, 0, 0, 1, 11, 8, 4, 0, 19, 2, 0]
print(BubbleSort(A))

