import sys

N = int(sys.stdin.readline())

numbers = []
cmp = []
pm =[]
k = 0
for _ in range(N):
    cmp.append(int(sys.stdin.readline()))

for i in range(1, N+1):
    numbers.append(i)
    pm.append('+')
    while numbers[-1] == cmp[k] and k < N:
        numbers.pop()
        pm.append('-')
        k += 1
        if len(numbers) == 0:
            break

if len(numbers):
    print('NO')
else:
    for ch in pm:
        print(ch)



