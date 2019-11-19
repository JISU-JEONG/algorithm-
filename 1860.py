import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    guest = list(map(int, input().split()))
    f_b, i = 0, 1
    flag = 0
    while guest:
        copy = []
        cnt = []
        while guest:
            f = guest.pop()
            if f < M*i:
                cnt.append(f)
            else:
                copy.append(f)

        if len(cnt) > f_b:
            flag = 1
            break
        else:
            f_b -= len(cnt)
            guest = copy
        f_b += K
        i += 1

    if flag == 0:
        print('#{} Possible'.format(t))
    else:
        print('#{} Impossible'.format(t))