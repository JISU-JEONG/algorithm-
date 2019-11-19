import sys

sys.stdin = open('input.txt', 'r')


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

    return num_list.pop()

for t in range(1, 10):
    N = int(input())
    string = input()
    pm = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
    stack = []
    numbers = []

    for ch in string:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                numbers.append(stack.pop())
            stack.pop()
        else:
            if ch.isdigit():
                numbers.append(ch)
            else:
                if stack[-1] != '(' and pm[stack[-1]] >= pm[ch]:
                    numbers.append(stack.pop())
                stack.append(ch)

    print('#{} {}'.format(t, calulation(numbers)))