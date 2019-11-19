

T = int(input())
for t in range(1, T+1):
    A,B=[],[]
    N = int(input())
    bus = [0]*5001
    for _ in range(N):
        a, b = map(int,input().split())
        for i in range(a,b+1):
            bus[i] +=1
    P = int(input())
    result = []
    print('#{} '.format(t), end='')
    for _ in range(P):
        result.append(bus[int(input())])
    print(*result)