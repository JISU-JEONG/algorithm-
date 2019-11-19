# import sys
#
# sys.stdin = open("input.txt", "r")
#
# for t in range(1, 11):
#     N = int(input())
#     string = [input() for _ in range(100)]
#     max_length = 0
#     for i in range(100):
#         for j in range(100,0,-1):
#             if max_length < j:
#                 for k in range(100-j+1):
#                     pattern = string[i][k:k+j]
#                     if pattern == pattern[::-1]:
#                         max_length = j
#                         break
#
#     for i in range(100):
#         for j in range(100,0,-1):
#             if max_length < j:
#                 pattern = ''
#                 for k in range(100-j+1):
#                     for l in range(j):
#                         pattern += string[k+l][i]
#                     if pattern == pattern[::-1]:
#                         max_length = j
#                         break
#
#     print('#{} {}'.format(t, max_length))



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