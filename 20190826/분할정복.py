arr = [6, 4, 2, 5, 1, 55, 9, 2, 11, 8, 1, 7]

def getMin(lo, hi): # 재귀 호출
    mid = (lo+hi)>>1
    if lo==hi:
        return arr[lo]
    else:
        return min(getMin(lo,mid), getMin(mid+1,hi))


print(getMin(0,len(arr)-1))