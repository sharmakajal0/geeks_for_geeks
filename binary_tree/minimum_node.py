#!/usr/bin/env python

'''Module for Finding Minimum node'''

class Node:

    '''Initialization of Node Class'''
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(node, data):

    '''Function Definition to insert node'''
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)

        return node

def min_value(node):

    '''Function definition to find the minimum node'''
    current = node

    while current.left is not None:
        current = current.left

    return current.data

ROOT_NODE = None
ROOT_NODE = insert(ROOT_NODE, 4)
insert(ROOT_NODE, 7)
insert(ROOT_NODE, 4)
insert(ROOT_NODE, 6)
insert(ROOT_NODE, 5)
print(min_value(ROOT_NODE))
