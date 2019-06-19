def swap(arr, a, b, c):
    temp = a
    a = b
    b = c
    c = temp
def leftRotate(arr, d, n):  
    if(d == 0 or d == n):  
        return
    i = d  
    j = n - d  
    while (i != j):  
          
        if(i < j): 
            swap(arr, d - i, d + j - i, i)  
            j -= i  
          
        else: 
            swap(arr, d - i, d, j)  
            i -= j  
      
    swap(arr, d - i, d, i) 
def printArray(arr, size):
    for i in range(size):
        print("%d" %arr[i], end = " ")
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
leftRotate(arr, 2, 7)
print(arr, 7)
