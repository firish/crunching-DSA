# Instead of only storing the next value after we've peeked at it,
# we can store it immediately in the constructor and then again in the next(...) method.
# This greatly simplifies the code,
# because we no longer need conditionals to check whether we are currently storing a peeked at value

# give an iterator to the peeking iterator
# it will iterate over the iterator with an added function that allows you to peak the next value


class PeekingIterator:
    def __init__(self, iterator):
        self._next = iterator.next()
        self._iterator = iterator

    def peek(self):
        return self._next

    def next(self):
        if self._next is None:
            raise StopIteration()
        to_return = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return to_return

    def hasNext(self):
        return self._next is not None