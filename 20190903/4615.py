T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    if N == 4:
        board = [
            [0,0,0,0],
            [0,2,1,0],
            [0,1,2,0],
            [0,0,0,0]
        ]
    elif N==6:
        board = [
            [0, 0, 0, 0, 0 ,0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 2, 1, 0, 0],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
    else:
        board = [
            [0, 0, 0, 0, 0, 0, 0 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    for _ in range(M):
        i, j, stone = map(int, input().split())
        board[i-1][j-1] = stone
        x, y = i - 2, j - 1
        while 0<=x:
            if board[x][y] == 0:
                break
            elif board[x][y] != stone:
                board[x][y] = stone
            else:
                break
            x -= 1

        x, y = i, j - 1
        while x < N:
            if board[x][y] == 0:
                break
            elif board[x][y] != stone:
                board[x][y] = stone
            else:
                break
            x += 1
        x, y = i - 1, j - 2
        while 0 <= y:
            if board[x][y] == 0:
                break
            elif board[x][y] != stone:
                board[x][y] = stone
            else:
                break
            y -= 1

        x, y = i - 1, j
        while x < N:
            if board[x][y] == 0:
                break
            elif board[x][y] != stone:
                board[x][y] = stone
            else:
                break
            y += 1
    print(board)