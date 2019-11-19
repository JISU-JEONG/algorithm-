for i in range(10):
    base = []
    result = 0
    num = int(input())

    for xyd in range(100):
        base.append(list(input()))

    # p = 고정점
    # q = 가변점
    # l 는 회문 길이
    for p in range(100):
        for q in range(p, 100):
            for l in range(100 - q, -1, -1):
                word_1 = list(base[p][y] for y in range(q, q + l))  # 세로 확인
                word_2 = list(base[x][p] for x in range(q, q + l))  # 가로 확인
                if word_1 == word_1[::-1] or word_2 == word_2[::-1]:  # 회문 있다면
                    if l > result:  # 길이 파악해서
                        result = l  # 저장
                        break  # 반복문 끝 생각해보니까 이 길이(l)에서는 더이상 반복문 돌릴 필요가 없을거같은데?

    print('#{0} {1}'.format(i + 1, result))