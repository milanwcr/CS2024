while True:
    n=int(input())
    if n==0:
        break
    a=[int(s) for s in input().split()]
    aa=[]
    for i in range(n):
        l=[i+1]
        ind=i
        while a[ind]!=i+1:
            l.append(a[ind])
            ind=a[ind]-1
        aa.append(l)
    while True:
        s=input()
        if s=='0':
            break
        k=int(s[:s.index(' ')])
        ans=[' ' for j in range(n)]
        for i in range(len(s[s.index(' ')+1:])):
            ans[aa[i][k%len(aa[i])]-1]=s[s.index(' ')+1+i]
        print(''.join(ans))
    print()