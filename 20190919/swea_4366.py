
def find_b(x):
    S = 0
    for i in range(N):
        S *=2
        S +=x[i]
    return S

def find_t(x):
    S = 0
    for i in range(M):
        S *=3
        S +=x[i]
    return S

def solution():
    for i in range(N):
        bnum = b_num.copy()
        bnum[i] = (b_num[i]+1)%2
        for j in range(M):
            tnum1,tnum2 = t_num.copy(),t_num.copy()
            tnum1[j] = (t_num[j]+1)%3
            tnum2[j] = (t_num[j] + 2) % 3
            if find_b(bnum) == find_t(tnum1):
                return find_b(bnum)
            if find_b(bnum) == find_t(tnum2):
                return find_b(bnum)

T = int(input())

for t in range(1,T+1):
    b_num = list(map(int,list(input())))
    t_num = list(map(int, list(input())))
    N, M = len(b_num), len(t_num)
    print('#{} {}'.format(t, solution()))





