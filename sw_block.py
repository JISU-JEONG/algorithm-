def back(k, choose):
    global cnt

    if k == 3:
        cnt += 1
        print(cnt)

    else:
        for i in range(13):
            choose.append(i)
            back(k+1, choose)
            choose.pop()


cnt = 0

back(0,[])




