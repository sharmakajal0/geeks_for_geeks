#!/usr/bin/env python

'''Module for equal brackets'''

def matches(left, right):

    '''Function definition for matching parenthesis'''
    if left == '(' and right == ')':
        return True
    elif left == '{' and right == '}':
        return True
    elif left == '[' and right == ']':
        return True
    else:
        return False

def check_symbol(test_list):

    '''Function definition for checking the balance of brackets'''
    my_stack = []
    balanced = 0
    for sym in test_list:
        if sym in ('(', '[', '{'):
            my_stack.append(sym)
        else:
            if len(my_stack) is None:
                balanced = 0
                break
            if sym in ('}', ']', ')'):
                temp_var = my_stack.pop()
            if not matches(temp_var, sym):
                balanced = 0
                break
            else:
                balanced = 1
    if len(my_stack):
        balanced = 0
    return balanced

for _ in range(int(input())):
#    TEST_LIST = list(map(str, input().split()))
    INPUT_STRING = input()
    if check_symbol(INPUT_STRING) == 1:
        print('balanced')
    else:
        print('not balanced')
