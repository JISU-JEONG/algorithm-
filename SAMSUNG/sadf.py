from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    visit = [[0]*N for _ in range(N)]
    visit[x][y] = 1
    queue = deque()
    queue.append((x,y))
    while queue:
        stack = []
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if not visit[nx][ny] and (not board[nx][ny] or board[nx][ny] == shark[1]):
                        visit[nx][ny] = visit[x][y]+1
                        queue.append((nx,ny))
                    elif not visit[nx][ny] and 0< board[nx][ny] < shark[1]:
                        visit[nx][ny] = 1
                        stack.append((nx, ny, visit[x][y]))
        if len(stack)>0:
            break
    return stack


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
shark = [0]*3
fish = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark[0] = [i,j]
            shark[1] = 2
            shark[2] = 0
        elif board[i][j]:
            fish += 1
time = 0
while fish:
    x, y = shark[0]
    result = bfs(x,y)
    if result:
        result.sort()
        board[x][y] = 0
        shark[2] += 1
        fish -= 1
        if shark[2] == shark[1]:
            shark[2] = 0
            shark[1] += 1

        nx, ny, cnt = result[0]
        board[nx][ny] = 9
        shark[0] = [nx, ny]
    else:
        break
    time += cnt
print(time)