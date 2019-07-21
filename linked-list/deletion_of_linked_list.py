#!/usr/bin/env python

'''module for linked list'''

class Node:

    '''Initialization function for Node class'''
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    '''Initialization function for LinkedList class'''
    def __init__(self):
        self.head = None

    def delete_list(self):

        'Function definition for deleting list'
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

    def push(self, new_data):

        '''Function definition for adding new elements into the list'''
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

if __name__ == "__main__":
    L_LIST = LinkedList()
    L_LIST.push(1)
    L_LIST.push(2)
    L_LIST.push(3)
    L_LIST.push(4)
    L_LIST.push(5)
    L_LIST.delete_list()
