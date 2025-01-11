for _ in range(int(input())):
    n=int(input())
    f=1
    ans=0
    while n>0:
        if n%2!=0:
            ans+=f
            n-=1
            f=1-f
        elif n%4==0 and n!=4:
            ans+=(n//2)*f+2*(1-f)
            n=n//2-2
        else:
            ans+=f*(n//2)+(1-f)
            n=n//2-1
    print(ans)