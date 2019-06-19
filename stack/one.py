from sys import maxsize
def createStack():
    stack = []
    return stack

def isempty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item)

def pop(stack):
    if (isempty(stack)):
        return(-maxsize - 1)

    return stack.pop()

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack), "Popped from stack")