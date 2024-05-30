def knapSack_dp(w,wt,val,n):
    A = [[0 for x in range(w+1)for x in range(n+1)]]

    for i in range(1,n+1):
        for w in range(1,w+1):
            if wt[i-1]>w:
                A[i][w] = A[i-1][w]
            else:
                valwith = val[i-1] + A[i-1][w-wt[i-1]]
                valwithout = A[i-1][w]
                A[i][w] =max(valwith, valwithout)

    return A[n][w]

val = [60,100,190,120,200,150]
wt = [2,5,8,4,7,6]
w = 18
n = len(val)
print("0-1배낭문제(분할 정복):",knapSack_dp(w,wt,val,n))
print("0-1배낭문제(동적 계획):",knapSack_dp(w,wt,val,n))