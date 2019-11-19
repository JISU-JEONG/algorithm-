
def back(s, k):
    global Max
    if k >= N:
        Max = max(Max, s)
        return
    else:
        used[k] = 1
        if k+T[k] <= N:
            back(s+P[k],k+T[k])
        used[k] = 0
        back(s, k+1)

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
used = [0]*N
Max = 0
back(0,0)
print(Max)