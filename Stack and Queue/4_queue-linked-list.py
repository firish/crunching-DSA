
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self): return self._size

    def isEmpty(self): return self._size == 0

    def enqueue(self, el):
        newest = _Node(el, None)
        if self.isEmpty(): self._front = self._rear = newest
        else:
            self._rear._next = newest
            self._rear = newest
        self._size += 1

    def dequeue(self):
        if self.isEmpty(): print("Queue is empty.")
        else:
            el = self._front._element
            self._front = self._front._next
            self._size -= 1
            return el

    def first(self):
        if self.isEmpty(): print("Queue is empty.")
        else: return self._front._element

    def display(self):
        space = 0
        pos = self._front
        while pos:
            space += int(len(str(pos._element))) + 4
            pos = pos._next
        space -= 3
        print(" " + "_" * space + "_ ")
        print("| ", end="")
        pos = self._front
        index = 0
        while pos:
            if index != self._size-1:
                print(pos._element, end=" <--")
            else:
                print(pos._element, end=" ")
            index += 1
            pos = pos._next
        print("|")
        print(" " + "_" * space + "_ ")


import random
q = Queue()
print('Top of Queue ::: ' + str(q.first()))
for i in range(1, 13):
    q.enqueue(i * random.randrange(1, 100, 5))
print('Length of Queue ::: ' + str(len(q)))
print('Top of Queue ::: ' + str(q.first()))
for _ in range(5):
    print('Queue dequeued ::: ' + str(q.dequeue()))
print('Length of Queue ::: ' + str(len(q)))
print('Top of Queue ::: ' + str(q.first()))
q.display()
