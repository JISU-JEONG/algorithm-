def solution(N, number):
    answer = -1
    Max = 32001
    dp = [[] for _ in range(9)]
    for i in range(1,9):
        k = int(str(N)*i)
        if k < Max:
            dp[i].append(k)

    def find(n, x):
        for i in range(1,n+1):
            if x in dp[i]:return 0
        return 1

    for i in range(2,9):
        for j in range(1, i//2+1):
            a, b = j, i-j
            for n1 in dp[a]:
                for n2 in dp[b]:
                    if n1+n2 < Max and find(i,n1+n2):
                        dp[i].append(n1+n2)
                    if n1*n2 < Max and find(i,n1*n2):
                        dp[i].append(n1 * n2)
                    if n1-n2 > 0 and find(i,n1-n2):
                        dp[i].append(n1-n2)
                    if n2-n1 > 0 and find(i,n2-n1):
                        dp[i].append(n2-n1)
                    if n1//n2 > 0 and find(i, n1//n2):
                        dp[i].append(n1//n2)
                    if n2//n1 > 0 and find(i,n2//n1):
                        dp[i].append(n2//1)
    for i in range(1, 9):
        if number in dp[i]:
            answer = i
            break
    return answer