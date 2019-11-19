import sys
def push(x):
    result.append(x)

def top():
    if result:
        print(result[-1])
    else:
        print(-1)

def size():
    print(len(result))

def empty():
    if result:
        print(0)
    else:
        print(1)
def pop2():
    if len(result) > 0:
        print(result.pop())
    else:
        print(-1)

result =[]

for _ in range(int(sys.stdin.readline())):
    string = list(sys.stdin.readline().split())

    if string[0] == 'push':
        push(int(string[1]))
    elif string[0] == 'top':
        top()
    elif string[0] == 'size':
        size()
    elif string[0] == 'empty':
        empty()
    elif string[0] == 'pop':
        pop2()
