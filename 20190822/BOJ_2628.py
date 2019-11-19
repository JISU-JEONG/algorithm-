import sys
input = sys.stdin.readline

N, M = map(int, input().split())

G1 = [0, N]
G2 = [0, M]

T = int(input())
for _ in range(T):
    d, num = map(int, input().split())
    if d == 0:
        G2.append(num)
    else:
        G1.append(num)
max_n = 0
G1.sort()
G2.sort()

for i in range(len(G1)-1):
    for j in range(len(G2)-1):
        area = (G1[i+1]-G1[i])*(G2[j+1]-G2[j])
        max_n = max(max_n, area)
print(max_n)