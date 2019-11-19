

N = int(input())
stack = []
for _ in range(N):
    stack.append(tuple(map(int, input().split())))
stack.sort()
dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if stack[j][1] < stack[i][1] and stack[j][0] < stack[i][0] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(len(stack)-max(dp))