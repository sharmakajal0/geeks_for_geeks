#!/usr/bin/env python

'''Module for Search Element'''

class Node:

  '''Initialization of Node Class'''
  def __init__(self, key):
    self.key = key
    self.next = None

class LinkedList:

  '''Initialization of Linked list class'''
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def search(self, x):
    current = self.head

    while current is not None:
      if current.key == x:
        return True
      current = current.next

    return False

if __name__ == "__main__":
  my_list = LinkedList()
  for _ in range(int(input())):
    N = int(input())
    my_list.push(N)
  X = int(input())
  if my_list.search(X):
    print("Yes, the element is in the list")
  else:
    print("No, the element is not in the list")
