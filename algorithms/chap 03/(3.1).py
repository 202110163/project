def printstep(arr, val):
    print(" step %2d = " % val, end='')
    print(arr)

def selection(A):
    n=len(A)
    for i in range(n-1):
        least =i
        for j in range(i+1, n):
            if(A[j]<A[least]):
                least =j
        A[i], A[least] = A[least], A[i]
        printstep(A, i+1)

data = [5,3,8,4,9,1,6,2,7]
print("original", data)
selection(data)
print("selection : ",data)