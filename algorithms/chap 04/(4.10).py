def kth_smallest_sort(A, k):
    A.sort()
    return A[k-1]

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
k = 3
result = kth_smallest_sort(test_list, k)
print(f"{k}번째로 작은 원소는: {result}")