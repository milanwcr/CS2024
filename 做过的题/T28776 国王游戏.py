n=int(input())
ak,bk=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
l.sort(key=lambda x:x[0]*x[1])
plus,ans=ak,0
for i in range(n):
    ans=max(ans,plus//l[i][1])
    plus*=l[i][0]
print(ans)