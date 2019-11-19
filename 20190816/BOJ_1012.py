import sys
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, k):
    visited[x][y] = 1
    farm[x][y] = k

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < M and visited[nx][ny] == 0 and farm[nx][ny]==1:
            farm[nx][ny] = k
            bfs(nx, ny, k)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    k = 2
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and farm[i][j] == 1:
                bfs(i, j, k)
                cnt += 1
                k+=1

    print(cnt)