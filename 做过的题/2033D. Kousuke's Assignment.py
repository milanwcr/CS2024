for _ in range(int(input())):
    n=int(input())
    a=[int(s) for s in input().split()]
    summ=[0]*(n+1)    
    s={0}
    ans=0
    for i in range(n):
        summ[i+1]+=summ[i]+a[i]
        if summ[i+1] not in s:
            s.add(summ[i+1])
        else:
            ans+=1
            s={summ[i+1]}
    print(ans)