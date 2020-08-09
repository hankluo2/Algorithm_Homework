"""
@File Node.py
@author Hankluo2
@date 2020-8-8
@desc A node class for linked list type
"""

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


# method on Node
class LinkedBag:
    def __init__(self, dataList = None):
        self._items = None # reference to itself
        self.size = 0
        for i in range(len(dataList) - 1, -1, -1): # insert from head
            self.add(dataList[i])

    def add(self, data):
        """ Set default that the current node is head"""
        self._items = Node(data, self._items)
        self.size += 1
        
    def __iter__(self):
        cursor = self._items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next