
sol = [0]*101
L = [0]*101
R = [0]*101

def order(x):
    if sol[x] =='*':
        return order(L[x])*order(R[x])
    elif sol[x] =='/':
        return order(L[x]) / order(R[x])
    elif sol[x] == '-':
        return order(L[x]) - order(R[x])
    elif sol[x]=='+':
        return order(L[x]) + order(R[x])
    else:
        return int(sol[x])

for t in range(1,11):
    N = int(input())
    for i in range(1,N+1):
        num = list(input().split())
        sol[i] = num[1]
        if len(num)>=3:
            L[i] = int(num[2])
        if len(num)==4:
            R[i] = int(num[3])
    result = order(1)
    print("#{} {}".format(t,int(result)))
