# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache.
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


# Define a node class for a doubly-linked list (DLL)
class _Node:
    __slots__ = '_prev', '_val', '_key', '_next'

    def __init__(self, val, key, prev, nxt):
        self._val = val
        self._key = key
        self._prev = prev
        self._next = nxt


class LRUCache:
    # LRU Cache is implemented as a doubly linked list (DLL)
    # Addition of nodes takes place only at the end  of the DLL
    # Deletion of nodes takes place only at the head of the DLL     (least frequently used)
    # Once any element is accessed, move it to end of DLL           (most recently used)

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._head = None
        self._tail = None
        self._size = 0
        self._hashmap = {}

    def add_node(self, node):
        if self._size == 0:
            self._head = node
            self._tail = node
        else:
            node._prev = self._tail
            self._tail._next = node
            self._tail = self._tail._next

    def remove_node(self):
        del self._hashmap[self._head._key]
        self._head = self._head._next
        if self._head: self._head._prev = None
        self._size -= 1

    def update_cache(self, node):
        # if there is a single node, return
        if self._size == 1: return
        # if node is already most recently accessed node
        elif node == self._tail: return
        # if node is least recently used node
        elif node == self._head:
            self._head = self._head._next
            self._head._prev = None
        else:
            if node._next: node._next._prev = node._prev
            if node._prev: node._prev._next = node._next
        node._next = None
        node._prev = None
        self.add_node(node)

    def display(self):
        p = self._head
        while p:
            if p._next:
                print(str(p._key) + ":" + str(p._val), end=' --> ')
            else:
                print(str(p._key) + ":" + str(p._val), end=' \n')
            p = p._next

    def get(self, key: int) -> int:
        if key in self._hashmap:
            print("Get operation, key::: " + str(key) + " found")
            self.display()
            node = self._hashmap[key]
            self.update_cache(node)
            return node._val
        else:
            print("Get operation, key::: " + str(key) + " not found")
            self.display()
            return -1

    def put(self, key: int, value: int) -> None:
        print("Put operation, key and val ::: " + str(key) + " " + str(value))
        if key in self._hashmap:
            self._hashmap[key]._val = value
            self.update_cache(self._hashmap[key])
        else:
            newest = _Node(value, key, None, None)
            if self._size < self._capacity:
                self.add_node(newest)
            else:
                self.remove_node()
                self.add_node(newest)
            self._hashmap[key] = newest
            self._size += 1
        self.display()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Working Example
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

# Step by Step Output
# Put operation, key and val ::: 1 1
# 1:1
# Put operation, key and val ::: 2 2
# 1:1 --> 2:2
# Get operation, key::: 1 found
# 1:1 --> 2:2
# Put operation, key and val ::: 3 3
# 1:1 --> 3:3
# Get operation, key::: 2 not found
# 1:1 --> 3:3
# Put operation, key and val ::: 4 4
# 3:3 --> 4:4
# Get operation, key::: 1 not found
# 3:3 --> 4:4
# Get operation, key::: 3 found
# 3:3 --> 4:4
# Get operation, key::: 4 found
# 4:4 --> 3:3


# Example 2
# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
# Step by Step output
# Put operation, key and val ::: 2 1
# 2:1
# Put operation, key and val ::: 1 1
# 2:1 --> 1:1
# Put operation, key and val ::: 2 3
# 1:1 --> 2:3
# Put operation, key and val ::: 4 1
# 2:3 --> 4:1
# Get operation, key::: 1 not found
# 2:3 --> 4:1
# Get operation, key::: 2 found
# 2:3 --> 4:1



