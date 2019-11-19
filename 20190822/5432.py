
T = int(input())
for t in range(1, T+1):
    bar = input()
    cnt = 0
    result = []
    for i in range(len(bar)):
        if bar[i] == '(':
            result.append(bar[i])
        else:
            result.pop()
            if bar[i - 1] == ')':
                cnt += 1
            else:
                cnt += len(result)
    print('#{} {}'.format(t, cnt))
