
def back(k,result):
    global Min,Max
    if k==L:
        Max = max(result,Max)
        Min = min(result,Min)
    else:
        if cal[0]:
            cal[0]-=1
            back(k+1,result+numbers[k])
            cal[0]+=1
        if cal[1]:
            cal[1]-=1
            back(k+1,result-numbers[k])
            cal[1]+=1
        if cal[2]:
            cal[2]-=1
            back(k+1,result*numbers[k])
            cal[2]+=1
        if cal[3]:
            cal[3]-=1
            back(k+1,int(result/numbers[k]))
            cal[3]+=1



T = int(input())

for t in range(1,T+1):
    N = int(input())
    cal = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    Max = -0xffffff
    Min = 0xffffff
    L = len(numbers)
    back(1,numbers[0])
    print("#{} {}".format(t,Max-Min))