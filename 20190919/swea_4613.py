
def find(x):
    S1, Min = 0, 0xffff
    for i in range(x):
        S1 += M-cnt[i]['W']
    for i in range(1,N-x):
        S2, S3 = 0, 0
        for j in range(x, x+i):
            S2 += M - cnt[j]['B']
        for j in range(x+i,N):
            S3 += M - cnt[j]['R']
        Min = min(S1+S2+S3, Min)
    return Min

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    cnt = [{'W':0, 'R':0, 'B':0} for _ in range(N)]
    flag = [input() for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(M):
            cnt[i][flag[i][j]] += 1

    for i in range(1, N-1):
        result.append(find(i))
    print("#{} {}".format(t,min(result)))