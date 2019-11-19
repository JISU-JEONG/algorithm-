from collections import deque


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    oven = deque()
    for i in range(1, N+1):
        oven.append([C.pop(0),i])
    k = N+1
    while len(oven) != 1:
        if len(oven) == 1:
                break
        if oven[0][0] == 0:
            oven.popleft()
            if len(C):
                oven.appendleft([C.pop(0),k])
                k += 1
        else:
            oven[0][0] = oven[0][0]//2
            oven.append(oven.popleft())


    print('#{} {}'.format(t, oven[0][1]))
