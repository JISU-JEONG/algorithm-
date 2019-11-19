

def add(x):
    if x<=15 and x%5==0:
        x = 100*(x//5)
        return x

def back(k,a1,a2,a3,a4,s1,s2,s3,s4):

    if k ==10:
        pass

    else:
        na1 = add(a1+command[k])
        back(k+1,na1,a2,a3,a4,s1+board[na1%100][na1//100],s2,s3,s4)
        back()
        back()
        back()



board = [
    [0, 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
    [10,13,16,19,25,30,35,40],
    [20,22,24,25,30,35,40],
    [30,28,27,26,25,30,35,40]
]

command = list(map(int,input().split()))
back(0,0,0,0,0,0,0,0,0)