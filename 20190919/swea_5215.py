
def back(k, p, c):
    global Max
    if c > L:
        return
    if k == N:
        Max = max(Max, p)
    else:
        back(k+1, p+point[k], c+cal[k])
        back(k + 1, p, c)

T = int(input())

for t in range(1, T+1):
    N, L = map(int, input().split())
    point = [0]*N
    cal = [0]*N
    Max = 0
    for i in range(N):
        point[i], cal[i] = map(int,input().split())

    back(0,0,0)

    print('#{} {}'.format(t,Max))