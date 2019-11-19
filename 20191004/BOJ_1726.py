from collections import deque

dx = [0, 0,0,1,-1]
dy = [0, 1,-1,0,0]
# [1,2,3,4]  동 서 남 북
LR = [{1:4, 4:2, 2:3, 3:1},{4:1, 2:4, 3:2, 1:3}]

def bfs(sx,sy,sd):
    visit[sd][sx][sy] = 1
    dq = deque()
    dq.append((sd,sx,sy))
    if sd == ed and ey == sy and ex == sx:
        return visit[sd][sx][sy]
    while dq:
        dir, x, y = dq.popleft()
        for i in range(1,4):
            flag = 0
            nx,ny = x+dx[dir]*i,y+dy[dir]*i
            if 0<=nx<N and 0<=ny<M:
                if not visit[dir][nx][ny]:
                    for k in range(i):
                        if board[nx-dx[dir]*k][ny-dy[dir]*k] == 1: flag = 1
                    if flag==1:continue
                    visit[dir][nx][ny] = visit[dir][x][y]+1
                    if dir == ed and ey ==ny and ex ==nx:
                        return visit[dir][nx][ny]
                    dq.append((dir,nx,ny))

        for i in range(2):
            nd = LR[i][dir]
            if not visit[nd][x][y]:
                visit[nd][x][y] = visit[dir][x][y] + 1
                if nd == ed and ey == y and ex == x:
                    return visit[nd][x][y]
                dq.append((nd, x, y))
    return 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
sx,sy,ex,ey = sx-1,sy-1,ex-1,ey-1
visit = [[[0]*M for _ in range(N)] for _ in range(5)]
result = bfs(sx,sy,sd)
print(result-1)