def back(k, choice):
    if len(choice) == 3:
        print(*choice)
    else:
        for i in range(1, 6):
            if used[i] == 0:
                used[i] = 1
                choice.append(i)
                back(i+1, choice)
                used[i] = 0
                choice.pop()

used = [0] * 6
numbers = list(range(1, 6))
back(1, [])



# for i in range(N):
#   if used & (1<<i): continue
#   back(k+1,n,used | (1<<i))