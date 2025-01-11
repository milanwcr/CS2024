l=input()
ll=[0]*len(l)
f=0
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        f+=1
    ll[i+1]=f
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    print(ll[b-1]-ll[a-1])