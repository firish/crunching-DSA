# How to work with a heap
# Using Python 3 in-built module heapify

# Python heapq module creates a min heap
# https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python, for max-heap

import heapq as heap
# l1 = []
# heap.heappush(l1, 25)
# heap.heappush(l1, 15)
# heap.heappush(l1, 35)
# heap.heappush(l1, 5)
# heap.heappush(l1, 10)
# print(l1)
# print(heap.heappop(l1))
# print(l1)
# e = heap.heappushpop(l1, 12) # add and then remove
# print(e)
# print(l1)
# e = heap.heapreplace(l1, 4) # remove and then add
# print(e)
# print(l1)

import random as rand
l2 = [rand.randint(1,100) for x in range(10)]
print(l2)
heap.heapify(l2)
print(l2)
print(l2.pop())

# print(heap.nsmallest(3, l2))
# print(heap.nlargest(3, l2))