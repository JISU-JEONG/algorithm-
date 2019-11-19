
dx = [1,-1,0,0]
dy = [0,0,1,-1]

T = int(input())

for t in range(1,T+1):
    N = int(input())

    room = [list(map(int,input().split())) for _ in range(N)]
    dp = [1]*(N**2+1)
    p = [0]*(N**2+1)
    for i in range(N):
        for j in range(N):
            p[room[i][j]] = (i,j)

    for i in range(2, N**2+1):
        for k in range(4):
            nx,ny = p[i][0]+dx[k],p[i][1]+dy[k]
            if 0<=nx<N and 0<=ny<N:
                if i - room[nx][ny] ==1:
                    dp[i] = dp[i-1]+1
                    break
    r = max(dp)
    print("#{} {} {}".format(t,dp.index(r)-r+1,r))