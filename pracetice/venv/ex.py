def fuc(x,k):

    if len(x)==3:
        print(x)

    else:
        for i in range(k,6):
            if used[i] == 0:
                used[i] = 1
                x.append(i)
                fuc(x,k+1)
                used[i]=0
                x.pop()


x=[]
used = [0]*6
fuc(x,0)
