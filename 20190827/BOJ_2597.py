
def color(x,y):
    return min(x,y),max(x,y)

L = int(input())
r1, r2 = map(int, input().split())
b1, b2 = map(int, input().split())
y1, y2 = map(int, input().split())
r1, r2 = color(r1, r2)
b1, b2 = color(b1, b2)
y1, y2 = color(y1, y2)
flag1 = 0
flag2 = 0
if r1+r2 == b1+b2:
    flag1 = 1
if r1+r2 == y1+y2:
    flag2 = 1
if (r1+r2)/2 > L-(r1+r2)/2:
    L = (r1+r2)/2
    if b1 > L: b1 = 2*L-b1
    if b2 > L: b2 = 2*L -b2
    if y1 > L: y1 = 2 * L - y1
    if y2 > L: y2 = 2 * L - y2
else:
    L = L-(r1+r2)/2
    if b1 > (r1+r2)/2: b1 = b1-(r1+r2)/2
    else: b1 = (r1+r2)/2-b1
    if b2 > (r1+r2)/2: b2 = b2-(r1+r2)/2
    else: b2 = (r1 + r2) / 2 - b2
    if y1 > (r1+r2)/2: y1 = y1-(r1+r2)/2
    else: y1 = (r1 + r2) / 2 - y1
    if y2 > (r1+r2)/2: y2 = y2-(r1+r2)/2
    else: y2 = (r1 + r2) / 2 - y2

if not flag1:
    b1, b2 = color(b1, b2)
    y1, y2 = color(y1, y2)
    if b1+b2 == y1+y2:
        flag2 = 1
    if (b1 + b2) / 2 > L - (b1 + b2) / 2:
        L = (b1 + b2) / 2
        if y1 > L: y1 = 2 * L - y1
        if y2 > L: y2 = 2 * L - y2
    else:
        L = L - (b1 + b2) / 2
        if y1 > (b1 + b2) / 2:
            y1 = y1 - (b1 + b2) / 2
        else:
            y1 = (b1 + b2) / 2 - y1
        if y2 > (b1 + b2) / 2:
            y2 = y2 - (b1 + b2) / 2
        else:
            y2 = (b1 + b2) / 2 - y2

if not flag2:
    L = max((y1+y2)/2,L-(y1+y2)/2)

print(L)