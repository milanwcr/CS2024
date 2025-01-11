a,b,k=map(int,input().split())
A=[[1 for i in range(b)] for j in range(a)]
for i in range(k):
    r,s,p,t=map(int,input().split())
    p=(p-1)//2
    if t==0:
        for j in range(max(1,r-p),min(a,r+p)+1):
            for l in range(max(1,s-p),min(b,s+p)+1):
                A[j-1][l-1]=0
    else:
        for j in range(1,a+1):
            for l in range(1,b+1):
                if j<max(1,r-p) or j>min(a,r+p) or l<max(1,s-p) or l>min(b,s+p):
                    A[j-1][l-1]=0
ans=0
for i in range(a):
    ans+=sum(A[i])
print(ans)