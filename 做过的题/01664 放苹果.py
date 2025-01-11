for _ in range(int(input())):
    m,n=map(int,input().split())
    dp=[[0]*(m+1) for i in range(n+1)]
    for i in range(n):
        dp[i+1][0]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if j<i:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-i]
    print(dp[n][m])