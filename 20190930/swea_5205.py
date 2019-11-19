
def quick_sort(lo, hi, arr):
    if lo>=hi:
        return
    i,j = lo,hi
    while i < j:
        while i<=hi and arr[i] <= arr[lo]:
            i += 1
        while arr[j] > arr[lo]:
            j -= 1
        if i >=j: break
        arr[i],arr[j] = arr[j],arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]

    quick_sort(lo,j-1,arr)
    quick_sort(j+1, hi,arr)



T = int(input())

for t in range(1,T+1):
    N = int(input())
    unsort = list(map(int,input().split()))
    quick_sort(0,N-1,unsort)
    print("#{} {}".format(t,unsort[N//2]))