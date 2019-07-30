#!/usr/bin/env python

'''Module for conversion of an postfix expression to prefix expression'''

class Conversion:

  '''Initialization of Conversion Class'''
  def __init__(self):
    self.stack = []

  def convert(self, test_list):

    '''function for conversion of prefix expression to postfix expression'''
    operators = set(['+', '-', '*', '/'])
    for _, letter in reversed(list(enumerate(test_list))):
      if letter not in operators:
        self.stack.append(letter)
      else:
        op1 = self.stack.pop()
        op2 = self.stack.pop()
        result = op1 + op2 + letter
        self.stack.append(result)
    return self.stack.pop()


c = Conversion()

for _ in range(int(input())):
  my_list = input()
  print("The postfix expression of the given prefix expression is", end=' ')
  print(c.convert(my_list))
