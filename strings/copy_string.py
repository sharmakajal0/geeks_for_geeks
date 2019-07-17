#!/usr/bin/env python

'''module for copy of one string to another and reverse of that string'''
def copy(string_one, string_two):

    '''Function Definition for copying string'''
    a_length = len(string_one)
    for i in range(a_length):
        string_two[i] = string_one[i]
    print("".join(string_two))

for _ in range(int(input())):
    S_ONE = input()
    S_TWO = (['']*(len(S_ONE)))
    copy(S_ONE, S_TWO)
    reverse = S_TWO [::-1]
    print("".join(reverse))
