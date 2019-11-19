
N, M = map(int, input().split())
money = []

for _ in range(N):
    money.append(int(input()))
cnt = 0
for i in range(N-1,-1,-1):
    cnt += M//money[i]
    M = M%money[i]
print(cnt)