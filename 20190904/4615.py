dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,1,-1,-1, 1,-1,1]
def solution(x,y,stone):
    board[x][y] = stone
    for i in range(8):
        nx,ny = x+dx[i],y+dy[i]
        while 0<=nx<N and 0<=ny<N:
            if board[nx][ny] ==0:
                nx, ny = nx - dx[i], ny - dy[i]
                while nx != x or ny != y:
                    board[nx][ny] = r[stone]
                    nx, ny = nx - dx[i], ny - dy[i]
                break
            elif board[nx][ny] == stone:
                break
            else:
                board[nx][ny] = stone
            nx, ny = nx + dx[i], ny + dy[i]
            if nx<0 or N <=nx or ny<0 or N <=ny:
                nx, ny = nx - dx[i], ny - dy[i]
                while nx != x or ny != y:
                    board[nx][ny] = r[stone]
                    nx, ny = nx - dx[i], ny - dy[i]
                break
T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    r = {1:2,2:1}
    board[N//2][N//2] = 2
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2] = 1
    board[N//2-1][N//2-1] = 2
    for _ in range(M):
        x, y, stone = map(int, input().split())
        solution(x-1,y-1,stone)
    cnt1,cnt2 = 0,0
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                cnt1+=1
            if board[i][j]==2:
                cnt2+=1
    print('#{} {} {}'.format(t,cnt1,cnt2))