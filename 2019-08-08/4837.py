T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K =map(int,input().split())
    count_t = 0
    num = list(range(1, 13))
    for i in range(1<<len(num)):
        sum_num = []
        for j in range(len(num)):
            if i & (1<<j):
                sum_num.append(num[j])
        if len(sum_num) == N and sum(sum_num) == K:
            count_t +=1
    print('#{} {}'.format(t, count_t))