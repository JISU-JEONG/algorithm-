dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def pos_limit(x,y):
    if 0<= x <N and 0<= y < M:
        return 1
    else:
        return 0


def bfs():
    visited[0][0] = 1
    queue=[(0,0)]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if pos_limit(nx, ny) and not visited[nx][ny] and labin[nx][ny] ==1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))



N, M = map(int, input().split())

labin = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

bfs()

print(visited[N-1][M-1])
