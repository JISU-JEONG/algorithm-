from queue import PriorityQueue
from collections import deque
def bfs(sx,sy):
    visit = [[0]*N for _ in range(N)]
    visit[sx][sy] = 1
    dq = deque()
    Q = PriorityQueue()
    dq.append((sx,sy))
    time = 0
    while dq:
        time+=1
        for _ in range(len(dq)):
            x,y = dq.popleft()
            for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
                nx, ny = x+dx,y+dy
                if 0<=nx<N and 0<=ny<N:
                    if not visit[nx][ny] and board[nx][ny]<=shark_size:
                        if 0< board[nx][ny] < shark_size:
                            Q.put((nx,ny))
                        else:
                            visit[nx][ny] = 1
                            dq.append((nx,ny))
        if not Q.empty():
            return Q.get(), time
    return (0,0),-1


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
shark_size = 2
shark_eat = 0
for i in range(N):
    for j in range(N):
        if board[i][j] ==9:
            board[i][j] = 0
            sharkx,sharky = i,j
            break
t = 0
while True:
    shark, pt = bfs(sharkx,sharky)
    if pt ==-1:
        break
    board[shark[0]][shark[1]] = 0
    shark_eat+=1
    if shark_size == shark_eat:
        shark_size+=1
        shark_eat=0
    sharkx,sharky = shark
    t+=pt
print(t)