# 이진탐색은 배열이 정렬된 상태여야 한다!
arr = [8, 11, 16, 28, 39, 49, 60, 67, 85, 89]
N = len(arr)

def BinarySearch(start, end, key):

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1

print(BinarySearch(0, N, 20))
print(BinarySearch(0, N, 85))