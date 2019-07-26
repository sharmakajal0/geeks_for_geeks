#!/usr/bin/env python

'''Module for delete node'''

class Node:
  def __init__(self, data):
    self.data = data
    self.head = None

class LinkedList:

  '''Function Definition for initialization of Linked List'''
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def delete(self, pos):

    '''Function Definition to Delete Node'''
    if self.head is None:
      raise ValueError("Linked List is empty")

    temp = self.head
    if pos == 0:
      self.head = temp.next
      temp = None
      return
    for _ in range(pos - 1):
      temp = temp.next
      if temp is None:
        break
    if temp is None:
      return
    if temp.next is None:
      return
    next_pointer = temp.next.next
    temp.next = None
    temp.next = next_pointer

  def printlist(self):
    temp = self.head
    while temp:
      print("%d"%(temp.data), end="")
      temp = temp.next

llist = LinkedList()
print("Enter the number of elements to be pushed into the linked list")
print("Enter the elements to be pushed")
for _ in range(int(input())):
  n = int(input())
  llist.push(n)

print("Enter the number of elements to be deleted from the linked list")
print("Enter the elements to be deleted")
for _ in range(int(input())):
  m = int(input())
  llist.delete(m)
llist.printlist()
