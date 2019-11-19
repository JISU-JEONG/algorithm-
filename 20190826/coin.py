coin = [1, 4, 6]


def coinChange(n, choice):
    global Min
    if sum(choice) > n or len(choice) >= Min:
        return
    if sum(choice) == n:
        Min = min(Min, len(choice))
        print(*choice)
        return
    else:
        for i in range(2, -1, -1):
            choice.append(coin[i])
            coinChange(n, choice)
            choice.pop()


Min = 0xffffffff
coinChange(8, [])
print('결과 :', Min)
