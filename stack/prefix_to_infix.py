#!/usr/bin/env python

'''Module for conversion of an infix expression to prefix expression'''

class Conversion:

  '''Initialization of Conversion Class'''
  def __init__(self):
    self.stack = []

  def push(self, op):
    operators = ['+', '-', '*', '/']
    if op in operators:
      op1 = self.stack.pop()
      op2 = self.stack.pop()
      self.stack.append('(%s %s %s)'% (op1, op, op2))
    else:
      self.stack.append(op)
  def convert(self, test_list):
    test_list.reverse()
    for i in test_list:
      self.push(i)
    return self.stack.pop()

c = Conversion()

for _ in range(int(input())):
  my_list = list(map(str, input().split()))
  print("The prefix expression of the given infix expression is", end=' ')
  print(c.convert(my_list))
