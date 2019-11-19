
N = int(input())

used = [list(range(1,i+3)) for i in range(14)]
number = [1]*14
for i in range(14):
    for n in used[i]:
        number[i] *=n
for _ in range(N):
    ans = min(number)
    for i in range(14):
        if number[i] == ans:
            number[i] //=used[i][0]
            used[i].pop(0)
            used[i].append(used[i][-1]+1)
            number[i] *= used[i][-1]

print(ans)
