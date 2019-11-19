def BoubleSort(x):
    for i in range(len(x)-1, 0, -1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    num_list = list(map(int, input().split()))
    BoubleSort(num_list)
    print('#{} {}'.format(test_case, num_list[-1] - num_list[0] ))