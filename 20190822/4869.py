def play(num):
    dp = [1, 3]

    for i in range(2, num):
        dp.append(dp[i-1] + 2*dp[i-2])

    return dp[num-1]



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num = int(input())
    print('#{} {}'.format(test_case, play(num//10)))