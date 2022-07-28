# Binary Search Tree is BT where all nodes in left subtree < root
# and all nodes in right subtree > root
# left and right search tree are also BST

# properties
# BST does not contain duplicates (imp)
# Inorder traversal of BST is a list sorted in increasing order
# searching for elements takes average O(logn) // or O(h) where h is height
# searching in worst case is O(n), for left/right skewed BST


class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinarySearchTree:

    def __init__(self):
        self._root = None

    # to diplay nodes
    def inorder(self, troot):
        if not troot:
            return
        else:
            self.inorder(troot._left)
            print(troot._element, end=' ')
            self.inorder(troot._right)

    # Insert values according to BST rules
    def insert(self, troot, el):
        temp = None
        while troot:
            temp = troot
            if el == troot._element:
                return
            elif el < troot._element:
                troot = troot._left
            else:
                troot = troot._right

        new = _Node(el)
        if self._root:
            if el > temp._element:
                temp._right = new
            else:
                temp._left = new
        else:
            self._root = new

    # recursive insert method
    def rinsert(self, troot, el):
        if troot:
            if el < troot._element:
                troot._left = self.rinsert(troot._left, el)
            elif el > troot._element:
                troot._right = self.rinsert(troot._right, el)
        else:
            new = _Node(el)
            troot = new
        return troot

    # Search values iteratively
    def search(self, troot, el):
        if not troot:
            return -1
        else:
            while troot:
                if el == troot._element:
                    return troot
                elif el < troot._element:
                    troot = troot._left
                else:
                    troot = troot._right
            return -1

    # Search values recursively
    def rsearch(self, troot, el):
        if not troot:
            return -1
        else:
            if troot._element == el:
                return troot
            elif troot._element < el:
                return self.rsearch(troot._left, el)
            else:
                return self.rsearch(troot._right, el)

    # Delete values according to BST rules
    def delete(self, el):
        p = self._root  # parent
        pp = None  # parent of parent
        if not p: return -1
        # find the element
        while p and p._element != el:
            pp = p
            if p._element > el: p = p._left
            else: p = p._right
        if not p: return -1

        # Case 1: if node has two subtrees
        if p._left and p._right:
            # find smallest el in right subtree or largest element in left subtree
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            # replace p (element to be deleted) with the largest el in left subtree
            p._element = s._element
            p = s
            pp = ps

        # Case 2: if node has one subtree
        # Also handles case when node is leaf node
        c = None
        if p._left: c = p._left
        else: c = p._right
        if p == self._root: self._root = None
        else:
            if p == pp._left: pp._left = c
            else: pp._right = c


# Driver Code
import random as rand

bst = BinarySearchTree()
bst2 = BinarySearchTree()
nodes = [rand.randint(0, 101) for _ in range(20)]

# for rinsert, you need to store the root for the first insert operation
bst2._root = bst2.rinsert(bst2._root, -1 * nodes[0])
for el in nodes:
    bst.insert(bst._root, el)
    bst2.rinsert(bst2._root, -1 * el)

bst.inorder(bst._root)
print('\n')
bst2.inorder(bst2._root)
print('\n')

el = bst._root
if el._left: el = el._left._element
else: el = el._right._element
el2 = rand.randint(0, 101)
el3 = rand.randint(0, 101)
print('Searching element ::: ' + str(el) + ' in BST, found ::: ' + str(bst.search(bst._root, el)))
print('Searching element ::: ' + str(el2) + ' in BST, found ::: ' + str(bst.search(bst._root, el2)))
print('Searching element ::: ' + str(el3) + ' in BST, found ::: ' + str(bst.rsearch(bst._root, el3)))

while True:
    del_el = bst._root
    if del_el._right: del_el = del_el._right._element
    else: del_el = del_el._left._element
    if bst.search(bst._root, del_el) != -1: break
print('\n')
print('BST before deleteion ::: ')
bst.inorder(bst._root)
print(" ")
print('Element to be deleted ::: ' + str(del_el))
bst.delete(del_el)
bst.inorder(bst._root)
