from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def limit(x, y):
    if 0 <= x < N and 0 <= y < M:
        return 1
    else:
        return 0

def bfs():
    visited[0][0][0] = 1
    queue = deque([(0,0,0)])

    while queue:
        z, x, y = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[z][x][y]
        for i in range(4):

            nx, ny = x + dx[i], y + dy[i]

1            if limit(nx,ny) and visited[z][nx][ny] == 0 and board[nx][ny] == 0:
                visited[z][nx][ny] = visited[z][x][y] + 1
                queue.append((z,nx,ny))
            if limit(nx, ny) and z == 0 and visited[1][nx][ny] == 0 and  board[nx][ny]:
                visited[1][nx][ny] = visited[z][x][y] + 1
                queue.append((1,nx,ny))

    return -1


N, M = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]
result = bfs()
print(result)


