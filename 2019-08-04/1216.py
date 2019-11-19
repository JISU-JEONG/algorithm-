import sys

sys.stdin = open('input.txt','r')

for _ in range(10):
    t = int(input())
    s = [ input() for _ in range(100)]
    max_n = 0

    for i in range(100):
        for j in range(100):
            tmp = ''
            for k in range(j,100):
                tmp += s[i][k]
                if tmp == tmp[::-1] and len(tmp) > max_n:
                    max_n = len(tmp)

    for i in range(100):
        for j in range(100):
            tmp = ''
            for k in range(j, 100):
                tmp += s[k][i]
                if tmp == tmp[::-1] and len(tmp) > max_n:
                    max_n = len(tmp)

    print('#{} {}'.format(t, max_n))