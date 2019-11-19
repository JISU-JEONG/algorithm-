
def back(k, S, t):
    global num
    if num ==M or S>M:
        return
    if k==3:
        if abs(M-num) > abs(M-S):
            num = S
    else:
        for i in range(t, N):
            if not used[i]:
                used[i] = 1
                back(k+1,S +numbers[i],i+1)
                used[i]=0

N, M = map(int,input().split())
numbers = list(map(int, input().split()))
num = 0
used = [0]*N
back(0,0,0)
print(num)
