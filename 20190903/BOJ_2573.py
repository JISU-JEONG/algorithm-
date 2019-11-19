from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    visit[x][y] = 1
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx,ny))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ice = dict()

for i in range(N):
    for j in range(M):
        if board[i][j]:
            ice[(i,j)] = board[i][j]
L = 1
time = 0
while L:
    time +=1
    new_ice=dict()
    for key, value in ice.items():
        x,y = key
        tmp = 0
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny <M:
                if not board[nx][ny]:
                    tmp += 1
        if value - tmp <0:
            value = 0
        else:
            value -= tmp
        new_ice[(x,y)] = value
    ice = dict()
    for key, value in new_ice.items():
        x, y = key
        board[x][y] = value
        if value:
            ice[key] = value
    visit = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
           if not visit[i][j] and board[i][j]:
                bfs(i,j)
                cnt+=1
    if cnt >=2:
        break
    L = len(ice)
if len(ice):
    print(time)
else:
    print(0)