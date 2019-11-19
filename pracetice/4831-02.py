def bus(pos, ditance, cnt):
    global MIN_NUM, flag

    if ditance >= N:
        if MIN_NUM > cnt:
            MIN_NUM = cnt
            flag = 1
        return
    else:
        if cnt < MIN_NUM:
            for i in range(ditance,pos-1,-1):
                if used[i] == 0 and check[i] != 0:
                    used[i] = 1
                    bus(i, i+K, cnt+1)
    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    flag = 0
    K, N, M = map(int, input().split())
    MIN_NUM = N
    charge = list(map(int, input().split()))
    used = [0] * (N+1)
    check = [0] * (N+1)
    for i in charge:
        check[i] = K
    bus(1, K, 0)
    if flag:
        print('#{} {}'.format(test_case, MIN_NUM))
    else:
        print('#{} {}'.format(test_case, 0))