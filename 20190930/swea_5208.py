def bus_charge(x, choice, used, N, distance, rotation):
    global min_num

    if distance >= (N-1):
        if min_num > len(choice):
            min_num = len(choice)
    if len(choice) < min_num:
        for i in range(rotation, distance+1):
            if used[i] == 0:
                used[i] = 1
                distance = x[i] + i
                choice.append(x[i])
                bus_charge(x, choice, used, N, distance, i)
                used[i] = 0
                distance -= x[i]
                choice.pop()


T = int(input())

for test_case in range(1, T + 1):
    min_num = 10000
    x = list(map(int, input().split()))
    x.append(0)
    N = x.pop(0)
    bus_charge(x, [], [0] * N, N, 0, 0)
    print('#{} {}'.format(test_case, min_num-1))