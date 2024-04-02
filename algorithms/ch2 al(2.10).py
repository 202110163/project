def binary_digits(n):
    if n <=1:
        return 1
    else:
        return 1 + binary_digits(n//2)