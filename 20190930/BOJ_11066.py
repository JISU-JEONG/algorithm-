import sys,pprint
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    books = list(map(int, input().split()))
    dp = [[0]*N for _ in range(N)]
    for i in range(N-2,-1,-1):
        for j in range(i,N):
            if i==j:continue
            else:
                S, Min = 0, 0xffff
                for k in range(i,j+1):
                    S += books[k]
                for k in range(i, j):
                    Min = min(Min, dp[i][k]+dp[k+1][j]+S)
                dp[i][j] = Min
    pprint.pprint(dp)
    print(dp[0][N-1] if dp[0][N-1] else books[0])