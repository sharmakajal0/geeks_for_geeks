#!/usr/bin/env python

def segregate(arr, n):
    count = 0

    for i in range(0, n):
        if arr[i] == 0:
            count = count + 1
    
    for i in range(0, count):
        arr[i] = 0
    
    for i in range(count, n):
        arr[i] = 1
    
    for i in range(0, n):
        print(arr[i], end = ' ')

arr = list(map(int, input().split()))
n = len(arr)

segregate(arr, n)
