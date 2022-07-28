# implement a doubly linked list

class _Node:
    __slots__ = "_val", "_next", "_prev"

    def __init__(self, val, next, prev):
        self._val = val
        self._next = next
        self._prev = prev


class DoublyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def addNode(self, val, pos=-1):
        newest = _Node(val, None, None)
        # if pos is greater than number of elements
        if pos > self._size:
            return None
        # if list is empty
        if self._size == 0:
            self._head = newest
            self._tail = newest
        # add at head of list
        elif pos == 0:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
        # add at tail of list
        elif pos == self._size or pos == -1:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        # add at any specific position
        else:
            p, index = self._head, 0
            while index < pos-1:
                index += 1
                p = p._next
            newest._next = p._next
            p._next._prev = newest
            newest._prev = p
            p._next = newest
        self._size += 1

    def removeNode(self, pos=-1):
        # if list is empty
        if self._size == 0:
            return None
        # if pos is out of index
        elif pos > self._size:
            return None
        # if there is only one node in list
        elif self._size == 1:
            el = self._head._val
            self._head, self._tail = None, None
        # if you have to remove at head
        elif pos == 0:
            el = self._head._val
            self._head._next._prev = None
            self._head = self._head._next
        # if you have to remove at tail
        elif pos == -1 or pos == self._size-1:
            el = self._tail._val
            self._tail._prev._next = None
            self._tail = self._tail._prev
        # if you have to remove at any specific instance
        else:
            p, index = self._head, 0
            while index < pos:
                index += 1
                p = p._next
            el = p._val
            p._prev._next = p._next
            p._next._prev = p._prev
        self._size -= 1
        return el

    def display(self):
        pos, index = self._head, 0
        while index < self._size:
            if index != self._size - 1:
                print(pos._val, end=" <--> ")
            else:
                print(pos._val, end="\n")
            index += 1
            pos = pos._next
        return


D = DoublyLinkedList()
P = [x for x in range(1, 8)]
N = [x for x in range(-1, -7, -1)]
for val in P:
    D.addNode(val) # add at tail
for val in N:
    D.addNode(val, pos=0) # add at head
D.addNode(0, 6) # add at fixed instance
D.removeNode() # acts as D.pop()
D.removeNode(len(D)-1) # remove at tail
D.removeNode(6) # remove at fixed instance
D.removeNode(0) # remove at head
D.display()
