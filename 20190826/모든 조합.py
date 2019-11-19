def back(k, choice, cnt):
    if cnt == 5:
        print(choice)
    else:
        for i in range(k,6):
            if used[i] == 0:
                used[i] = 1
                choice.append(i)
                back(i + 1, choice,cnt+1)
                used[i] = 0
                choice.pop()
                back(i + 1, choice,cnt+1)

used = [0]*6
numbers = list(range(1, 6))
back(1, [], 0)