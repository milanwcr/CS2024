def war(a,b):
    if len(a)<len(b):
        if a==b[:len(a)]:
            return war(a,b[len(a):])
        return a>b
    elif len(a)==len(b):
        return a>=b
    else:
        if b==a[:len(b)]:
            return war(a[len(b):],b)
        return a>b

n=int(input())
l=list(input().split())
for i in range(n):
    j=i-1
    while j>=0 and war(l[i],l[j]):
        j-=1
    l.insert(j+1,l.pop(i))
print(''.join(l),end=' ')
l.reverse()
print(''.join(l))