
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1
A = [3,1,4,1,5,9,2,6,5,3,5]
key = 4
print(sequential_search(A,key))