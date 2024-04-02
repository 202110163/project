def binary_digits(n):
    count = 1
    while n > 1:
        count = count + 1
        n = n // 2
    return count
result=binary_digits(10)
print(result)