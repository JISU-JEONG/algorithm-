def binarySeach(arr, key):
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = (lo + hi) >> 1 # 몫이 나온다.
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1

    return False

# 재귀 호출 방식
def binarySeach2(arr, key, lo, hi):
    if lo > hi:
        return False
    else:
        mid = (lo + hi) >> 1
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            binarySeach2(arr, key, lo, mid-1)
        else:
            binarySeach2(arr, key, mid + 1, hi)