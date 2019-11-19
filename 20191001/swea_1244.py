
def back(k,numbers):
    if k==cnt:
        return
    else:
        for i in range(N-1):
            for j in range(i+1,N):
                tmp = numbers.copy()
                tmp[i], tmp[j] = tmp[j], tmp[i]
                if tmp not in visit[k]:
                    visit[k].append(tmp)
                    back(k+1, tmp)

T = int(input())
for t in range(1,T+1):
    numbers, cnt = map(int,input().split())
    numbers = list(str(numbers))
    N = len(numbers)
    visit = [[] for _ in range(cnt)]
    back(0,numbers)
    result = map(lambda x:''.join(x), visit[cnt-1])
    print("#{} {}".format(t, max(result)))