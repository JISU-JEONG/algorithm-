def pair(string):
    stack = []
    for ch in string:
        if ch == '(' or ch == '{':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0:
                return 0
            if stack.pop() != '(':
                return 0
        elif ch == '}':
            if len(stack) == 0:
                return 0
            if stack.pop() != '{':
                return 0
    if len(stack):
        return 0

    return 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    print('#{} {}'.format(test_case, pair(string)))




