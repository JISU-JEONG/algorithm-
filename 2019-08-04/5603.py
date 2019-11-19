T = int(input())

for test in range(1, T+1):
    N = int(input())
    S = 0
    numbers=[]
    for i in range(N):
        x = int(input())
        numbers.append(x)
        S += x

    Avg = S//N
    result = 0

    for number in numbers:
        if number-Avg > 0:
            result += number-Avg

    print('#{} {}'.format(test,result))
