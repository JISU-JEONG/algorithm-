from collections import deque

N, K = map(int, input().split())
result = []
numbers = deque(x for x in range(1, N+1))

while numbers:
    for _ in range(K-1):
        numbers.append(numbers.popleft())
    result.append(numbers.popleft())


print('<{}>'.format(', '.join(map(str, result))))