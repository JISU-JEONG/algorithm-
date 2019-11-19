for t in range(int(input())):
    ch, num= input().split()
    result = input().split()
    char_num =["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_dic ={
        "ZRO" : 0,
        "ONE" : 1,
        "TWO" : 2,
        "THR" : 3,
        "FOR" : 4,
        "FIV" : 5,
        "SIX" : 6,
        "SVN" : 7,
        "EGT" : 8,
        "NIN" : 9
    }
    cnt = [0]*10
    for num in result:
        cnt[num_dic[num]] += 1

    print('#{}'.format(t))

    for i in range(10):
        print((char_num[i]+' ')*cnt[i], end='')
    print()