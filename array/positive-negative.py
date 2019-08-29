#!/usr/bin/env python

def positive_negative(test_array):

    n = len(test_array)
    pivot = -1

    for j in range(n):
        if test_array[j] < 0:
            pivot += 1
            test_array[pivot], test_array[j] = test_array[j], test_array[pivot]

    positive, negative = pivot + 1, 0

    while (positive < n and negative < positive and test_array[negative] < 0):
        test_array[negative], test_array[positive] = test_array[positive], test_array[negative]
        positive += 1
        negative += 2

    return test_array


arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9] 
print(positive_negative(arr))
