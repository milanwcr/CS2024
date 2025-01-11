n=int(input())
for i in range(n):
    s=int(input())
    a=s*(s+1)//2
    f=0
    while s>=2:
        f+=1
        s/=2
    print(a-2*(2**(f+1)-1))