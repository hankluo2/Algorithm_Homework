"""
@File Node.py
@author Hankluo2
@date 2020-8-8
@desc A node class for linked list type
"""

class Node:
    def __init__(self, data, next_node = None):
        self._items = None # reference to itself
        self.size = 0
        self.data = data
        self.next = next_node

    def add(self, data):
        """ Set default that the current node is head"""
        self._items = Node(data, self._items)
        self.size += 1
        
    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next