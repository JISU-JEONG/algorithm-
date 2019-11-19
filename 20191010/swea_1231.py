
for t in range(1, 11):
    N = int(input())
    alpha = [0]*(N+1)
    L = [0] * (N + 1)  # tree = [[0, 0, 0] for _ in range(V+1)]
    R = [0] * (N + 1)  # tree = [[] for _ in range(V+1)]
    P = [0] * (N + 1)
    for _ in range(N):
        order = list(input().split())
        if len(order)==2:
            num, ch = order
            num = int(num)
        elif len(order)==3:
            num, ch, l = order
            num, l = int(num), int(l)
            P[l] = num
            L[num] = l
        else:
            num, ch, l, r = order
            num, l, r = int(num), int(l), int(r)
            P[l] = P[r] = num
            L[num] = l
            R[num] = r
        alpha[num] = ch
    def inorder(v):
        if v == 0:
            return
        inorder(L[v])
        print(alpha[v], end='')
        inorder(R[v])
    print("#{} ".format(t),end='')
    inorder(1)
    print()