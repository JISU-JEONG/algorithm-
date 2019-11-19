
def merge_sort(lo, hi):
    global cnt
    if lo == hi: return
    mid = (lo+hi) >> 1
    if (hi-lo+1)%2:
        mid -= 1
        merge_sort(lo, mid)
        merge_sort(mid+1, hi)
    else:
        merge_sort(lo, mid)
        merge_sort(mid + 1, hi)
    if arr[mid] > arr[hi]:
        cnt +=1
    i,j,k = lo, mid+1, lo
    while i<=mid and j <= hi:
        if arr[i]<=arr[j]:
            tmp[k]=arr[i]; k,i = k+1, i+1
        else:
            tmp[k]=arr[j];k, j = k + 1, j + 1
    while i<=mid:
        tmp[k]=arr[i]; k,i = k+1, i+1
    while j<=hi:
        tmp[k]=arr[j];k, j = k + 1, j + 1
    for i in range(lo,hi+1):
        arr[i] = tmp[i]

T = int(input())
for t in range(1, T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    merge_sort(0, len(arr)-1)
    print("#{}".format(t), end=' ')
    print(arr[N//2], cnt)