n=int(input())
for i in range(n):
    s=0
    m=int(input())
    while m%6==0:
        m=m/6
        s+=1
    while m%3==0:
        m=m/3
        s+=2
    if m==1:
        print(s)
    else:
        print(-1)