def bs(l):
    if l[n-1][1]>=l[n-1][0]:
        return l[n-1][0]
    if l[0][0]>=s:
        return s
    if l[0][0]>=l[0][1]:
        return l[0][0]
    left,right=0,n-1
    while left<=right:
        mid=left+(right-left)//2
        if l[mid][0]<=l[mid][1] and l[mid+1][0]>=l[mid+1][1]:
            return min(l[mid][1],l[mid+1][0])
        elif l[mid][0]>l[mid][1]:
            right=mid-1
        else:
            left=mid+1
for i in range(int(input())):
    n=int(input())
    a=[int(s) for s in input().split()]
    b=[int(s) for s in input().split()]
    s=sum(b)
    c=[]
    for j in range(n):
        c.append([a[j],b[j]])
    c.sort()
    c[0][1]=s-c[0][1]
    for j in range(1,n):
        c[j][1]=c[j-1][1]-c[j][1]
    print(bs(c))