#!/usr/bin/env python

'''Module for k times_leftrotation'''

def pre_process(test_array, n_num):

    '''Function Definition for Preprocess'''
    temp_var = [None] * (2 * n_num)

    for i in range(n_num):
        temp_var[i] = temp_var[i + n_num] = test_array[i]
    return temp_var

def left_rotate(n_num, k, temp_var):

    '''Function definition for left Rotation'''
    start = k % n_num
    for i in range(start, start + n_num):
        print(temp_var[i], end=' ')
    print("")

for _ in range(int(input())):
    TEST_ARRAY = list(map(int, input().split()))
    N = len(TEST_ARRAY)
    TEMP = pre_process(TEST_ARRAY, N)
    K = int(input())
    left_rotate(N, K, TEMP)
    K = int(input())
    left_rotate(N, K, TEMP)
    K = int(input())
    left_rotate(N, K, TEMP)
