from sys import *
setrecursionlimit(10 ** 6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    rain[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<= ny < N:
            if not rain[nx][ny] and board[nx][ny] <=H:
                dfs(nx, ny)

def dfs2(x, y):
    visit[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<= ny < N:
            if not visit[nx][ny] and not rain[nx][ny]:
                dfs2(nx, ny)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
Max = 0
height = 0
for i in range(N):
    for j in range(N):
        height = max(height, board[i][j])
for H in range(1, height):
    rain = [[0]*N for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] <=H and rain[i][j] == 0:
                dfs(i ,j)

    for i in range(N):
        for j in range(N):
            if not rain[i][j] and not visit[i][j]:
                cnt += 1
                dfs2(i,j)

    Max = max(Max, cnt)

print(Max)