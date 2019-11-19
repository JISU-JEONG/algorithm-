dx = [0,0,1,-1]
dy = [1,-1,0,0]


def back(s, k, x, y):
    global Max
    if k ==4:
        Max = max(s, Max)
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not used[nx][ny]:
                    used[nx][ny] = 1
                    back(s+board[nx][ny], k+1, nx,ny)
                    used[nx][ny] = 0
def T_solution():

    s1,s2,s3,s4 = 0,0,0,0
    for i in range(N-2):
        for j in range(M-1):
            s1 = max(board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j+1],s1)
            s2 = max(board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+1][j],s2)
    for i in range(N-1):
        for j in range(M-2):
            s3 = max(board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+1],s3)
            s4 = max(board[i][j+1]+ board[i+1][j]+board[i+1][j+1]+board[i+1][j+2],s4)

    return max(s1,s2,s3,s4)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
used = [[0]*M for _ in range(N)]
Max = 0
for i in range(N):
    for j in range(M):
        back(board[i][j], 1,i,j)
Max = max(Max,T_solution())

print(Max)

