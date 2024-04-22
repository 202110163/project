import time

def powerMat(x, n) :
    if n == 1 :
        return x
    elif (n%2) == 0 :
        return powerMat(multMat(x,x), n // 2)
    else :
        return multMat(x, powerMat(multMat(x,x), (n - 1) // 2))
    
print("억지기법(2**500)=", powerMat(2.0, 500))
print("축소정복기법(2**508) =", multMat(2.0, 508))

t1 = time.time()
for i in range(100000) : powerMat(2.0, 500)
t2 = time.time()
for i in range(100000) : multMat(2.0, 500)
t3 = time.time()

print("억지기법 시간... ", t3-t2)
print("축소정복기법 시간... ", t2-t1)