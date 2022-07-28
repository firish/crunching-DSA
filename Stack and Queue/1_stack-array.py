# Implementing a stack, LIFO
# Common Applications -> Webpages/Browser History, Undo operation in any application like a text editor,
# Matching HTML tags and programming parenthesis, Evaluating Arithmetic expressions, Infix to Postfix conversion


# Stack, using an array
class Stack:
    def __init__(self):
        self._data = []
        print('Stack data structure initialized.')

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return True if len(self._data) == 0 else False

    def top(self):
        if self.isEmpty():
            print('Stack is empty.')
        else:
            return self._data[-1]

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.isEmpty():
            print('Stack is empty.')
        else:
            return self._data.pop()

    def display(self):
        if self.isEmpty():
            print('Stack is empty.')
            return
        space = len(str(max(self._data)))
        print("__" *space)
        for val in self._data:
            e_space = space - len(str(val))
            print("| " + " "*e_space + str(val) + " |")
        print("__" *space)


import random
s = Stack()
print('Top of stack ::: ' + str(s.top()))
for i in range(1, 11):
    s.push(i * random.randrange(1, 100, 5))
print('Length of stack ::: ' + str(len(s)))
print('Top of stack ::: ' + str(s.top()))
for _ in range(5):
    print('Stack popped ::: ' + str(s.pop()))
print('Length of stack ::: ' + str(len(s)))
print('Top of stack ::: ' + str(s.top()))
s.display()
