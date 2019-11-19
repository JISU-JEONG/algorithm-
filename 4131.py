
def find(x):

    tmp = x[0]
    cnt = 1
    for i in range(1, len(x)):
        if tmp == x[i]:
            cnt += 1
            continue

        elif tmp < x[i]:
            if cnt < X or x[i] - tmp > 1:
                return 0
            tmp = x[i]
            cnt = 1

        else:
            if tmp-x[i] > 1:
                return 0
            tmp = x[i]
            if i + X > len(x):
                return 0
            for j in range(i, i+X):
                if tmp != x[j]:
                    return 0
            cnt = -X

    print(x)
    return 1


T = int(input())

for t in range(1, T+1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(len(board)):
        if find(board[i]):
            cnt += 1
    print()
    for i in range(len(board)):
        for j in range(len(board)):
            if i < j :
                board[i][j], board[j][i] = board[j][i], board[i][j]
    for i in range(len(board)):
        if find(board[i]):
            cnt += 1

    print('#{} {}'.format(t,cnt))