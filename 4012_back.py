def back(k, c1, c2):
    global MIN_N

    if len(c1) > N//2 or len(c2) > N//2 or k>len(c1)+len(c2):
        return

    if k == N and len(c1) == N//2 == len(c2):
        S1, S2 = 0, 0
        for i in range(len(c1)):
            for j in range(len(c1)):
                if i != j:
                    S1 += cook[c1[i]][c1[j]]
                    S2 += cook[c2[i]][c2[j]]
        if MIN_N > abs(S1 - S2):
            MIN_N = abs(S1 - S2)

    else:
        for i in range(k, N):
            c1.append(i)
            back(i+1, c1, c2)
            c1.pop()
            c2.append(i)
            back(i+1, c1, c2)
            c2.pop()




T = int(input())

for t in range(T):
    MIN_N = 0xFFFF
    N = int(input())
    cook = [list(map(int, input().split())) for _ in range(N)]

    back(0, [], [])
    print('#{} {}'.format(t + 1, MIN_N))