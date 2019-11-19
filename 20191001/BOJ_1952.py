
T = int(input())

for t in range(1,T+1):
    D, M, M3, Y = list(map(int,input().split()))
    day = [0]+list(map(int,input().split()))
    dp = [0]*13
    for i in range(1, 13):
        dp[i] = min(M,day[i]*D)+dp[i-1]
        if i>2:
            dp[i] = min(dp[i-3]+M3,dp[i])
    dp[12] = dp[12] if Y>dp[12] else Y
    print("#{} {}".format(t,dp[12]))
