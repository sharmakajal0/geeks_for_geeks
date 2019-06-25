#!/usr/bin/env python

def reverseList(A, start, end): 
	while start < end: 
		A[start], A[end] = A[end], A[start] 
		start += 1
		end -= 1

A = list(map(int, input().split()))
start = int(input())
end = int(input())
print("Before reversing ", A)
reverseList(A, start, end)
print("Reversed list is", A)
