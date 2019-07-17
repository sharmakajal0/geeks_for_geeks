def SearchElement(arr, n, x):

    ''' Search function'''
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1

TEST_ARRAY = [1, 2, 3, 3, 4, 5, 6]
X = 4
N = len(TEST_ARRAY)
RESULT_INDEX = SearchElement(TEST_ARRAY, N, X)
if RESULT_INDEX == -1:
    print("The element is not in the list ")
else:
    print("The Index of the given element is ", RESULT_INDEX)
