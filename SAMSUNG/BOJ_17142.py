from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(start,cnt):
    visit = [[0] * N for _ in range(N)]
    queue=deque()
    for x, y in start:
        visit[x][y] = 1
        queue.append((x, y))
    time = 0
    while queue and cnt:
        time += 1
        for i in range(len(queue)):
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if not visit[nx][ny] and not board[nx][ny]:
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append((nx,ny))
                        cnt -= 1
                    elif not visit[nx][ny] and board[nx][ny] ==2:
                        visit[nx][ny] = visit[x][y]
                        queue.append((nx, ny))
    if cnt:
        return 0xfffff
    else:
        return time



def back(choice,k):
    global cnt, Min
    if len(choice) == M:
        start = []
        for c in choice:
            start.append(c)
        count =cnt
        result = bfs(start,count)
        Min = min(Min,result)
    else:
        for i in range(k,L):
            if not used[i]:
                used[i] = 1
                choice.append(virus[i])
                back(choice, i+1)
                choice.pop()
                used[i] = 0


N ,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
Min = 0xfffff
virus = []
for i in range(N):
    for j in range(N):
        if board[i][j]==2:
            virus.append((i, j))
        elif not board[i][j]:
            cnt += 1

L = len(virus)
used = [0]*L
back([], 0)

if Min == 0xfffff:
    print(-1)
else:
    print(Min)