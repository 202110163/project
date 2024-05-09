def merge(A, left, mid, right):
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i, k = i + 1, k + 1
        else:
            temp[k] = A[j]
            j, k = j + 1, k + 1

    if i > mid:
        temp[k:k + right - j + 1] = A[j:right + 1]
    else:
        temp[k:k + mid - i + 1] = A[i:mid + 1]

    A[left:right + 1] = temp[left:right + 1]

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)

        merge(A, left, mid, right)

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
temp = [0] * len(data)
print("Original:", data)
merge_sort(data, 0, len(data) - 1)
print("Merge Sorted:", data)