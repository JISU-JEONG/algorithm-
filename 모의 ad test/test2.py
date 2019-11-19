dx = [0,0,-1,1]
dy = [1,-1,0,0]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    atom = dict()
    for _ in range(N):
        x,y,d,k = map(int, input().split())
        atom[(2*x,2*y)] = [d, k]
    k_sum = 0
    while N:
        new_atom = dict()

        for key,value in atom.items():
            x, y = key
            d, k = value
            nx, ny = x +dx[d], y + dy[d]
            if -2000<=nx<=2000 and -2000<=ny<=2000:
                if new_atom.get((nx,ny)):
                    new_atom[(nx,ny)][0] = 4
                    new_atom[(nx, ny)][1] += k
                else:
                    new_atom[(nx,ny)] = value
        atom = dict()
        for key, value in new_atom.items():
            if value[0] == 4:
                k_sum += value[1]
            else:
                atom[key] = value
        N = len(atom)
    print('#{} {}'.format(t,k_sum))

