#!/usr/bin/env python

'''Module to find the sum of nodes in a binary tree'''

class Node:

    '''Initialization of function'''
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def addbinary_tree(root):

    '''Function Definition to add nodes of the binary tree'''
    if root is None:
        return 0

    return root.key + addbinary_tree(root.left) + addbinary_tree(root.right)

if __name__ == '__main__':
    ROOT_NODE = Node(2)
    ROOT_NODE.left = Node(1)
    ROOT_NODE.right = Node(45)
    ROOT_NODE.left.left = Node(23)
    ROOT_NODE.left.right = Node(21)
    ROOT_NODE.right.left = Node(11)
    ROOT_NODE.right.right = Node(34)
    TOTAL_SUM = addbinary_tree(ROOT_NODE)
    print(TOTAL_SUM)
