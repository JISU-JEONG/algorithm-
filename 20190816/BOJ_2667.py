dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, k):
    global cnt
    visited[x][y] = 1
    cnt += 1
    home[x][y] = k

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0 and home[nx][ny]:
            bfs(nx, ny, k)

    return cnt


N = int(input())
home = [list(map(int, input())) for _ in  range(N)]
visited = [[0]*N for _ in range(N)]
k = 2
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and home[i][j] == 1:
            cnt = bfs(i, j, k)
            result.append(cnt)
            k+=1
            cnt = 0
result.sort()

print(len(result))
for num in result:
    print(num)