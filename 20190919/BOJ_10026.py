N = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(sx, sy):
    visit1[sx][sy] = 1
    queue=[(sx,sy)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visit1[nx][ny] and board[nx][ny] == board[x][y]:
                    visit1[nx][ny] =1
                    queue.append((nx,ny))
def bfs2(color,sx, sy):
    visit2[sx][sy] = 1
    queue=[(sx,sy)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visit2[nx][ny] and board[nx][ny] in color:
                    visit2[nx][ny] =1
                    queue.append((nx,ny))

board = [input() for _ in range(N)]
visit1 = [[0]*N for _ in range(N)]
visit2 = [[0]*N for _ in range(N)]
cnt1,cnt2 = 0, 0
for i in range(N):
    for j in range(N):
        if not visit1[i][j]:
            cnt1 += 1
            bfs(i, j)
        if not visit2[i][j]:
            cnt2 += 1
            if board[i][j] == 'B':
                bfs2(['B'],i, j)
            else:
                bfs2(['G','R'],i, j)
print(cnt1, cnt2)