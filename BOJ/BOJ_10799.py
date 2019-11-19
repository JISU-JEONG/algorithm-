bar = input()

S = 0
steal =[]

for i in range(len(bar)):

    if bar[i] == '(':
        steal.append(bar[i])
    else:
        steal.pop()
        if bar[i-1] == '(':
            S += len(steal)
        else:
            S += 1

print(S)
