class Heap:
    def __init__(self):
        self._maxsize = 100
        self._data = [-1]*self._maxsize
        self._csize = 0

    def is_empty(self): return self._csize == 0

    def insert(self, el):
        if self._csize == self._maxsize:
            print("Heap is full.")
            return
        self._csize += 1
        hi = self._csize
        # Insert element at end of tree for preserving structural property
        self._data[hi] = el
        # Perform up-heap bubbling to maintain relational property
        while hi > 1 and el > self._data[hi//2]:
            self._data[hi] = self._data[hi//2]
            hi //= 2
        self._data[hi] = el

    def max(self):
        if self.is_empty():
            print("Heap is empty")
            return
        else: return self._data[1]

    def delete(self):
        if self.is_empty():
            print("Heap is empty")
            return
        # remove node as element to be deleted
        # replace node with last element of tree to preserve structural property
        el = self._data[1]
        self._data[1] = self._data[self._csize]
        self._data[self._csize] = -1
        self._csize -= 1
        # perform down-heap bubbling to maintain relational property
        i, j = 1, 2
        while j <= self._csize:
            # chose the child node with greater value to be next root node
            if self._data[j] < self._data[j+1]: j += 1
            if self._data[j] > self._data[i]:
                self._data[j], self._data[i] = self._data[i], self._data[j]
                i = j     # chose left side of right side for next node
                j = i*2   # j is one level below i (node i's children)
            else: break
        return el

def HeapSort(A):
    k = len(A)-1
    heap = Heap()
    for val in A: heap.insert(val)
    while k >= 0:
        A[k] = heap.delete()
        k -= 1
    return A


import random as rand
A = []
for _ in range(10): A.append(rand.randint(0, 100))
print("Unsorted Array ::: " + str(A))
print("Sorted Array is ::: " + str(HeapSort(A)))