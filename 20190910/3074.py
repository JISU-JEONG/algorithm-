

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    used =[]
    for _ in range(N):
        used.append(int(input()))
    people = 0
    time = 0
    while people<M:
        time+=1
        for i in range(N):
            if time%used[i] == 0:
                people += 1

    print('#{} {}'.format(t, time))

