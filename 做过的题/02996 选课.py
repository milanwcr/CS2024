n=int(input())
m=int(input())
a=[int(s) for s in input().split()]
for i in range(m):
    left,right=n-1,n-1
    while left>0 and a[left]<a[left-1]:
        left-=1
    if left==0:
        a.reverse()
        continue
    while a[right]<a[left-1]:
        right-=1
    a[left-1],a[right]=a[right],a[left-1]
    a[left:]=a[left:][::-1]
print(' '.join(map(str,a)))