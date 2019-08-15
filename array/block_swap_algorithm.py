#!/usr/bin/env python

'''Module for Block Swap algorithm for array rotation'''

def block_swap(test_array, rotation_count, array_size):

    '''Function for rotation of array'''
    for i in range(0, rotation_count):
        test_array.append(test_array[0])
        test_array.pop(0)

    for i in range(0, array_size):
        print(test_array[i], end=" ")
    print('\n')

for _ in range(int(input())):
    print("Test Array")
    TEST_ARRAY = list(map(int, input().split()))
    print(TEST_ARRAY)

    print('rotation count')
    D = int(input())
    print(D)

    N = len(TEST_ARRAY)
    print('resultant array')
    block_swap(TEST_ARRAY, D, N)
