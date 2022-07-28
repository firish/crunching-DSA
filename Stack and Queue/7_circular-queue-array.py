# Design Circular Queue, it is also called "Ring Buffer"

# Design your implementation of the circular queue. The circular queue is a linear data structure in which the
# operations are performed based on FIFO (First In First Out) principle and the last position is connected back to
# the first position to make a circle. One of the benefits of the circular queue is
# that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the queue. But using the circular queue,
# we can use the space to store new values.


class MyCircularQueue:

    def __init__(self, k: int):
        self._limit = k
        self._data = [-1] * k
        self._size = 0
        self._front = self._rear = None

    def enQueue(self, value: int) -> bool:
        if self._size >= self._limit:
            return False
        elif self._size == 0:
            self._data[0] = value
            self._front = self._rear = 0
        else:
            self._rear += 1
            if self._rear == self._limit:
                self._rear = 0
            self._data[self._rear] = value
        self._size += 1
        return True

    def deQueue(self) -> bool:
        if self._size == 0: return False
        if self._front == self._limit:
            self._front = 0
        else:
            self._data[self._front] = -1
            self._front += 1
        self._size -= 1
        return True

    def Front(self) -> int:
        if self._size == 0:
            return -1
        else:
            return self._data[self._front]

    def Rear(self) -> int:
        if self._size == 0:
            return -1
        else:
            return self._data[self._rear]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._limit
