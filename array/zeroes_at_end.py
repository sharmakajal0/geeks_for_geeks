#!/usr/bin/env python

'''Module for zeroes at the end'''

def zeroes_end(test_array):

    '''function definition to move zeroes at the end'''
    array_length = len(test_array)
    count = 0
    test_array.sort()
    for i in test_array:
        if i != 0:
            test_array[count] = i
            count += 1

    while count < array_length:
        test_array[count] = 0
        count += 1
    return test_array

if __name__ == "__main__":
    for _ in range(int(input())):

        TEST_LIST = list(map(int, input().split()))
        print(zeroes_end(TEST_LIST))
