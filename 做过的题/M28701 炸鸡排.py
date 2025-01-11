n,k=map(int,input().split())
t=list(map(int,input().split()))
s=sum(t)
t.sort()
while True:
    if s>=k*t[-1]:
        print('{:.3f}'.format(s/k))
        break
    s-=t.pop()
    k-=1