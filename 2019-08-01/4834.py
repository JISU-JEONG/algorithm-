
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    str_num = input()
    numbers = list(map(int, str_num))
    cnt = [0] * 10

    for i in numbers:
        cnt[i] += 1

    max_idx = max(cnt)

    for i in range(10):
        if cnt[i] == max_idx:
            max_num = i



    print('#{} {} {}'.format(test_case, max_num, max_idx))