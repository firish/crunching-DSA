# Implementing a stack, LIFO
# Common Applications -> Webpages/Browser History, Undo operation in any application like a text editor,
# Matching HTML tags and programming parenthesis, Evaluating Arithmetic expressions, Infix to Postfix conversion


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self): return self._size

    def push(self, el):
        newest = _Node(el, None)
        if self._size == 0:
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self._size == 0: print('Stack is empty.')
        else:
            el = self._top._element
            self._top = self._top._next
            self._size -= 1
            return el

    def top(self): return self._top._element if self._size != 0 else None

    def display(self):
        if self._size == 0: print('Stack is empty.')
        else:
            space = float('-inf')
            pos = self._top
            while pos:
                space = max(space, len(str(pos._element)))
                pos = pos._next
            print("__" * space)
            pos = self._top
            while pos:
                e_space = space - len(str(pos._element))
                print("| " + " " * e_space + str(pos._element) + " |")
                pos = pos._next
            print("__" * space)


import random
s = Stack()
print('Top of stack ::: ' + str(s.top()))
for i in range(1, 6):
    s.push(i * random.randrange(50, 100, 2))
print('Length of stack ::: ' + str(len(s)))
print('Top of stack ::: ' + str(s.top()))
for _ in range(2):
    print('Stack popped ::: ' + str(s.pop()))
print('Length of stack ::: ' + str(len(s)))
print('Top of stack ::: ' + str(s.top()))
s.display()
