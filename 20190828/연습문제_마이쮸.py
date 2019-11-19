queue = []
michu = 20
i = 1
while michu:
    queue.append([i, 0])
    for _ in range(len(queue)):
        if michu ==0: break
        tmp = queue.pop(0)
        tmp[1] += 1
        michu -= 1
        queue.append(tmp)
    i +=1

print(queue[-1][1])