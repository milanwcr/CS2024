def cal(l):
    b=[]
    if len(l)==1:
        return [l]
    for i in range(len(l)):
        c=l[:]
        c.pop(i)
        d=cal(c)
        for j in range(len(d)):
            b.append([l[i]]+d[j])
    return b

a=[i+1 for i in range(int(input()))]
ans=cal(a)
for i in ans:
    print(' '.join(map(str,i)))