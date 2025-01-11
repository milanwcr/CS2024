ans=['win','lose']
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    if a<b:
        a,b=b,a
    f=0
    if a==b:
        print('win')
        continue
    while b!=0:
        if a//b>=2:
            print(ans[f])
            break
        else:
            a,b=b,a-b
            f=1-f