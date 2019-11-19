def f(row, score, N, m):
    global min_sol

    if score > min_sol:
        return
    if row == N:
        if score < min_sol:
            min_sol = score
            return min_sol

    for i in range(N):
        if col_check[i] == 0:
            col_check[i] = 1
            f(row + 1, score + m[row][i], N, m)
            col_check[i] = 0

    return min_sol


T = int(input())

for test_case in range(1, T + 1):
    INT_MAX = 10000
    min_sol = INT_MAX
    N = int(input())
    m = []
    col_check = [0] * N
    for _ in range(N):
        m.append(list(map(int, input().split())))

    print('#{} {}'.format(test_case, f(0, 0, N, m)))


