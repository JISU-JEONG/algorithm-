def stringremove(a):
    result = []
    for ch in a:
        if len(result) == 0:
            result.append(ch)
        elif ch == result[-1]:
            result.pop()
        else:
            result.append(ch)
    return len(result)


T = int(input())

for test_case in range(1, T+1):
    print('#{} {}'.format(test_case, stringremove(input())))