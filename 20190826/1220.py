import sys
import pprint
sys.stdin = open('input.txt', 'r')

for t in range(1,11):
    N = int(input())

    board = [list(map(int, input().split())) for _ in  range(N)]
    flag = 1
    cnt = 0
    # 1 N극 / 2
    while flag:
        flag = 0
        for i in range(N):
            for j in range(N):
                if j != 99 and board[j][i] == 1 and board[j+1][i] == 0:
                    board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
                    flag = 1
                if j != 99 and board[j][i] == 0 and board[j+1][i] == 2:
                    board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
                    flag = 1
                if board[0][i] == 2:
                    board[0][i] = 0
                    flag = 1
                if board[99][i] == 1:
                    board[99][i] = 0
                    flag = 1

    flag = 0
    for i in range(N):
        for j in range(N-1):
            if flag ==1 :
                if board[j][i] != board[j+1][i]:
                    flag =0
                continue
            if board[j][i]+board[j+1][i] == 3:
                cnt += 1
                flag =1

    print('#{} {}'.format(t, cnt))

