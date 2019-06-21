# Implementation of queue using Dynamic Circular Array

class Queue(object):
    def __init__(self, limit = 3):
        self.que = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    def isEmpty(self):
        return self.size <= 0
    
    def enQueue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        
        else:
            self.rear = self.size
        self.size += 1
        print(self.que)
    
    def deQueue(self):
        if self.size <= 0:
            print("Queue is Underflow")
            return 0
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print(self.que)
    
    def queueFront(self):
        if self.front is None:
            print("The Queue is Empty")
            raise IndexError
        return self.que[self.front]
    
    def queueRear(self):
        if self.rear is None:
            print("The Queue is Empty")
            raise IndexError
        return self.que[self.rear]
    
    def sizeof(self):
        return self.size

    def resize(self):
        newQue = list(self.que)
        self.limit = 2 * self.limit
        self.que = newQue

que = Queue()
que.enQueue("First")
print("front", que.queueFront())
print("rear", que.queueRear())
que.enQueue("second")
print("front", que.queueFront())
print("rear", que.queueRear())
que.enQueue("third")
print("front", que.queueFront())
print("rear", que.queueRear())
que.enQueue("fourth")
print("front", que.queueFront())
print("rear", que.queueRear())
que.deQueue()
print("front", que.queueFront())
print("rear", que.queueRear())
print(que.sizeof())