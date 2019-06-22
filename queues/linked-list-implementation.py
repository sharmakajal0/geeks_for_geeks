# Implementation of queue using Linked list

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.last = None
        self.next = next
    
    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def setLast(self, last):
        self.last = last

    def getLast(self):
        return self.last
    
    def hasNext(self):
        return self.next != None

class Queue(object):
    def __init__(self, data = None):
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, data):
        self.lastNode = self.front
        self.front = Node(data, self.front)
        if self.lastNode:
            self.lastNode.setLast(self.front)
        if self.rear is None:
            self.rear = self.front
        self.size += 1

    def queueFront(self):
        if self.front is None:
            raise IndexError
        return self.front.getData()
    
    def queueRear(self):
        if self.rear is None:
            raise IndexError
        return self.rear.getData()
    
    def deQueue(self):
        if self.rear is None:
            raise IndexError
        result = self.rear.getData()
        self.rear = self.rear.last
        self.size -= 1
        return result
    
    def sizeof(self):
        return self.size

que = Queue()
que.enQueue("first")
que.enQueue("second")
que.enQueue("third")
print("Front", que.queueFront())
print("Rear", que.queueRear())
que.deQueue()
print("Front", que.queueFront())
que.enQueue(45)
que.enQueue(65)
que.enQueue(54)
que.enQueue(887)
print("Front", que.queueFront())
print("Rear", que.queueRear())
print(que.sizeof())
que.deQueue()
print(que.sizeof())
