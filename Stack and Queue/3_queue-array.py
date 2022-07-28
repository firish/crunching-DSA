# Implementing a Queue, FIFO
# common functions are enqueue and dequeue
# Common Applications -> first come first serve applications, used in printers, access to shared resources and memory
# servers use queue to process requests received, many traditional computer applications.


class Queue:
    def __init__(self):
        self._data = []

    def __len__(self): return len(self._data)

    def isEmpty(self): return len(self._data) == 0

    def enqueue(self, el): self._data.append(el)

    def dequeue(self):
        if self.isEmpty(): print("Queue is empty.")
        else: return self._data.pop(0)

    def first(self):
        if self.isEmpty(): print("Queue is empty.")
        else: return self._data[0]

    def display(self):
        space = 0
        for val in self._data: space += int(len(str(val)))+1
        print(" " + "_" * space + "_ ")
        print("| ", end="")
        for val in self._data: print(val, end=" ")
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
