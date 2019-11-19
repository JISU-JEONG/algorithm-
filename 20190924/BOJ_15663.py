
def back(choice):

    if len(choice) == M:
        print(*choice)
    else:
        for i in range(Min, Max + 1):
            if used[i] < cnt[i]:
                used[i]+=1
                choice.append(i)
                back(choice)
                used[i]-=1
                choice.pop()


N, M = map(int, input().split())
numbers = list(map(int,input().split()))
Max, Min = 0, 10000
cnt = [0]*10001
used = [0]*10001
for i in numbers:
    cnt[i] += 1
    Max = max(Max, i)
    Min = min(Min, i)

back([])

