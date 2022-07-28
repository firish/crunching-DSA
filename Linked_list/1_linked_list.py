# Creating the node of a linked list

# use _ before class and instance names for defining primitive data structs
# for instance values of data struct, use __slots__
# it is a built-in way for allocating memory efficiently
# use __init__ constructor for assigning values to instance of class


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def addNode(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            # if list is empty, first element is head
            self._head = newest
        else:
            # this statement links the current last element of linked list to new node
            self._tail._next = newest
        # make tail the last element of linked list
        self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        while p:
            if p._next:
                print(p._element, end=' --> ')
            else:
                print(p._element, end='\n')
            p = p._next

    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1

    def addFirst(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def addAtIndex(self, e, i):
        newest = _Node(e, None)
        p = self._head
        index = 0
        if i >= self._size:
            print("Index out of range")
            return
        elif i == self._size - 1:
            self.addNode(e)
            return
        else:
            while index != i:
                index += 1
                p = p._next
            newest._next = p._next
            p._next = newest
        self._size += 1

    def removeFirst(self):
        if self._size == 0:
            print("List is already empty")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        # if list becomes empty, adjust tail pointer
        if self._size == 0:
            self._tail = None
        return e


    def pop(self):
        # to delete the last node from linked list
        if self._size == 0:
            print('List is already empty')
            return
        p = self._head
        n = self._size - 2
        while n > 0:
            p = p._next
            n -= 1
        e = p._next._element
        p._next = None
        self._tail = p
        self._size -= 1
        # If list becomes empty
        if self._size == 0:
            print('List is now empty')
            self._tail = None
        return e

    def removeAtIndex(self, pos):
        if pos >= self._size:
            print("Position out of Linked List")
            return
        elif pos == self._size - 1:
            e = self.pop()
            return e
        elif pos == 0:
            e = self.removeFirst()
            return e
        p = self._head
        index = 0
        while index != pos-1:
            p = p._next
            index += 1
        # use secondary pointer temp
        temp = p._next
        e = temp._element
        p._next = temp._next
        self._size -= 1
        return e



A = [x for x in range(1, 11)]
L = LinkedList()
for val in A:
    L.addNode(val)

B = [x for x in range(-1, -5, -1)]
for val in B:
    L.addFirst(val)

L.addAtIndex(e=0, i=3)
L.addAtIndex(e=-99, i=0)
L.addAtIndex(e=-99, i=1)
L.addAtIndex(e=99, i=len(L)-1)
L.addAtIndex(e=100, i=len(L)-1)

# L.removeFirst()
L.pop()
L.removeAtIndex(3)
L.removeAtIndex(0)
L.removeAtIndex(len(L)-1)

print("Linked List size ::: " + str(len(L)))
print("Searching element " + str(6) + " in the Linked List ::: " + str(L.search(6)))
print("Linked List ::: ", end=" ")
L.display()


