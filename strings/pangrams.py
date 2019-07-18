#!/usr/bin/env python

'''Module for pangrams'''

def pangrams(my_string):

    '''Function Definition for Pangrams'''
    my_list = []
    for _ in range(26):
        my_list.append(False)

    for _ in my_string.lower():
        if not _ == " ":
            my_list[ord(_) - ord('a')] = True

    for i in my_list:
        if i is False:
            return False
    return True

SENTENCE = input()
if pangrams(SENTENCE):
    print("pangram")

else:
    print("not pangram")

# the sentence can be ...
# SENTENCE = "The quick brown fox jumps over the lazy dog"
