
MAX = 1000000
T = int(input())

for t in range(1,T+1):
    start, end = map(int,input().split())
    visit = [0]*(MAX+1)
    dp = [start]
    idx = 0
    while True:
        idx += 1
        new = []
        for num in dp:
            if num-1>0 and not visit[num-1]:
                new.append(num-1)
                visit[num-1] = 1
            if num-10>0 and not visit[num-10]:
                new.append(num-10)
                visit[num-10] = 1
            if num+1<=MAX and not visit[num+1]:
                new.append(num+1)
                visit[num+1] = 1
            if num*2<=MAX and not visit[num*2]:
                new.append(num*2)
                visit[num*2] = 1
        if end in new:
            break
        dp =new

    print("#{} {}".format(t,idx))