#!/usr/bin/env python

'''Module for the conversion of postfix to prefix expression'''

class Conversion:

    '''Initialization of class conversion'''
    def __init__(self):
        self.stack = []

    def convert(self, test_list):

        '''Function Definition of Conversion'''
        operators = ['+', '-', '*', '/']
        for i in test_list:
            if i not in operators:
                self.stack.append(i)
            else:
                op1 = self.stack.pop()
                op2 = self.stack.pop()
                self.stack.append('%s%s%s'%(i, op2, op1))

        return self.stack.pop()


MY_STACK = Conversion()
for _ in range(int(input())):
    MY_LIST = input()
    print(MY_STACK.convert(MY_LIST))
