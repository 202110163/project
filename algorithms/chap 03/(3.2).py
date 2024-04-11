def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1
result = sequential_search([1,2,3,4,5], 1)
print(result)
