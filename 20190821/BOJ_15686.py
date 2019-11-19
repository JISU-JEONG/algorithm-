def solution(choice, k):
    global Min_num

    if len(choice) == M:
        S = 0
        for hx,hy in home:
            distance = []
            for cx, cy in choice:
                distance.append(abs(cx-hx)+abs(cy-hy))
            S += min(distance)
        if S < Min_num:
             Min_num = S

    else:
        if L-k + len(choice) >= M:
            for i in range(k, L):
                if used[i] == 0:
                    used[i] = 1
                    choice.append(chicken[i])
                    solution(choice,i+1)
                    used[i] = 0
                    choice.pop()


N, M =map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []
Min_num = 1000000
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i, j))
        if board[i][j] == 2:
            chicken.append((i,j))

L = len(chicken)
used = [0]*L

solution([],0)
print(Min_num)