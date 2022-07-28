# Implementing selection sort

# Key points
# Time Complexity - O(n2) (n2 comparisons, n swaps)
# This is the only algorithm with only O(n-1) swaps
# This is an unstable algorithm (relative order of similar elements is not preserved)
# The con with selection sort is that its best and worst complexity are both O(n2)
# so for a completely sorted array, the algo will still take O(n2)


def SelectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        # pos keep tracks of index with minimum value
        pos = i
        for j in range(i, n):
            if arr[j] < arr[pos]: pos = j
        if i != pos:
            # swap arr[i] with the minimum element
            arr[i], arr[pos] = arr[pos], arr[i]
    return arr


A = [3, 5, 9, 9, 0, 0, 1, 11, 8, 4, 0, 19, 2, 0]
print(SelectionSort(A))
