def binary_search_iter(A, key, low, high) :
    while (low <= high) :
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

listA = [1, 3, 8, 13, 13, 16, 21, 26, 27, 30, 33, 36, 39, 41, 44, 49]
print("입력 리스트 = ", listA)
print("33 탐색(순환) --> ", binary_search_iter(listA, 33, 0, len(listA)-1))
print("33 탐색(반복) --> ", binary_search_iter(listA, 33, 0, len(listA)-1))
print("32 탐색(순환) --> ", binary_search_iter(listA, 32, 0, len(listA)-1))
print("32 탐색(반복) --> ", binary_search_iter(listA, 32, 0, len(listA)-1))