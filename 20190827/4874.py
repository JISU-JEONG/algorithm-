def calulation(a):
    num_list = []

    while a:
        cal = a.pop(0)
        if cal.isdigit():
            num_list.append(int(cal))
            continue
        if cal == '+':
            if len(num_list) < 2:
                return 'error'
            else:
                x = num_list.pop(-1)
                y = num_list.pop(-1)
                num_list.append(x + y)
        elif cal == '-':
            if len(num_list) < 2:
                return 'error'
            else:
                x = num_list.pop(-1)
                y = num_list.pop(-1)
                num_list.append(y - x)
        elif cal == '/':
            if len(num_list) < 2:
                return 'error'
            else:
                x = num_list.pop(-1)
                y = num_list.pop(-1)
                num_list.append(y // x)
        elif cal == '*':
            if len(num_list) < 2:
                return 'error'
            else:
                x = num_list.pop(-1)
                y = num_list.pop(-1)
                num_list.append(x * y)
        elif cal == '.':
            if len(num_list) != 1:
                return 'error'
            else:
                return num_list.pop()
        else:
            return 'error'

    return 'error'


T = int(input())

for test_case in range(1, T + 1):
    x = list(input().split())

    print('#{} {}'.format(test_case, calulation(x)))
