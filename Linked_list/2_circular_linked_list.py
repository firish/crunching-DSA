# Creating the node of a linked list

class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class CircularLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def addNode(self, val, pos=-1):
        newest = _Node(val,None)
        # check if there is no element in Linked List
        if pos > self._size:
            return False
        if self._size == 0:
            newest._next = newest
            self._head = newest
            self._tail = newest
        # if we have to add at tail
        elif pos == -1:
            newest._next = self._tail._next
            self._tail._next = newest
            self._tail = newest
        # if we have to add at head
        elif pos == 0:
            newest._next = self._head
            self._tail._next = newest
            self._head = newest
        # if we have to add at a specific index
        else:
            p, index = self._head, 0
            while index < pos-1:
                p = p._next
                index += 1
            newest._next = p._next
            p._next = newest
        self._size += 1

    def removeNode(self, pos=-1):
        if pos > self._size:
            return False
        # check if list is empty
        elif self._size == 0:
            return False
        # if there is only one node in list
        elif self._size == 1:
            el = self._head._element
            self._head = None
            self._tail = None
        # if you want to remove at head
        elif pos == 0:
            el = self._head._element
            self._tail._next = self._head._next
            self._head = self._head._next
        # if you want to remove at tail
        elif pos == self._size-1:
            p, index = self._head, 0
            while index < self._size-2:
                index += 1
                p = p._next
            el = self._tail._element
            p._next = self._head
            self._tail = p
        # if you want to remove at a particular index value
        else:
            p, index = self._head, 0
            while index < pos - 1:
                index += 1
                p = p._next
            el = p._next._element
            p._next = p._next._next
        self._size -= 1
        return el

    def display(self):
        # this part is used to display the circular links above the elements
        s, index, pos = "", 0, self._head
        es = ""
        while index < self._size-1:
            num = pos._element
            dig = 0
            if index == 0 and num < 0:
                es = " "
            if num < 0:
                num = abs(num)
                dig += 1
            while num >= 1:
                num = num / 10
                dig += 1
            s += " <-- " + str(" ")*dig
            index += 1
            pos = pos._next
        print(es + "|" + s + "|")
        # this part is used to display the nodes in the Circular Linked List
        pos, index = self._head, 0
        while index < self._size:
            if index != self._size-1:
                print(pos._element, end=" --> ")
            else:
                print(es + str(pos._element), end="\n")
            index += 1
            pos = pos._next
        return


C = CircularLinkedList()
L = [x for x in range(1, 14)]
N = [x for x in range(-1, -7, -1)]
for val in L:
    C.addNode(val)
for val in N:
    C.addNode(val, pos=0)
C.addNode(0, 6)
C.removeNode(0)
for _ in range(3):
    C.removeNode(len(C) - 1)
C.removeNode(5)
C.display()


