
def b_find(lo, hi, n, d):
    global cnt
    if lo > hi:
        return
    mid = (lo+hi)>>1
    if arr[mid] == n:
        cnt+=1
    elif arr[mid] > n and d !=0:
        b_find(lo,mid-1,n,0)
    elif arr[mid]< n and d != 1:
        b_find(mid+1,hi,n,1)
    else:
        return


T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    numbers = list(map(int, input().split()))
    cnt = 0
    for number in numbers:
        if b_find(0,N-1,number,2):
            cnt+=1
    print('#{} {}'.format(t, cnt))