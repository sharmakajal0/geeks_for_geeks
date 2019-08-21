#!/usr/bin/env python

def minimum_distance(test_array, x, y):
    for i, num in enumerate(test_array):
        if num == x:
            a = i

    for j, num2 in enumerate(test_array):
        if num2 == y:
            b = j

    answer = b - a

    if answer < 0:
        answer = answer * (-1)

    return answer

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print('Enter any two different integers from the array')
    x, y = map(int, input().split())
    print('The minimum distance between the two values is:', end=' ')
    print(minimum_distance(arr, x, y))
