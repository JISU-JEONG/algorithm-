water = list[map(int, input().split())]
find = 1
while find:
    if i in range(2):
        for j in range(i+1,3):
            if i==j: continue
            if water[i] == water[j]:
                find = 0
                break
    Max = max(water)
    