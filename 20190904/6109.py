import copy
# 0, 1, 2, 3 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solve(board, d):
    new_board = copy.deepcopy(board)
    if d ==0 or d==2:
        stack = []
        for i in range(N):
            for j in range(N):
                if new_board[i][j]:
                    tmp = new_board[i][j]
                    col,raw = i+dx[d], j+dy[d]
                    while 0<=col<N and 0<=raw<N:
                        if new_board[col][raw] == 0:
                            new_board[col][raw] = tmp
                            new_board[col-dx[d]][raw-dy[d]] = 0
                        elif new_board[col][raw] == tmp:
                            stack.append((col,raw,2*tmp))
                            new_board[col][raw] = '*'
                            new_board[col-dx[d]][raw-dy[d]] = 0
                            break
                        else:
                            break
                        col, raw = col + dx[d], raw + dy[d]
        for x,y,value in stack:
            new_board[x][y] = value
    else:
        stack=[]
        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):
                if new_board[i][j]:
                    tmp = new_board[i][j]
                    col,raw = i+dx[d], j+dy[d]
                    while 0<=col<N and 0<=raw<N:
                        if new_board[col][raw] == 0:
                            new_board[col][raw] = tmp
                            new_board[col-dx[d]][raw-dy[d]] =0

                        elif new_board[col][raw] == tmp:
                            stack.append((col, raw, 2 * tmp))
                            new_board[col][raw] = '*'
                            new_board[col-dx[d]][raw-dy[d]] = 0
                            break
                        else:
                            break
                        col, raw = col + dx[d], raw + dy[d]
        for x, y, value in stack:
            new_board[x][y] = value
    return new_board

T = int(input())

for t in range(1,T+1):
    N, d = input().split()
    N = int(N)
    board = [list(map(int,input().split())) for _ in range(N)]
    if d == 'up':
        d =0
    elif d == 'down':
        d=1
    elif d== 'left':
        d=2
    else:
        d=3
    board=solve(board,d)
    print('#{}'.format(t))
    for b in board:
        print(*b)