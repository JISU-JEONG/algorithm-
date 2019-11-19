T = int(input())

for t in range(1, T+1):
    N, A, B = map(int,input().split())
    n = int(N**0.5) + 1
    r= 0
    Min = 1000000
    while r < N:

        for c in range(1, n+1):
            if r*c > N:
                break
            elif (A*abs(r-c)+B*(N-r*c)) < Min:
                Min = (A*abs(r-c)+B*(N-r*c))

        r += 1

    print('#{} {}'.format(t,Min))