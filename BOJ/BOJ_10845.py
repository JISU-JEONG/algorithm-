from collections import deque
import sys

result = deque()

for _ in range(int(sys.stdin.readline())):
    pos = list(sys.stdin.readline().split())
    if pos[0] == 'push':
        result.append(pos[1])
    elif pos[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    elif pos[0] == 'size':
        print(len(result))
    elif pos[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif pos[0] == 'front':
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    else:
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])