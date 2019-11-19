from collections import deque

def bfs():
    D = [[0xffff]*N for _ in range(N)]
    D[0][0] = 0
    Q = deque()
    Q.append((0,0))
    while Q:
        x,y = Q.popleft()
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx, ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                w = max(0,board[nx][ny]-board[x][y])+1
                if D[nx][ny] > D[x][y]+w:
                    D[nx][ny] = D[x][y]+w
                    Q.append((nx,ny))
    return D[N-1][N-1]

T = int(input())

for t in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    print("#{} {}".format(t,bfs()))