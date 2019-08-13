#!/usr/bin/env python

'''Module for Reversal algorithm for array rotation'''

def reverse(test_array, arr_start, arr_end):

    '''Function for reversing of array'''
    while arr_start < arr_end:
        temp = test_array[arr_start]
        test_array[arr_start] = test_array[arr_end]
        test_array[arr_end] = temp
        arr_start += 1
        arr_end -= 1

def rotate(test_array, times_rotation):

    '''Function for rotation of array'''
    arr_length = len(test_array)
    reverse(test_array, 0, times_rotation-1)
    reverse(test_array, times_rotation, arr_length-1)
    reverse(test_array, 0, arr_length -1)
    for i in range(0, arr_length):
        print(test_array[i], end=' ')
    print('\n')

for _ in range(int(input())):
    TEST_LIST = list(map(int, input().split()))
    print('Array to be reversed')
    print(*TEST_LIST)

    print('Enter the number of times array is to be rotated: ') 
    TIMES_ROTATION = int(input())
    print(TIMES_ROTATION, '\n')

    print('Reversed array')
    rotate(TEST_LIST, TIMES_ROTATION)
    print('\n')
