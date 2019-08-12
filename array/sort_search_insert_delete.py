#!/usr/bin/env python

'''Module for search, insert and delete in a sorted array'''

def test_operations(test_list, key):

    '''Function for search, insert and delete in a sorted array'''
    test_list.sort()

    for i, value in enumerate(test_list):
        if key == value:
            print("The value is found at index ", i)

            print("Now we are deleting the element from the list")
            popped_element = test_list.pop(i)
            print("The item popped from the list is ", popped_element)

            break

        if key not in test_list:
            print("The item was not found in the list, hence we are appending it to the list")

            test_list.append(key)
            test_list.sort()
            print("The key was not found in the list hence after appending the new element")
            print("The new list is ", test_list)

            break

for _ in range(int(input())):
    TEST_ARRAY = list(map(int, input().split()))
    print("Enter the element to be searched")
    KEY = int(input())
    test_operations(TEST_ARRAY, KEY)
