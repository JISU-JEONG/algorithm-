from collections import deque

N = int(input())

numbers = deque(x for x in range(1, N+1))

while len(numbers) != 1:
    numbers.popleft()
    numbers.append(numbers.popleft())

print(numbers[0])