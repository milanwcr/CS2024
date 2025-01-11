n=int(input())
for i in range(n):
    s=int(input())
    a=int(input())
    A=[int(j) for j in input().split()]
    b=int(input())
    B=[int(j) for j in input().split()]
    ans,j,k=0,0,0
    A.sort()
    B.sort(reverse=True)
    while j<=a-1 and k<=b-1:
        if A[j]+B[k]==s:
            jj,kk=1,1
            while j+jj<=a-1 and A[j]==A[j+jj]:
                jj+=1
            while k+kk<=b-1 and B[k]==B[k+kk]:
                kk+=1
            ans+=jj*kk
            j+=jj
            k+=kk
        elif A[j]+B[k]<s:
            j+=1
        else:
            k+=1
    print(ans)