def binary_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 2
    return count
result=binary_digits(10)
print(result)