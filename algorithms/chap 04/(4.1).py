def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recur(n - 1)

print(f"10!는 {factorial_recur(10)}")