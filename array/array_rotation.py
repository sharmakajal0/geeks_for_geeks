#!/usr/bin/env python

'''Module for array rotation'''

def array_rotation(test_array, times_rotation):

    '''Function for rotation of an array'''
    for _ in range(times_rotation):
        temp_var = test_array[0]
        array_length = len(test_array)

        for i in range(array_length - 1):
            test_array[i] = test_array[i + 1]

        test_array[array_length-1] = temp_var

    for j in range(array_length):
        print("%d" % test_array[j], end=' ')

for _ in range(int(input())):
    TEST_ARRAY = list(map(int, input().split()))
    print("Enter the number of times the array is to be rotated")
    TIMES_ROTATION = int(input())
    array_rotation(TEST_ARRAY, TIMES_ROTATION)
