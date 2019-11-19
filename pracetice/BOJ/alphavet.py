dxy=[(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(pos, s, choose, used):
    global Max
    if s in choose:
        if Max < len(choose):
            Max = len(choose)
        print(choose)
        return
    else:
        used.append(pos)
        for i in range(4):
            next = (pos[0]+dxy[i][0], pos[1]+dxy[i][1])
            if 0<=next[0]<R and 0<=next[1]<C and next not in used:
                choose.append(alpha[pos[0]][pos[1]])
                solution(next, alpha[next[0]][next[1]], choose,used)
                choose.pop()
        used.pop()

    return

R, C = map(int, input().split())
alpha = [list(input()) for _ in range(R)]
Max = 0
solution((0,0),alpha[0][0], [],[])

print(Max)