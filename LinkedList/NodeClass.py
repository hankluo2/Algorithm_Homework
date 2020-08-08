"""
@File Node.py
@author Hankluo2
@date 2020-8-8
@desc A node class for linked list type
"""

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node
