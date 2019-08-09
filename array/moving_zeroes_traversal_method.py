#!/usr/bin/env python

'''Module for moving zeroes to the end'''

def move_zeroes(test_list):

    '''Function for moving zeroes at the end in a list using traversal method'''
    array_length = len(test_list)
    count = 0
    for i in range(0, array_length):
        if test_list[i] != 0:
            test_list[count], test_list[i] = test_list[i], test_list[count]
            count += 1

    return test_list

if __name__ == "__main__":
    for _ in range(int(input())):
        MY_LIST = list(map(int, input().split()))
        print(move_zeroes(MY_LIST))
