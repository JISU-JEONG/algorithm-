T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    str1 =input()
    str2 =input()
    str_set = set(str1)
    max_count = 0
    for ch in str_set:
        if max_count < str2.count(ch):
            max_count = str2.count(ch)
    print('#{} {}'.format(test_case, max_count))