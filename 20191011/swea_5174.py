def solve(S):
    global cnt
    cnt+=1
    for v in C[S]:
        solve(v)
    return

T = int(input())

for t in range(1, T+1):
    N, S = map(int,input().split())
    numbers = list(map(int,input().split()))
    C = [[] for _ in range(1002)]
    for i in range(N):
        C[numbers[2*i]].append(numbers[2*i+1])
    cnt = 0
    solve(S)
    print("#{} {}".format(t,cnt))