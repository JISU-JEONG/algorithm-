
def back(cur, charge, res):
    global result
    if res > result:
        return
    if cur > data[0] - 1:
        return
    if charge + cur >= data[0]:
        if result > res:
            result = res
        return
    else:
        back(cur + 1, charge + data[cur] - 1, res + 1)
        if charge > 0:
            back(cur + 1, charge - 1, res)


T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    result = 10 ** 6
    back(2, data[1] - 1, 0)
    print('#{} {}'.format(tc, result))



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


def bus_charge(x, choice, used, N, distance, rotation):
    global min_num

    if distance >= N:
        if min_num > len(choice):
            min_num = len(choice)
    if len(choice) < min_num:
        for i in range(rotation, distance + 1):
            if used[i] == 0:
                used[i] = 1
                distance += x[i]
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
    print('#{} {}'.format(test_case, min_num - 1))