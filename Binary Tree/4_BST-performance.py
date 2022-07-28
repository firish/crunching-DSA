# Highlights of BST structure

# for bst with n nodes and height h
# For a tree with height h, max number of nodes, N = 2^(h+1) -1

# space = O(n)
# searching = O(h)
# Insertion = O(h)
# Deletion = O(h)

# Searching in worse case takes O(h) for leaf node or unsuccessful search
# insertion and deletion need to perform a search first, so time complexity is O(h) for all three operations

# one big problem with bst
# depending on value chosen for root node
# same set of elements can lead to bst with varying height
# the problem will be worse for a right/left skewed bst, which effects time complexity, here O(h) = O(n)

# Average case = O(logN)

