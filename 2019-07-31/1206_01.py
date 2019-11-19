import sys
sys.stdin = open('input.txt', 'r')
for test in range(1, 11):
    N = int(input())
    board = [[0]*255 for _ in range(N)]

    cnt = 0

    apt = list(map(int, input().split()))


    for i in range(N):
        for j in range(apt[i]):
            board[i][j] = 1

    for i in range(N):
        if apt[i] == 0 : continue
        for j in range(apt[i]):
            if board[i][j] == 0: continue
            if i <= 1:
                if board[i+1][j] == board[i+2][j] == 0:
                    cnt += 1
            elif N-2 <= i:
                if board[i-1][j] == board[i-2][j] == 0:
                    cnt += 1
            else:
                if board[i-1][j] == board[i-2][j] == board[i+1][j] == board[i+2][j]== 0:
                    cnt += 1

    print('#{} {}'.format(test, cnt))