# Implementing Shell Sort


# Key points
# Named after the person who invented the algo
# Time Complexity = O(n * logn)
# An updated version of insertion sort
# one distinction is that, left side is not sorted at all times like in insertion sort

def ShellSort(A):
    # start with a gap of n/2
    n = len(A)
    gap = n // 2
    while gap != 0:
        # Traverse from gap to the last element
        for i in range(gap, n):
            key = A[i]
            # use a second pointer j, which checks elements to left of i
            # just like insertion sort, it makes sure key is inserted in correct position
            # amongst the elements to the left side
            j = i - gap
            while j >= 0 and A[j] > key:
                # shifting elements to right
                A[j + gap] = A[j]
                j -= gap
            # j + gap is the correct position from key
            A[j + gap] = key
        gap = gap // 2
    return A


A = [3, 5, 9, 9, 0, 0, 1, 11, 8, 4, 0, 19, 2, 0]
print(ShellSort(A))

