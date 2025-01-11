while True:
    n=int(input())
    if n==0:
        break
    l=[[0,0,0] for i in range(n)]
    for i in range(n):
        l[i][0],l[i][1]=map(int ,input().split())
    l.sort(key=lambda x:(x[0],-x[1]))
    m=10001
    for i in range(n):
        if m>l[i][1]:
            l[i][2]=1
            m=l[i][1]
    m=10001
    ans=0
    l.sort(key=lambda x:(x[1],-x[0]))
    for i in range(n):
        if m>l[i][0] and l[i][2]==1:
            ans+=1
            m=l[i][0]
    print(ans)