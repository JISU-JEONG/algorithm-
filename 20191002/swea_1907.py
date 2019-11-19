from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,0,-1,1,0,-1,1]


def bfs(sx,sy):
    visit[sx][sy]=1
    queue = deque()
    queue.append((sx,sy))
    while queue:
        x,y = queue.popleft()
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1):
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
                if castle[nx][ny] == '.':
                    queue.append((nx,ny))
                    visit[nx][ny] = 1
                else:
                    if (nx,ny) not in result and castle[i][j] !='9':
                        result.append((nx,ny))

N, M = map(int, input().split())
castle = [list(input()) for _ in range(N)]
time = 0

while True:
    result = []
    record = [[False] * M for _ in range(N)]
    flag = 0
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and castle[i][j]=='.':
                bfs(i,j)
    for i,j in result:
        if castle[i][j] != '.':
            cnt = 0
            for k in range(8):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<N and 0<=ny<M and castle[nx][ny]=='.':
                    cnt+=1
            if cnt>=int(castle[i][j]):
                record[i][j] = True
                flag = 1
    if not flag:
        break
    for i, j in result:
        if record[i][j]:
            castle[i][j] ='.'
    time += 1
print("{}".format(time))