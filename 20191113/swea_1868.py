import pprint

dxy = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def solve(x,y,k):
    queue = [(x,y)]
    visit[x][y] = k
    cnt=1
    while queue:
        x,y = queue.pop(0)
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != '*':
                if visit[nx][ny] !=k and dp[nx][ny]!='*':
                    visit[nx][ny] = k
                    if dp[nx][ny]==0:
                        cnt+=1
                        queue.append((nx,ny))
    return cnt


T = int(input())

for t in range(1,T+1):
    N = int(input())
    board = [input() for _ in range(N)]
    dp = [[0]*N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    Min = 0xffff
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                dp[i][j] = '*'
                visit[i][j] = 1
                for dx,dy in dxy:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<N and 0<=ny<N and board[nx][ny]!='*':
                        dp[nx][ny] +=1
    cnt = 0
    zero = []
    for i in range(N):
        for j in range(N):
            if dp[i][j]==0:
                zero.append((i,j))
                cnt+=1
    L = len(zero)
    click=0
    for i in range(L):
        if cnt==0:break
        x, y = zero[i][0], zero[i][1]
        if not visit[x][y]:
            k = solve(x, y, 1)
            cnt -= k
            click+=1
    Min = min(Min, click + N ** 2 - sum(map(sum, visit)))
    print("#{} {}".format(t,Min))