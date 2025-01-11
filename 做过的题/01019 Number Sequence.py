l=[0,45, 9045, 1395495, 189414495, 23939644445]
for i in range(int(input())):
    n=int(input())
    le=0
    for j in range(6):
        if l[j]<n:
            le+=1
    n-=l[le-1]
    k=10**(le-1)
    while n>(le*(k*k+k-10**(le-1)*(10**(le-1)-1))//2-(k-10**(le-1)+1)*((10**le-1)//9-le)):
        k+=1
    k-=1
    n-=(le*(k*k+k-10**(le-1)*(10**(le-1)-1))//2-(k-10**(le-1)+1)*((10**le-1)//9-le))
    k+=1
    ll=[str(s) for s in range(1,k+1)]
    s=''.join(ll)
    print(s[n-1])