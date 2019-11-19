

def mergeSort(lo, hi):
    if lo >= hi: return
    mid = (lo + hi) >> 1
    mergeSort(lo, mid)
    mergeSort(mid+1, hi)

    i, j, k = lo, mid+1, lo
    while i<=mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; k,i=k+1,i+1
        else:
            tmp[k] = arr[j]; k, j=k+1,j+1
    while i<= mid:
        tmp[k] = arr[i]; k, i = k+1,i+1
    while j<= hi:
        tmp[k] = arr[j]; k, j = k+1,j+1
    for i in range(lo,hi+1):
        arr[i] = tmp[i]

T= int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    arr=[]
    for _ in range(M):
        arr.extend(list(map(int, input().split())))
    L = N*M
    tmp = [0]*L
    mergeSort(0, L-1)
    result = []
    for i in range(L-1,L-11,-1):
        result.append(arr[i])
    print(*result)