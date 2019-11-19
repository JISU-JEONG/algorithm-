
coins = [6,4,1]
N = 5967
dp = [0]*(N+1)

def coin_change(N):
    if N == 0: return 0
    if dp[N]:
        return dp[N]
    Min = 0xffff
    for i in range(3):
        if N-coins[i] >=0:
            Min = min(Min,coin_change(N-coins[i]) + 1)
    dp[N] = Min
    return dp[N]

result = coin_change(N)
print(result)