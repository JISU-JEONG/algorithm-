
def back(choice, s, k):
    global Min
    if s >= Min:
        return
    if len(choice) == N:
        s += board[choice[-1]][choice[0]]
        Min = min(s, Min)
    else:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                if k >0:
                    back(choice, s+ board[choice[k-1]][choice[k]], k+1)
                else:
                    back(choice, s, k + 1)
                choice.pop()
                used[i] = 0

T = int(input())

for t in range(1, T+1):
    N = int(input())
    Min = 0xffff
    board = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*N
    back([], 0, 0)
    print('#{} {}'.format(t,Min))