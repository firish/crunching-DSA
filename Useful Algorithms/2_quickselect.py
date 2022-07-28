# Quick Select Algorithm
# Quickselect is a textbook algorthm typically used to solve the problems "find kth something":
# kth smallest, kth largest, kth most frequent, kth less frequent, etc. Like quicksort,
# quickselect was developed by Tony Hoare, and also known as Hoare's selection algorithm.

# It has O(n) average time complexity and is widely used in practice. Its worth noting that its
# worst-case time complexity is O(n2), although the probability of this worst-case is negligible.
from collections import defaultdict
import random as rand


def partition(count, unique, left, right, pivot_index):
    # get pivot frequency
    pivot_freq = count[unique[pivot_index]]
    # make pivot last element of array
    unique[right], unique[pivot_index] = unique[pivot_index], unique[right]
    i = store_index = left
    # scan all elements and put less frequent elements to the left
    while i < right:
        if count[unique[i]] < pivot_freq:
            unique[i], unique[store_index] = unique[store_index], unique[i]
            store_index += 1
        i += 1
    # insert pivot element into its right place
    unique[right], unique[store_index] = unique[store_index], unique[right]
    return store_index


def QuickSelect(count, unique, left, right, k):
    # get a random pivot index
    pivot_index = rand.randint(left, right)
    # sort the pivot_index acc to freq
    pivot_index = partition(count, unique, left, right, pivot_index)
    # check if you have the elements you require
    required = len(unique) - k
    if pivot_index == required:
        return
    # else, recursively call quick select and sort another element
    elif required < pivot_index:
        # Go left
        QuickSelect(count, unique, left, pivot_index - 1, k)
    else:
        # Go right
        QuickSelect(count, unique, pivot_index + 1, right, k)


Arr = [1, 1, 1, 1, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5]
k = 2
# get frequency of all elements
count = defaultdict(int)
for val in Arr: count[val] += 1
# get all unique elements
unique = list(count.keys())
print("Frequency of elements in input array ::: " + str(count))
QuickSelect(count, unique, 0, len(unique) - 1, k)
required = len(unique) - k
print(str(k) + " most frequent elements are ::: " + str(unique[required:]))
