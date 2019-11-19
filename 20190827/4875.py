def dfs(a, start, end):
    visited = []
    queue=[start]
    N = len(a)
    while queue:
        p = queue.pop(0)
        if p == end:
            return 1
        for i in range(4):
            next = xy_move(p, i)
            if limit_xy(next, N) and a[next[0]][next[1]] != '1':
                if next not in visited:
                    visited.append(p)
                    queue.append(next)

    return 0

def limit_xy(xy, N):
    if 0<= xy[0] < N and 0<= xy[1] < N:
        return 1
    else:
        return 0

def xy_move(xy, d):
    if d == 0:
        return xy[0]+1,xy[1]
    elif d == 1:
        return xy[0] - 1, xy[1]
    elif d == 2:
        return xy[0], xy[1] + 1
    else:
        return xy[0], xy[1] - 1



T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    map_list = [list(input()) for _ in range(N)]
    S = ()
    G = ()
    for i in range(N):
        for j in range(N):
            if S and G:
                break
            if map_list[i][j] == '3':
                G = (i, j)
                continue
            if map_list[i][j] == '2':
                S = (i, j)

    print('#{} {}'.format(test_case, dfs(map_list, S, G)))
