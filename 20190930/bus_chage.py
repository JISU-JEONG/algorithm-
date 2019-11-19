

def back(p, oil, charge):
    global Min
    if p+oil>=N:
        Min






T = int(input())

for t in range(1, T+1):
    station = list(map(int, input().split()))+[0]
    N = station[0]
    station[0] = 0

    back(1, station[1], 0)