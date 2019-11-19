N = int(input())
switch = list(map(int, input().split()))

t = int(input())

for _ in range(t):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(number-1, N, number):
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1
    else:
        idx_min, idx_max = number-1, number
        for i in range(1, 51):
            if number-1-i < 0 or number-1+i == N or switch[number-1-i] != switch[number-1+i]:
                break
            idx_min, idx_max = number-1-i, number+i
        for i in range(idx_min, idx_max):
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1

for i in range(N//20+1):
    print(*switch[20*i:20*i+20])