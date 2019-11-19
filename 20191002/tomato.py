import sys
from collections import deque
I = sys.stdin.readline
dz = [0, 0, 0, 0, 1, -1]
dx = [0, 0 ,1, -1, 0, 0]
dy = [1, -1 ,0, 0, 0, 0]

def limit_pos(z,x,y):
    if 0<=x<N and 0<=y<M and 0<= z < H:
        return 1
    else:
        return 0

def bfs():
    global cnt
    time = 0
    queue = deque()
    queue.extend(tomato)

    while queue:
        if cnt == 0:
            break
        time += 1
        for _ in range(len(queue)):
            z, x, y = queue.popleft()

            for i in range(6):
                if cnt == 0:
                    break
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if limit_pos(nz, nx,ny) and visited[nz][nx][ny] == 0 and board[nz][nx][ny] == 0:
                    board[nz][nx][ny] = 1
                    visited[nz][nx][ny] = 1
                    queue.append((nz,nx,ny))
                    cnt -= 1

    return time if cnt == 0 else -1


M, N, H = map(int, I().split())
board = [list(list(map(int, I().split())) for _ in range(N)) for _ in range(H)]
tomato = []
cnt = 0
visited = [list([0]*M for _ in range(N)) for _ in range(H)]

for h in range(H):
    for i in range(N):
        for j in range(M):
            if board[h][i][j] == 1:
                tomato.append((h, i,j))
                visited[h][i][j] = 1
            elif board[h][i][j] == 0:
                cnt += 1

result = bfs()

print(result)