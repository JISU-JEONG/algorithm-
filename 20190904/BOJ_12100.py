import copy
# 0, 1, 2, 3 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# def solve(board, d):
#     new_board = copy.deepcopy(board)
#     if d ==0 or d==2:
#         stack = []
#         for i in range(N):
#             for j in range(N):
#                 if new_board[i][j]:
#                     tmp = new_board[i][j]
#                     col,raw = i+dx[d], j+dy[d]
#                     while 0<=col<N and 0<=raw<N:
#                         if new_board[col][raw] == 0:
#                             new_board[col][raw] = tmp
#                             new_board[col-dx[d]][raw-dy[d]] = 0
#                         elif new_board[col][raw] == tmp:
#                             stack.append((col,raw,2*tmp))
#                             new_board[col][raw] = '*'
#                             new_board[col-dx[d]][raw-dy[d]] = 0
#                             break
#                         else:
#                             break
#                         col, raw = col + dx[d], raw + dy[d]
#         for x,y,value in stack:
#             new_board[x][y] = value
#     else:
#         stack=[]
#         for i in range(N-1,-1,-1):
#             for j in range(N-1,-1,-1):
#                 if new_board[i][j]:
#                     tmp = new_board[i][j]
#                     col,raw = i+dx[d], j+dy[d]
#                     while 0<=col<N and 0<=raw<N:
#                         if new_board[col][raw] == 0:
#                             new_board[col][raw] = tmp
#                             new_board[col-dx[d]][raw-dy[d]] =0
#
#                         elif new_board[col][raw] == tmp:
#                             stack.append((col, raw, 2 * tmp))
#                             new_board[col][raw] = '*'
#                             new_board[col-dx[d]][raw-dy[d]] = 0
#                             break
#                         else:
#                             break
#                         col, raw = col + dx[d], raw + dy[d]
#         for x, y, value in stack:
#             new_board[x][y] = value
#     return new_board

def rotate(a):
    n = len(a)
    copy = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy[j][n - 1 - i] = a[i][j]
    return copy


def push(a):
    for i in range(N):
        for j in range(N):
            if a[i][j] == 0:
                a[i].insert(a[i].pop(j), 0)


def add(a):
    for i in range(N):
        for j in range(N - 1, 0, -1):
            if a[i][j] == a[i][j - 1]:
                a[i][j] *= 2
                a[i].pop(j - 1)
                a[i].insert(0, 0)


def mymax(a):
    mxtmp = 0
    for i in range(N):
        if mxtmp < max(a[i]):
            mxtmp = max(a[i])
    return mxtmp


def solve(S, board):
    if S == 1:
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
        board = rotate(board)
        board = rotate(board)
    elif S == 2:
        board = rotate(board)
        board = rotate(board)
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
    elif S == 3:
        board = rotate(board)
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
        board = rotate(board)
    else:
        push(board)
        add(board)
    return board​

def back(k, board, choice):
    global Max
    if k ==5:
        Max = max(max(map(max,board)),Max)
        print(Max, *choice)
    else:
        for i in range(4):
            choice.append(i)
            back(k+1, solve(board,i),choice)
            choice.pop()
Max = 0
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
back(0, board,[])
print(Max)
