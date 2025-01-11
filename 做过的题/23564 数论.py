from math import sqrt
n=int(input())
l=int(sqrt(n))
f=0
if n==1:
    print(1)
else:
    a=0
    for i in range(2,l+1):
        b=0
        while n%i==0:
            b+=1
            a+=1
            n/=i
            if b>1:
                f=1
                print(0)
                break
        if f==1:
            break
    if n>1:
        a+=1
    if f==0:
        if a%2==0:
            print(1)
        else:
            print(-1)