def factorial_iter(n) :
    result = 1
    for k in range(1, n+1) :
        result = result * k
    return result

print(f"8!는 {factorial_iter(10)}")