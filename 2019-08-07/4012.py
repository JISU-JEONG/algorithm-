import sys

sys.stdin = open('input.txt','r')

T = int(input())

for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    MIN_N = 0xFFFF
    for i in range(1<<N):
        cook1 = []
        cook2 = []
        for j in range(N):
            if i & (1<<j):
                cook1.append(j)
            else:
                cook2.append(j)
        if len(cook1) == N//2:
            S1, S2 = 0, 0
            for k in range(len(cook1)):
                for l in range(len(cook1)):
                    if k != l:
                        S1 += board[cook1[k]][cook1[l]]
                        S2 += board[cook2[k]][cook2[l]]
            if MIN_N > abs(S1-S2):
                MIN_N = abs(S1-S2)

    print('#{} {}'.format(t+1, MIN_N))
