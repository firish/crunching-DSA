# Quick Sort Algo
# Avg time - O(nlogn), n comparison * logn, logn as we take action on both sides at same time
# Worst time - O(n2), when array is already sorted, n comparisons * n, as we take action only on right side

def QuickSort(Arr, low, high):
    if low < high:
        p = Partition(Arr, low, high)
        QuickSort(Arr, low, p-1) # Left Side
        QuickSort(Arr, p+1, high)  # Right Side


def Partition(Arr, low, high):
    pivot = Arr[low]
    i, j = low+1, high
    while 1:
        while Arr[i] <= pivot and i <= j: i += 1
        while Arr[j] > pivot and i <= j: j -= 1
        if i <= j: Arr[i], Arr[j] = Arr[j], Arr[i]
        else: break
    Arr[low], Arr[j] = Arr[j], Arr[low]
    return j


A = [9, 18, 77, 2, 111, 23, 88, 77, 74, 1, 1, 19, 100, 1000, 40, 1]
QuickSort(A, 0, len(A)-1)
print(A)