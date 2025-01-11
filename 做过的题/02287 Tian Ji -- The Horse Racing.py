while True:
    n=int(input())
    if n==0:
        break
    t=list(map(int,input().split()))
    k=list(map(int,input().split()))
    t.sort(reverse=True)
    k.sort(reverse=True)
    x,y,ans=0,0,0
    while x<len(t) and y<len(k):
        if t[x]<=k[y]:
            y+=1
        else:
            xx=x
            while xx<len(t) and t[xx]>k[y]:
                xx+=1
            ans+=1
            del t[xx-1],k[y]
    for i in range(len(t)):
        ans+=int(t[i]==k[len(t)-1-i])-1
    print(ans*200)