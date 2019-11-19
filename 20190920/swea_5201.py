







T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    S = 0
    idx=0
    c = 0
    while idx < M and c < N:
        if truck[idx] >= container[c]:
            S+=container[c]
            idx += 1
            c += 1
        elif truck[idx] < container[c]:
            c+=1
    print("#{} {}".format(t, S))
