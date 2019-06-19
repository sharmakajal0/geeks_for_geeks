class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enQueue(self, x):
        while len(self.s1) != 3:
            if len(self.s1) == 0:
                self.s1.append(x)
            return x

    def deQueue(self):
        if len(self.s1) == 0:
            print("stack is empty")
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1[-1])
                self.s1.pop()

            while len(self.s2) != 0:
                self.s2.pop()
            
if __name__ == "__main__":
    q = Queue()
    print(q.enQueue(1))
    print(q.enQueue(2))
    print(q.enQueue(3))
    print(q.enQueue(4))
    print(q.enQueue(5))

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())