dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(start):
    visit[start[0]][start[1]] = 1
    queue = [start]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if 0<= nx <N and 0<= ny <N:
                if not visit[nx][ny] and board[nx][ny] != 1:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx,ny))
                    if nx==end[0] and ny == end[1]:
                        return visit[nx][ny]-2
    return 0
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    start, end =0, 0
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start = (i, j)
            if board[i][j] == 3:
                end =(i, j)
    result = bfs(start)

    print('#{} {}'.format(t, result))