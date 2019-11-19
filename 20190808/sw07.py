import sys

sys.stdin = open('input.txt', 'r')


T = int(input())

for t in range(T):
    n = int(input())
    screw = list(map(int, input().split()))
    m_screw = []
    f_screw = []
    result = []
    for i in range(len(screw)):
        if 1&i:
            f_screw.append(screw[i])
        else:
            m_screw.append(screw[i])

    L = max(screw)
    cnt = [0]*(L+1)
    for i in screw:
        cnt[i] += 1

    start = 0
    for i in m_screw:
        if cnt[i] == 1:
            start = i
            break

    result += [start, f_screw[m_screw.index(start)]]

    while len(result) != len(screw):
        start = m_screw.index(result[-1])
        result += [m_screw[start], f_screw[start]]


    print('#{} {}'.format(t+1,' '.join(map(str,result))))