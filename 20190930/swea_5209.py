def back(x, total, used, N, row):
    global MIN_N

    if total >= MIN_N:
        return


    if row == N:
        if MIN_N > total:
            MIN_N = total
        return

    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                back(x, total+x[row][i], used, N, row+1)
                used[i] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    x =[0]*N
    MIN_N = 10000
    for i in range(N):
        x[i] = list(map(int, input().split()))

    back(x, 0, [0]*N, N, 0)
    print('#{} {}'.format(test_case,MIN_N))