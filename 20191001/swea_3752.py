

T = int(input())

for t in range(1,T+1):

    N = int(input())
    numbers = list(map(int,input().split()))
    visit = [0]*(sum(numbers)+1)
    visit[0] = 1

    for number in numbers:
        for i in range(sum(numbers),-1,-1):
            if visit[i]:
                visit[i +number] = 1

    print("#{} {}".format(t, sum(visit)))