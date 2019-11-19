from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y,fish):
    visit = [[0]*N for _ in range(N)]
    visit[x][y] = 1
    queue = deque()
    queue.append((x,y))
    start = (x,y)
    time = 0
    cnt = 0
    while queue and fish:
        stack = []
        cnt+=1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if not visit[nx][ny] and not board[nx][ny] or board[nx][ny] == shark[1]:
                        visit[nx][ny] = visit[x][y]+1
                        queue.append((nx,ny))
                    elif not visit[nx][ny] and 0< board[nx][ny] < shark[1]:
                        visit[nx][ny] = 1
                        stack.append((nx, ny))
        if len(stack)>0:
            stack.sort()
            board[start[0]][start[1]] = 0
            fish -= 1
            shark[2] += 1
            if shark[2] == shark[1]:
                shark[1]+= 1
                shark[2] = 0
            time += cnt
            cnt = 0
            queue = deque()
            queue.append((stack[0][0], stack[0][1]))
            visit = [[0] * N for _ in range(N)]
            start = (stack[0][0],stack[0][1])
            visit[stack[0][0]][stack[0][1]] = 1

    return time


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
shark = [0]*3
fish = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark[0] = (i,j)
            shark[1] = 2
            shark[2] = 0
        elif board[i][j]:
            fish += 1
x,y =  shark[0]
result = bfs(x,y,fish)

print(result)