#!/usr/bin/env python

'''Module for Balanced Parenthesis'''

def balanced(test_array):
    '''Function Definition for balanced parenthesis'''

    stack = []
    for i in range(len(test_array)):

        if (test_array[i] == '(' or test_array[i] == '[' or test_array[i] == '{'):
            stack.append(test_array[i])
            continue

        stack_length = len(stack)

        if stack_length == 0:
            return False

        if test_array[i] == ')':

            temp_var = stack.pop()

            if temp_var in ('{', '['):
                return False

        elif test_array[i] == '}':
            temp_var = stack.pop()

            if temp_var in ('(', '['):
                return False

        elif temp_var == ']':
            temp_var = stack.pop()

            if temp_var in ('(', '{'):
                return False

    if stack_length:
        return True

    return False

if __name__ == "__main__":

    TEST_ARRAY = "{()}[]"

    if balanced(TEST_ARRAY):
        print("Balanced")
    else:
        print("Not Balanced")
