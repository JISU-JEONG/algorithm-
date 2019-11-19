import sys
sys.setrecursionlimit(10 ** 6)
# 치즈 오픈된 부분의 구멍까지 작성완료
dx = [0,0,1,-1]
dy = [-1,1,0,0]

def dfs(x,y):
    open[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not open[nx][ny] and not board[nx][ny]:
                dfs(nx,ny)

def findcheese(x,y):

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<= nx < N and 0<= ny < M:
            if not visit[nx][ny] and board[nx][ny]:
                result.append((nx,ny))
                visit[nx][ny] =1

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
tmp = 0
time =0
while True:
    visit = [[0] * M for _ in range(N)]
    open = [[0] * M for _ in range(N)]
    cnt = 0
    result = []
    for i in range(N):
        for j in range(M):
            if i==0 or j == 0 or i == N-1 or j == M-1 and not open[i][j]:
                dfs(i,j)

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
            if not board[i][j] and open[i][j]:
                findcheese(i,j)

    if cnt == 0:
        print(time)
        print(tmp)
        break
    tmp = cnt
    for x, y in result:
        board[x][y] = 0
    time += 1


