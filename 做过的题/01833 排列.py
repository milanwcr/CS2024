import math

def count(l,x,j):
    l.sort()
    return (j-l.index(x))*math.factorial(j)

def pull(l,m):
    if len(l)==1:
        ans.append(l[0])
    else:
        mm=(m-1)//math.factorial(len(l)-1)
        ans.append(l[mm])
        m=m%math.factorial(len(l)-1)
        if m==0:
            m=math.factorial(len(l)-1)
        del l[mm]
        pull(l,m)

def cul(aa):
    global k,n
    for i in range(n):
        if k>count(aa[n-i-1:],aa[n-i-1],i):
            k-=count(aa[n-i-1:],aa[n-i-1],i)
        else:
            b=aa[n-i-1:]
            b.sort()
            kk=(k-1)//math.factorial(i)+1
            ans.append(b[b.index(aa[n-i-1])+kk])
            k=k%math.factorial(i)
            if k==0:
                k=math.factorial(i)
            del b[b.index(aa[n-i-1])+kk]
            pull(b,k)
            k=0
            break

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(s) for s in input().split()]
    ans=[]
    cul(a)
    if k!=0:
        if n<=4:
            k=k%math.factorial(n)
            if k==0:
                k=math.factorial(n)
        a=[i+1 for i in range(n)]
        k-=1
        if k!=0:
            cul(a)
        else:
            ans=a[:]
    if n>len(ans):
        print(' '.join(map(str,a[:n-len(ans)])),end=' ')
    print(' '.join(map(str,ans)))