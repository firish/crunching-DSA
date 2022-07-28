# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache.
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


# We're asked to implement the structure which provides the following operations in O(1) time :
# Get the key / Check if the key exists
# Put the key
# Delete the first added key (LRU)

# The first two operations in O(1) time are provided by the standard hashmap, and the last one - by linked list.
# There is a structure called ordered dictionary, it combines behind both hashmap and linked list.
# In Python this structure is called OrderedDict.


from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
