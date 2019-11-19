

def mergeSort(lo, hi):
    global cnt1, cnt2
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

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0]*N
    cnt1, cnt2 =0,0
    mergeSort(0, N-1)
    print(cnt1, cnt2)