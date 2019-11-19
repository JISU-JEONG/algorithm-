import sys

sys.stdin = open('input.txt', 'r')

for tc in range(10):
    n = int(input())
    string = [list(input()) for _ in range(100)]
    count = 0
    b = 0
    for i in range(100):
        for j in range(100):
            for m in range(100-j):
                for k in range(m):
                    b = k
                    if string[i][j+k] != string[i][m-1+j-k]:
                        break
                    else:
                        if b >= count:
                            count = b+1
                            break

                for k in range(m):
                    b = k
                    if string[j+k][i] != string[m-1+j-k][i]:
                        break
                else:
                    if b >= count:
                        count = b+1
                        break
    print('#{} {}'.format(n, count))