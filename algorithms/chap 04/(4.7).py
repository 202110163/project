def slow_power(x, n):
    result = 1.0
    for i in range(n):
        result = result * x
    return result

x = 2
n = 10
print(slow_power(x, n))