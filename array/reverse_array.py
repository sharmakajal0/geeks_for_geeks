#!/usr/bin/env python

'''Module for the reverse of the array'''

def reverse_array(test_array):

  '''Function to reverse an array'''
  start = 0
  end = len(test_array) - 1
  for _ in range(start, end):
    test_array[start], test_array[end] = test_array[end], test_array[start]
    start += 1
    end -= 1
    if start >= end:
      break
  print(*test_array)

for _ in range(int(input())):
  TEST_ARRAY = list(map(int, input().split()))
  reverse_array(TEST_ARRAY)
