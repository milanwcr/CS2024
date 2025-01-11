import math
while True:
    n=int(input())
    ans=float('inf')
    if n==0:
        break
    for i in range(n):
        a,b=map(int,input().split())
        if b>=0:
            ans=min(ans,math.ceil(b+4500*3.6/a))
    print(ans)