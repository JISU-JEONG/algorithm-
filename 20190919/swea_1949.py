import copy

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def back(x, y, k, c_b, f):
    global M_num
    if M_num < k:
        M_num = k

    for i in range(4):
        nx, ny = x+dx[i], y +dy[i]
        if 0<=nx<N and 0<=ny<N  and not visit[nx][ny]:
            if c_b[nx][ny] < c_b[x][y]:
                visit[nx][ny] = 1
                back(nx,ny,k+1,c_b, f)
                visit[nx][ny] = 0
            elif c_b[nx][ny]-K < c_b[x][y] and f==0:
                c_b[nx][ny] = c_b[x][y]-1
                visit[nx][ny] = 1
                back(nx, ny, k + 1, c_b, 1)
                visit[nx][ny] = 0
                c_b[nx][ny] = board[nx][ny]



T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    Max = max(map(max, board))
    M_num = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] ==Max:
                visit = [[0]*N for _ in range(N)]
                c_b = copy.deepcopy(board)
                visit[i][j] =1
                back(i, j, 1, c_b, 0)
    print("#{} {}".format(t,M_num))