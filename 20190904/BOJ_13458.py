
N = int(input())
v = list(map(int, input().split()))
pro, ad = map(int, input().split())
v = list(map(lambda x: x-pro if x-pro>0 else 0,v))
result = N
for num in v:
    if num%ad==0:
        result += num//ad
    else:
        result += num//ad + 1
print(result)