def BinarySeach(key,P):
    lo = 1
    hi = P
    cnt = 0

    while lo<=hi:
        mid = (lo+hi)>>1

        if mid == key:
            return cnt
        elif mid > key:
            hi = mid
        else:
            lo = mid

        cnt += 1





T = int(input())

for t in range(1, T+1):
    P, A, B = map(int,input().split())

    if BinarySeach(A, P) < BinarySeach(B, P):
        print('#{} A'.format(t))
    elif BinarySeach(A, P) > BinarySeach(B, P):
        print('#{} B'.format(t))
    else:
        print('#{} 0'.format(t))