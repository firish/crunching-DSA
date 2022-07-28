# Heap is a priority Queue
# Insertion is like a normal queue, FIFO, insert at end
# Deletion is not at front, but based on a priority is maintained by a key, assigned to each value in priority queue
# element with min key value (the highest priority) is deleted first

# Heap actually use Binary Trees in the back end, so they are also called Binary Heaps
# Some important properties of heaps are
# 1) Relational -> Key in a node of BT is greater/lesser or equal to key of its children (Minimum Heap/Maximum Heap)
# 2) Structural -> BT should be a complete BT

# for max-heap or min-heap, always the root node is deleted


class Heap:
    def __init__(self):
        self._maxsize = 10
        self._data = [-1]*self._maxsize
        self._csize = 0

    def __len__(self): return self._csize

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

    def nlargest(self, k):
        largest = []
        if self.is_empty():
            print("Stack is empty")
            return
        elif self._csize < k:
            print("Stack doesn't have " + str(k) + " elements yet")
        for _ in range(k):
            largest.append(self.delete())
            # if you don't want elements to be deleted, simple insert the element again
        return largest

    def nsmallest(self, k):
        smallest = []
        if self.is_empty():
            print("Stack is empty")
            return
        elif self._csize < k:
            print("Stack doesn't have " + str(k) + " elements yet")
        for _ in range(self._csize):
            smallest.append(self.delete())
            # if you don't want elements to be deleted, simple insert the element again
        return smallest[-k:][::-1]


import random as rand
h = Heap()
for _ in range(8): h.insert(rand.randint(1, 50))
print("Root (max element) ::: " + str(h.max()))
print(" Heap elements ::: " + str(h._data))
# print("Heap tree ::: " + str(h._data), end="\nDeleted Nodes : ")
# for _ in range(len(h)): print(str(h.delete()), end=" ")
# print("5 smallest elements are ::: " + str(h.nlargest(5)))
print("5 smallest elements are ::: " + str(h.nsmallest(3)))