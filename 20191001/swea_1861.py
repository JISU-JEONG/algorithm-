dx = [0,0,-1,1]
dy = [1,-1,0,0]
def back(x,y,k,sx,sy):
    global Max, Min

    if Max <= k:
        if Max ==k:
            Min = min(Min, room[sx][sy])
        else:
            Min = room[sx][sy]
        Max = k
    if Max == N**2:
        return
    else:
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and room[nx][ny]-room[x][y]==1:
                back(nx,ny,k+1,sx,sy)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    Min = 0xffff
    for i in range(N):
        for j in range(N):
            back(i,j,1,i,j)
    print("#{} {} {}".format(t,Min, Max))