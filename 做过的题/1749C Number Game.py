for _ in range(int(input())):
    n=int(input())
    a=[int(s) for s in input().split()]
    a.sort()
    left=-1
    while left<n-1 and a[left+1]==1:
        left+=1
    if left==-1:
        print(0)
        continue
    right=left
    k=1
    while left>0 and right<=n-1:
        if right!=n-1 and a[right+1]<=k+1:
            left-=1
            right+=1
        elif left>1:
            left-=2
        else:
            break
        k+=1
    print(k)