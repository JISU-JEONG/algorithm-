
def back(k,choice):
    global result
    if sum(choice) > C:
        return
    if k==M:
        result = max(result,sum(map(lambda x:x**2, choice)))
    else:
        back(k+1,choice)
        choice.append(stack[k])
        back(k+1,choice)
        choice.pop()

def back2(k, idx):
    global Max
    if len(k)==2:
        if k[0][0] == k[1][0] and abs(k[0][1]-k[1][1])<=M-1:
            return
        Max = max(Max, dp[k[0][0]][k[0][1]]+dp[k[1][0]][k[1][1]])
    else:
        for i in range(idx, N*L):
            if not used[i]:
                used[i] = 1
                k.append((i//L, i%L))
                back2(k,i+1)
                used[i] = 0
                k.pop()


T = int(input())

for t in range(1,T+1):
    N, M, C = map(int,input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*(N-M+1) for _ in range(N)]
    L = N-M+1
    for i in range(N):
        for j in range(L):
            result = 0
            stack =[]
            for k in range(j,j+M):
                stack.append(honey[i][k])
            back(0,[])
            dp[i][j] = result
    used = [0]*(N*L)
    Max = 0
    back2([], 0)

    print("#{} {}".format(t,Max))