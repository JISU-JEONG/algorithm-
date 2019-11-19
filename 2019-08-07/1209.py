import sys

sys.stdin = open('input.txt', 'r')


for _ in range(10):
    t = input()
    board = [list(map(int, input().split())) for _ in range(100)]

    M = max(map(sum,board))
    for i in range(100):
        for j in range(100):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]
    N = max(map(sum,board))

    K, L = 0,0
    for i in range(100):
        K += board[i][i]
        L += board[99-i][i]

    print('#{} {}'.format(t, max(M, N, K, L)))