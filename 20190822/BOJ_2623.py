N, M = map(int, input().split())

PD = [[] for _ in range(N+1)]

for i in range(M):
    singer = list(map(int, input().split()))
    for j in range(1, len(singer)-1):
        PD[singer[j]].append(singer[j])

    for i in range(len(PD)):
        PD[i] = list(set(PD[i]))

print(PD)
