


T = int(input())

for t in range(1, T+1):
    station = list(map(int,input().split()))
    N = station.pop(0)
    station.append(0)
    L = len(station)
    dp = [[0xffff]*L for _ in range(2)]
    dp[0][0] = 0
    dp[1][0] = 0
    oil = [[0]*L for _ in range(2)]
    oil[1][0] = station[0]
    for i in range(1, L):
        if oil[0][i] >=i and oil[1][i] >=i:
            dp[1][i] = min(dp[0][i-1]+1, dp[1][i-1]+1)
            
        if oil[0][i] >=i:
            dp[1][i] = min(dp[0][i-1]+1, dp[1][i])
            oil[1][i] = station[i]
        if oil[1][i] >=i:
            dp[1][i] = min(dp[1][i - 1]+1, dp[1][i])
            oil[1][i] = station[i]
