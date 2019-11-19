


N = int(input())
vol = list(map(int, input().split()))
pro, ad = map(int, input().split())
vol = list(map(lambda x:x-pro if x-pro>=0 else 0,vol))
s = 0;
for v in vol:
    if v!=0:
        s += v//ad
        if v%ad>0:
            s+=1
s+=N
print(s)