
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1,1,1,2,2]+[0]*100
    for i in range(3,N):
        dp[i] = dp[i-2]+dp[i-3]
    print(dp[N-1])