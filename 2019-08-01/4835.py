T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    max_num, min_num = 0, 0
    for i in range(M):
        max_num += arr[i]
        min_num += arr[i]

    for i in range(1, N-M+1):
        mx= 0
        for j in range(i, i+M):
            mx +=arr[j]
        if max_num < mx:
            max_num = mx
        if min_num > mx:
            min_num = mx
    print('#{} {}'.format(test_case, max_num-min_num))