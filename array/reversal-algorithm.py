def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def leftrotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d - 1)
    rverseArray(arr, d, n - 1)
    rverseArray(arr, 0, n - 1)

def printArray(arr, size):
    for i in range(size):
        print(" %d " % arr[i], end = " ")

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
d = d % n
leftrotate(arr, 2)
printArray(arr, 7)