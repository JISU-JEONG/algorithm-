def back(k, s):
    if k == N:
        return
    else:
        if not visit[k][s]:
            visit[k][s] = 1
            back(k+1,s)
        if not visit[k][s+numbers[k]]:
            visit[k][s + numbers[k]] = 1
            back(k+1, s + numbers[k])

T = int(input())

for t in range(1,T+1):
    N =int(input())
    numbers = list(map(int, input().split()))
    visit = [[0] * (sum(numbers) + 1) for _ in range(N)]
    back(0,0)
    print("#{} {}".format(t, sum(visit[N-1])))