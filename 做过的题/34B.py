n,m=map(int,input().split())
l=input().split()
l=[int(s) for s in l]
l.append(0)
l.sort()
print(-sum(l[0:min(m,l.index(0))]))