#!/usr/bin/env python

'''Binary Search Tree'''

class Node:

    ''' Initiation defining Method'''
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, node):

    ''' Insert function'''
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    '''Order of values'''
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

TEST_TREE = Node(50)
insert(TEST_TREE, Node(43))
insert(TEST_TREE, Node(32))
insert(TEST_TREE, Node(65))
insert(TEST_TREE, Node(21))
insert(TEST_TREE, Node(47))
insert(TEST_TREE, Node(89))
insert(TEST_TREE, Node(12))
inorder(TEST_TREE)
