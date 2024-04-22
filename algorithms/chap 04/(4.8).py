def slow_power(x,n):
    result = 1.0
    for i in range(n):
        result = result *x
    return result

def power(x,n):
    if n==0:
        return 1
    elif(n%2)==0:
        return power(x*x,n//2)
    else:
        return x*power(x*x,(n-1)//2)
    
import time
print("억지기법(2**500)=",power(2.0,500))
print("축소정복기법(2**500)=",slow_power(2.0,500))

t1 = time.time()
for i in range(100000): power(2.0,500)
t2 = time.time()
for i in range(100000): power(2.0,500)
t3 = time.time()
print("억지기법 시간 : ",t3-t2)
print("축소정복기법 시간 :",t2-t1)