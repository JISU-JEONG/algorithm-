visit = [0]*6
G = [
    [],
    [2,3],
    [4],
    [],
    [1,5],
    [2]
]
D = [[0]*6 for _ in range(6)]
D[1][2] = 1
D[1][3] = 2
D[2][4] = 2
D[4][1] = 1
D[4][5] = 3
D[5][2] = 1
def find_cycle(x,k):
    if visit[x]:
        if visit[x]==-1:
            return True
        return False

    visit[x] = -1
    for v in G[x]:
        if find_cycle(v,k):
            return True
    visit[x] = 1

    return False
for i in range(1,6):
    print(find_cycle(i, 0))