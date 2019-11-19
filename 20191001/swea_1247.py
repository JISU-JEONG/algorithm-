
def back(k, s, pos):
    global Min
    if Min <s:
        return
    if k ==N:
        Min = min(Min, s+abs(pos[0]-home[0])+abs(pos[1]-home[1]))
    else:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                back(k+1,s+abs(customer[i][0]-pos[0])+abs(customer[i][1]-pos[1]),customer[i])
                used[i] = 0


T = int(input())

for t in range(1,T+1):
    N = int(input())
    point = list(map(int,input().split()))
    customer = []
    used = [0]*N
    office = (point[0],point[1])
    home = (point[2],point[3])
    for i in range(2,N+2):
        customer.append((point[2*i], point[2*i+1]))
    Min = 0xffff
    back(0, 0, office)

    print("#{} {}".format(t,Min))