#!/usr/bin/env python

'''Module for Pivoted Binary Search'''

def findpivot(test_array):

    '''Function to find pivot'''
    if test_array[0] <= test_array[len(test_array) - 1]:
        return -1

    if len(test_array) is None:
        return None

    start = 0
    end = len(test_array) - 1

    while start <= end:

        mid = int((start + end)/ 2)

        if test_array[mid] > test_array[mid + 1]:
            return mid

        if test_array[mid] < test_array[mid - 1]:
            return mid - 1

        if test_array[start] >= test_array[mid]:
            end = mid - 1

        else:
            start = mid + 1

def binarysearch(test_array, lower_value, upper_value, key):

    '''Function for binary search'''
    if upper_value < lower_value:
        return -1

    mid = int((lower_value + upper_value) / 2)

    if key == test_array[mid]:
        return mid

    if key > test_array[mid]:
        return binarysearch(test_array, mid + 1, upper_value, key)

    return binarysearch(test_array, lower_value, mid - 1, key)

def pivoted_binary_search(test_array, array_length, key):

    '''Function for pivoted binary search'''
    pivot = findpivot(test_array)

    if pivot == -1:
        return binarysearch(test_array, 0, array_length - 1, key)

    if test_array[pivot] == key:
        return pivot

    if test_array[0] <= key:
        return binarysearch(test_array, 0, pivot - 1, key)
    return binarysearch(test_array, pivot + 1, array_length - 1, key)

for _ in range(int(input())):
    TEST_ARRAY = list(map(int, input().split()))
    N = len(TEST_ARRAY)
    SEARCH_ELEMENT = int(input())
    print(pivoted_binary_search(TEST_ARRAY, N, SEARCH_ELEMENT))
