
def order(k):
    global cnt

    if k>=h or cnt>N:
        return
    order(k+1)

    while root[x]:
        x+=1
    if x <=N:
        root[x] = cnt
        cnt += 1
    order(k+1)


T = int(input())

for t in range(1,T+1):
    N = int(input())
    root = [0] * 1001
    h = 0
    while 2**h <= N:
        h+=1
    cnt = 1
    order(0)
    print("#{} {} {}".format(t,root[1],root[N//2]))