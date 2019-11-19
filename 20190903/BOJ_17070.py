import sys
input = sys.stdin.readilne

dx = [0,1,1]
dy = [1,0,1]
def solution(x, y, d):
    if d == 0:
        nx,ny = x+dx[d],y+dy[d]
        if 0<=nx<N and 0<=ny<N:
            if not board[nx][ny]:
                return 1

    elif d == 1:
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if not board[nx][ny]:
                return 1
    else:
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny]:
                    return 0
            else:
                return 0
        return 1
    return 0
def pipvisit(x,y,d):
    if d == 0:
        board[x][y+1] = 1
        return x,y+1
    elif d ==1:
        board[x+1][y] = 1
        return x+1,y
    else:
        board[x][y+1] = 1
        board[x + 1][y] = 1
        board[x + 1][y+1] = 1
        return x+1,y+1
def pip_visit_return(x,y,d):
    if d == 0:
        board[x][y+1] = 0
        return
    elif d ==1:
        board[x+1][y] = 0
        return
    else:
        board[x][y+1] = 0
        board[x + 1][y] = 0
        board[x + 1][y+1] = 0
        return

def back(x, y, d):
    global cnt
    if x==N-1 and y==N-1:
        cnt += 1
    else:
        for i in direction[d]:
            if solution(x,y,i):
                nx,ny=pipvisit(x,y,i)
                back(nx,ny,i)
                pip_visit_return(x,y,i)


# 0: 가로 1: 세로 2: 대각선
N = int(input())
cnt = 0
direction = { 0: [0,2], 1: [1,2], 2: [0,1,2]}
board = [list(map(int, input().split())) for _ in range(N)]
board[0][0], board[0][1] = 1, 1
back(0, 1, 0)

print(cnt)
