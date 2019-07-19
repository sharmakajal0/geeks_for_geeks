#!/usr/bin/env python

'''Module for finding the maximum sum using rotation'''

def max_sum(arr):

    '''Function Definition for calculating maximum sum of elements in the array'''
    arr_sum = 0
    curr_val = 0
    n_length = len(arr)
    for i in range(0, n_length):
        arr_sum = arr_sum + arr[i]
        curr_val = curr_val + (i * arr[i])

    max_val = curr_val

    for i in range(1, n_length):
        curr_val = curr_val + arr_sum - n_length * arr[n_length - i]
        if curr_val > max_val:
            max_val = curr_val
    return max_val

for _ in range(int(input())):
    TEST_ARRAY = list(map(int, input().split()))
    print(max_sum(TEST_ARRAY))
