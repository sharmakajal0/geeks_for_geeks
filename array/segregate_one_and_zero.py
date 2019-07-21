#!/usr/bin/env python

'''
Segregation of 0 and 1 in list
'''
from sys import argv

def segregate(arr: list):
    '''
    Segregate 0 and 1 in list
    '''
    zeroes = []
    ones = []

    for i in arr:
        if i == '0':
            zeroes.append(i)
        else:
            ones.append(i)

    return ones + zeroes
def main(args):
    '''
    Driver method for program
    '''
    print(args)
    input_array = str(input())
    print(''.join(segregate(input_array)))

if __name__ == "__main__":
    main(argv)
