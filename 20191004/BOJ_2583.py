
def bfs(sx, sy):
    global area
    area +=1
    visit[sx][sy] =1
    queue=[(sx,sy)]
    while queue:
        x,y = queue.pop(0)
        for dx,dy in (1,0),(-1,0),(0,-1),(0,1):
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if not visit[nx][ny] and not board[nx][ny]:
                    visit[nx][ny] =1
                    queue.append((nx,ny))
                    area+=1

N, M, T = map(int,input().split())
board = [[0]*M for _ in range(N)]
for _ in range(T):
    y1,x1,y2,x2 = map(int,input().split())

    for i in range(x1,x2):
        for j in range(y1, y2):
            board[i][j] = 1

cnt = 0
visit = [[0]*M for _ in range(N)]
result = []
for i in range(N):
    for j in range(M):
        if not board[i][j] and not visit[i][j]:
            area = 0
            bfs(i,j)
            cnt +=1
            result.append(area)
print(cnt)
print(*sorted(result))