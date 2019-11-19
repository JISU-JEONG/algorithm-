import sys
from itertools import combinations
from collections import deque

dxy = [(1,0),(-1,0),(0,1),(0,-1)]

def limitpos(x,y):
    if 0<=x<N and 0<=y<N:
        return 1
    else:
        return 0


def soulution(k, choice):

    global Max
    # if len(choice) == M:
    com = list(combinations(virus, M))
    for choice in com:
        x = bfs(choice)
        if x < Max:
            if x!= -1:
                Max = x
    return
    # else:
    #     for i in range(k, L):
    #         if used[i] == 0:
    #             used[i] = 1
    #             choice.append(virus[i])
    #             soulution(i+1, choice)
    #             used[i] = 0
    #             choice.pop()

def bfs(choice):
    global cnt

    clab = [[0]*N for _ in range(N)]
    start = deque()
    visited = [[0]*N for _ in range(N)]
    start += choice


    for l in choice:
        clab[l[0]][l[1]] = 1
        visited[l[0]][l[1]] = 1
    times = 1
    infect = 0

    while start:
        if infect == cnt:
            return times
        if times > Max:
            return -1
        x, y = start.popleft()
        for i in range(4):
            n_x,n_y = x + dxy[i][0], y + dxy[i][1]
            if limitpos(n_x, n_y) and not visited[n_x][n_y] and lab[n_x][n_y]!= -1:
                clab[n_x][n_y] = clab[x][y]+1
                start.append((n_x, n_y))
                visited[n_x][n_y] = 1
                if clab[n_x][n_y] > Max:
                    return -1
                if lab[n_x][n_y] == 0:
                    times = clab[n_x][n_y]
                    infect += 1

    if infect == cnt:
        return times

    return -1



N, M = map(int, sys.stdin.readline().split())
cnt = 0
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
virus = []
Max = 100000
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
            lab[i][j] = '*'
        elif lab[i][j] == 1:
            lab[i][j] = -1
        else:
            cnt+=1
L = len(virus)
used = [0]*L

soulution(0, [])

if Max == 100000:
    Max = 0

print(Max-1)