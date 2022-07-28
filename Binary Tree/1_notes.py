# Implementing a binary tree data structure

# Trees
# A Tree can be empty (like stack), allows us to define a tree recursively
# Total nodes in a tree = N, total Edges = N-1

# Level of a tree, starts at root, (level 1) (level is number of nodes in path)
# Height of a tree, starts at root, (height 0) (height is number of edges in path)
# Therefore, Height = Level - 1

# Degree of a node is number of children it has
# Degree of a tree is max(degree of all its node)


# Binary Trees
# Properties
# every node has atmost two children (Degree 2), left and right
# left node precedes the right node (if degree of parent is 1)
# For a tree with height h, max number of nodes, N = 2^(h+1) -1


# Types of BT
# Proper / strict binary tree
# every node must have 0 or 2 children

# FUll binary tree
# every internal node has exactly 2 children and all leaf nodes are at same level
# No of nodes in FBT is always max = 2^(h+1) -1
# A FBT is always a CBT and PBT

# complete binary tree
# nodes at every level can be numbered from left to right without a gap
# A CBT will be a FBT upto height-1


# BT Representation
# Array representation
# For a BT with N nodes, have an array with N+1 size, (keeping 0 index empty)
# for any element at index i, its left and right child are at indexes i*2 and i*2 +1
# use same formula in reverse to get parents, for node at index i, its parent is floor(i/2)

# Linked representation
# create a node, with three members, left, element, and right


# Traversal of BT
# Pre-order traversal
# (Visit Root Node -> left node (recursively) -> right node (recursively)
# (used for searching a key in a BST)

# In-order traversal
# (left node (recursively) -> Root Node -> right node (recursively)
# For a BST, inorder traversal gives a sorted array (IMP)

# Post-order traversal
# (left node (recursively) -> right node (recursively) -> Root Node
# Useful for deleting a tree or a subtree of a tree
# Also useful for getting Postfix equation (BOD-MAS equation for calculator)

# level-order traversal
# visit nodes level by level (Top to Bottom, Left to Right)
# Non-recursive BFS search of a tree, also used in Cheny's Algo (tracing Garbage collection)



