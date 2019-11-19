def back(k, choice):
    global flag
    if sum(choice) > K:
        return
    if len(choice) == N and sum(choice) == K:
        flag += 1
        return
    else:
        for i in range(k, 13):
            if used[i] == 0:
                used[i] = 1
                choice.append(i)
                back(i + 1, choice)
                used[i] = 0
                choice.pop()

T = int(input())

numbers = list(range(1, 13))

for t in range(1, T + 1):
    used =[0]*13
    N, K = map(int, input().split())
    flag = 0
    back(1, [])
    print('#{} {}'.format(t, flag))