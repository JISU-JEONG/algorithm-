T = int(input())

for t in range(1, T+1):
    N = int(input())
    cnt = 0
    room = []

    for i in range(N):
        a, b = map(int, input().split())
        a, b = min(a,b), max(a,b)
        room.append((a,b))
    room.sort()
    while room:
        go = []
        stay = []
        cnt += 1
        for _ in range(len(room)):
            a, b = room.pop(0)
            if not a & 1:
                a = a-1
            if not b & 1:
                b += 1
            if len(go) == 0:
                go.append(a)
                go.append(b)
            elif a > go[-1]:
                go.append(a)
                go.append(b)
            else:
                stay.append((a,b))
        room = stay

    print('#{} {}'.format(t, cnt))
