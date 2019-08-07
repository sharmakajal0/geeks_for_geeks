#!/usr/bin/env python

'''Module for finding the minimum element in the array'''

def find_minimum(test_array, low, high):

    '''Function Definition to find the minimum value in an array'''
    if high < low:
        return test_array[0]

    if high == low:
        return test_array[low]

    mid_value = int((low + high)/2)

    if mid_value < high and test_array[mid_value+1] < test_array[mid_value]:
        return test_array[mid_value+1]

    if mid_value > low and test_array[mid_value] < test_array[mid_value - 1]:
        return test_array[mid_value]

    if test_array[high] > test_array[mid_value]:
        return find_minimum(test_array, low, mid_value-1)
    return find_minimum(test_array, mid_value+1, high)

for _ in range(int(input())):
    TEST_ARRAY = list(map(int, input().split()))
    n = len(TEST_ARRAY)
    print(find_minimum(TEST_ARRAY, 0, n-1))
