#!/usr/bin/env python

## 
# Simple circular array based implementation of Queue
##

class Queue(object):
    def __init__(self, limit = 5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        if self.size <= 0:
            return ("Queue is empty")
    def enQueue(self, item):
        if self.size >= self.limit:
            print("Queue Overflow")
        else:
            self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        self.rear = self.size
        self.size += 1
        print(self.que)
    def deQueue(self):
        if self.size <= 0:
            print("Queue Underflow")
        else:
            self.que.pop(0)
            self.size -= 1
        if self.size == 0:
            self.front = self.rear = None
        self.rear = self.size - 1
        print(self.que)
    def queueRear(self):
        if self.rear is None:
            raise IndexError
        print(self.rear)
    
    def queueFront(self):
        if self.front is None:
            raise IndexError
        print(self.front)
    
    def size(self):
        return self.size
myQueue = Queue()
myQueue.enQueue("first")
myQueue.queueFront()
myQueue.deQueue()
myQueue.enQueue("second")
myQueue.queueFront()