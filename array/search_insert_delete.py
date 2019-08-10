#!/usr/bin/env python

'''Module for search, insert, and delete'''

def test_operations(test_list, item):

    '''function to search an element, delete the element and insert a new element'''
    for i, num in enumerate(test_list):
        if item == num:
            print('the item is found at index', i)
            popped_element = test_list.pop(i)
            print('the item popped is ', popped_element)
            break

        if item not in test_list:
            test_list.append(item)
            print("The new list", test_list)
            break

for _ in range(int(input())):
    my_list = list(map(int, input().split()))
    print("Enter the element to be searched into the array")
    N = int(input())
    test_operations(my_list, N)
