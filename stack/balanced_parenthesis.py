#!/usr/bin/env python

'''Module for Balanced Parenthesis'''

def balanced(test_array):
    '''Function Definition for balanced parenthesis'''

    stack = []
    for sym in test_array:

        if sym in ('(', '[', '{'):
            stack.append(sym)
            continue

        stack_length = len(stack)

        if stack_length == 0:
            return False

        if sym == ')':

            temp_var = stack.pop()

            if temp_var in ('{', '['):
                return False

        elif sym == '}':
            temp_var = stack.pop()

            if temp_var in ('(', '['):
                return False

        else:
            temp_var = stack.pop()

            if temp_var in ('(', '{'):
                return False

    if stack_length:
        return False

    return True

if __name__ == "__main__":

    for _ in range(int(input())):
        TEST_ARRAY = list(map(str, input().split()))

        if balanced(TEST_ARRAY):
            print("Balanced")
        else:
            print("Not Balanced")
