

T = int(input())

for t in range(1, T+1):
    N = int(input())
    dog = []
    for _ in range(N):
        dog.append(list(map(int, input().split())))
    dog.sort()
    dp = [1]*N
    for i in range(1,N):
        if dog[i-1][1] <= dog[i][0]:
            dp[i] = dp[i-1]+1
        else:
            for j in range(i-1,-1,-1):
                if dog[j][1] <= dog[i][0] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1

    print("#{} {}".format(t,max(dp)))