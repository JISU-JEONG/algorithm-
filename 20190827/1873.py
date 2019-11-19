def detect(x, y):
    if 0<=x<H and 0<=y<W and board[x][y] =='.': return 1
    else: return 0


def keyboard(command, x, y):
    if command == 'U':
        nx, ny = x-1,y
        if detect(nx, ny):
            board[nx][ny] = '^'
            board[x][y] = '.'
            return (nx, ny)
        else:
            board[x][y] = '^'
    elif command == 'D':
        nx, ny = x + 1, y
        if detect(nx, ny):
            board[nx][ny] = 'v'
            board[x][y] = '.'
            return (nx, ny)
        else:
            board[x][y] = 'v'
    elif command == 'L':
        nx, ny = x, y -1
        if detect(nx, ny):
            board[nx][ny] = '<'
            board[x][y] = '.'
            return (nx, ny)
        else:
            board[x][y] = '<'
    else:
        nx, ny = x , y +1
        if detect(nx, ny):
            board[nx][ny] = '>'
            board[x][y] = '.'
            return (nx, ny)
        else:
            board[x][y] = '>'

    return (x,y)

def shoot(x,y):
    k = 1
    if board[x][y] == '<':
        while y-k>=0:
            if board[x][y-k] == '*':
                board[x][y - k] = '.'
                break
            elif board[x][y-k] == '#':
                break
            k += 1
    elif board[x][y] == '>':
        while y+k<W:
            if board[x][y+k] == '*':
                board[x][y + k] = '.'
                break
            elif board[x][y+k] == '#':
                break
            k += 1
    elif board[x][y] == '^':
        while x-k>=0:
            if board[x-k][y] == '*':
                board[x-k][y] = '.'
                break
            elif board[x-k][y] == '#':
                break
            k += 1
    else:
        while x+k < H:
            if board[x+k][y] == '*':
                board[x+k][y] = '.'
                break
            elif board[x+k][y] == '#':
                break
            k += 1


T = int(input())

for t in range(1, T+1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    N = int(input())
    commands = input()
    for i in range(H):
        for j in range(W):
            if board[i][j] in 'v^<>':
                s_x , s_y = i, j
    for command in commands:
        if command == 'S':
            shoot(s_x,s_y)
        else:
            s_x,s_y = keyboard(command,s_x,s_y)
    print('#{} '.format(t),end='')
    for b in board:
        print(''.join(b))