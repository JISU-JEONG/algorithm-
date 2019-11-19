
def solve(x,y):
    global S
    S += abs(t[x] - t[y])
    if t[x] >t[y]:
        return x
    else:
        return y

def game(lo, hi):
    if hi-lo==1:
        return solve(lo,hi)
    else:
        mid = (lo+hi)>>1
        return solve(game(lo, mid),game(mid+1,hi))

T = int(input())

for t in range(1,T+1):
    N = int(input())
    S = 0
    t = list(map(int,input().split()))
    game(0, 2**N-1)
    print("#{} {}".format(t,S))