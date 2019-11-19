# 병합정력 --> 연결리스트에 적합
# python List append(), pop(), slicing 을 사용하면 시간이 너무 오래 소요됨
# C-style, 배열을 사용하듯이
arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0]*len(arr)

def mergeSort(lo, hi):          # 문제의 크기 - 정렬할 자료의 범위
    if lo == hi: return
    mid = (lo+hi) >> 1
    mergeSort(lo, mid)
    mergeSort(mid+1,hi)
    # 왼쪽과 오른쪽 자료들이 정렬된 상태
    i, j, k = lo, mid+1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; k, i = k+1, i+1
        else:
            tmp[k] = arr[j]; k ,j = k+1, j+1
    while i <= mid:
        tmp[k] = arr[i]; k, i = k + 1, i + 1
    while j <= hi:
        tmp[k] = arr[j]; k, j = k + 1, j + 1
    for x in range(lo, hi +1):
        arr[x] = tmp[x]
mergeSort(0, len(arr)-1)
print(arr)