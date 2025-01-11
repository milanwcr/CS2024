for _ in range(int(input())):
    n,k=map(int,input().split())
    m=[int(s) for s in input().split()]
    p=[int(s) for s in input().split()]
    dp=[0]*n
    for i in range(n):
        maxx=0
        for j in range(i):
            if m[i]-m[j]>k:
                maxx=max(maxx,dp[j])
            else:
                break
        dp[i]=maxx+p[i]
    print(max(dp))