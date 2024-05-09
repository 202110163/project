def quick_sort(A, left, right):
    if left < right:
        pivot_index = partition(A, left, right)
        quick_sort(A, left, pivot_index - 1)
        quick_sort(A, pivot_index + 1, right)

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original:", data)
quick_sort(data, 0, len(data) - 1)
print("QuickSort:", data)