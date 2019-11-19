import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    p = list(range(N+1))
    ans = N
    for _ in range(M):
        a,b = map(int,input().split())

    print(ans-1)