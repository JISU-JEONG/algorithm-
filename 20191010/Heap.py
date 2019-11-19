import sys

input = sys.stdin.readline
# 힙구현
H = [0]*100001     # 저장소
top = 0         # 자료의 수, 마지막 노드의 인덱스

def push(item):
    global top
    top += 1
    H[top] = item
    c, p = top, top//2
    while p:
        if H[p]<H[c]:
            H[p],H[c] = H[c],H[p]
        else:
            break
        c = p
        p = c//2

def pop():
    global top
    # empty 체크
    if top==0:
        return 0
    ret = H[1]
    H[1] = H[top]
    H[top] = 0
    top -= 1
    p,c = 1, 2
    while c<=top:
        if c+1 <= top and H[c]<H[c+1]:
            c+=1
        if H[p]<H[c]:
            H[p],H[c] = H[c],H[p]
            p = c
            c = p * 2  # 왼쪽자식
        else:
            break

    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    if N==0:
        print(pop())
    else:
        push(N)