# Creating a Binary Tree

class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinaryTree:

    def __init__(self):
        self._root = None

    def maketree(self, e, left, right):
        self._root = _Node(e, left._root, right._root)

    def inorder(self, troot):
        if not troot: return
        else:
            self.inorder(troot._left)
            print(troot._element, end=' ')
            self.inorder(troot._right)

    def preorder(self, troot):
        if not troot: return
        else:
            print(troot._element, end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self, troot):
        if not troot: return
        else:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=' ')

    def levelorder(self, troot):
        q = []
        q.append(troot)
        print(troot._element, end=' ')
        while len(q) > 0:
            troot = q.pop(0)
            if troot._left:
                print(troot._left._element, end=' ')
                q.append(troot._left)
            if troot._right:
                print(troot._right._element, end=' ')
                q.append(troot._right)

    def count(self, troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x + y + 1
        else: return 0

    def height(self, troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)
            return x + 1 if x > y else y + 1
        else: return 0


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()  # Null Node that is used to specify children of leaf nodes
x.maketree(40, a, a)
y.maketree(50, a, a)
z.maketree(60, a, a)
r.maketree(20, x, a)
s.maketree(30, y, z)
t.maketree(10, r, s)
# BT = 10
#     |   |
#    20   30
#   |    |  |
#  40   50  60

print("Inorder Traversal of Binary Tree ::: ", end=' ')
t.inorder(t._root)
print()
print("Preorder Traversal of Binary Tree ::: ", end=' ')
t.preorder(t._root)
print()
print("Postorder Traversal of Binary Tree ::: ", end=' ')
t.postorder(t._root)
print()
print("Levelorder Traversal of Binary Tree ::: ", end=' ')
t.levelorder(t._root)
print()

print("Total number of nodes in Binary Tree ::: ", end=' ')
print(t.count(t._root))
print("Total height of Binary Tree ::: ", end=' ')
print(t.height(t._root))
print()








