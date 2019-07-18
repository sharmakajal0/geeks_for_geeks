#!/usr/bin/env python

'''module for queue using two stacks'''

class Queue:

    '''Initialization of class'''
    def __init__(self):
        self.s_one = []
        self.s_two = []

    def enqueue(self, element):

        '''Function Definition for Enqueue of Elements'''
        self.s_one.append(element)

    def dequeue(self):

        '''Function Definition for Dequeue of Elements'''
        if not self.s_two:
            while self.s_one:
                self.s_two.append(self.s_one.pop())
        return self.s_two.pop()

TEST_QUEUE = Queue()
TEST_INTEGER = int(input())
for i in range(1, TEST_INTEGER + 1):
    TEST_QUEUE.enqueue(i)
for i in range(1, TEST_INTEGER + 1):
    print(TEST_QUEUE.dequeue())
