import pprint

def solution(k):

    if k > 10:
        return -1
    else:
        for i in range(4):
            pass


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

Rx, Ry, Bx, By, O = 0, 0, 0, 0, 0

for i in range(1, N-1):
    for j in range(1, N-1):
        if board[i][j] == 'B':
            Bx, By = (i,j)
        if board[i][j] == 'R':
            Rx, Ry = (i,j)
        if board[i][j] == 'O':
            O = (i,j)

start = [[Bx,By,Rx,Ry]]

print(start)
