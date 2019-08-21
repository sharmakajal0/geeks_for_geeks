#!/usr/bin/env python

'''Module for maximum sum contiguous subarray'''

def maximum_sum_contiguous_subarray(contiguous_array):

    '''Function for contiguous subarrays'''
    max_till_here = 0
    max_so_far = 0

    for i in contiguous_array:
        max_till_here += i

        if max_till_here < 0:
            max_till_here = 0

        if max_so_far < max_till_here:
            max_so_far = max_till_here

    return max_so_far


for _ in range(int(input())):
    TEST_ARRAY = list(map(int, input().split()))
    print(maximum_sum_contiguous_subarray(TEST_ARRAY))
