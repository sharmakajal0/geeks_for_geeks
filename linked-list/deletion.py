#!/usr/bin/env python
'''Module for Linked List'''

class Node:

    '''Initializing Class'''
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:

    ''' defining class of linked list'''
    def __init__(self):
        self.head = None

    def push(self, new_data):
        ''' defining push function'''
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        '''Defining delete function'''
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def print_list(self):
        ''' Print function'''
        temp = self.head
        while temp:
            print("%d "%(temp.data), end=' ')
            temp = temp.next

MY_LIST = LinkedList()
MY_LIST.push(1)
MY_LIST.push(2)
MY_LIST.push(5)
MY_LIST.print_list()
print("\t")
MY_LIST.delete_node(2)
MY_LIST.print_list()
MY_LIST.delete_node(5)
MY_LIST.delete_node(1)
MY_LIST.print_list()
print("\t")
