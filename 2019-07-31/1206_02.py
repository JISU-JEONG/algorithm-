import sys
sys.stdin = open('input.txt', 'r')
for t in range(1, 11):
    N = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(2, N-4):
        m = max(a[i-2], a[i-1], a[i+1], a[i+2])
        c = c if a[i] <= m else c +(a[i]-m)
    print('#{} {}'.format(t, c))




