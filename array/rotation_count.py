#!/usr/bin/env python

'''Module for rotation count'''

def rotation_count(test_array, n_num):

    '''Function Definition to count the number of rotations'''
    min_num = test_array[0]
    for i in range(0, n_num):
        if min_num > test_array[i]:
            min_num = test_array[i]
            min_index = i
    return min_index

for i in range(int(input())):
    TEST_ARRAY = list(map(int, input().split()))
    N_NUM = len(TEST_ARRAY)
    print(rotation_count(TEST_ARRAY, N_NUM))
