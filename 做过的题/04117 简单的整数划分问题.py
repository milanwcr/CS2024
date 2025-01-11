while True:
    try:
        n=int(input())
        dp=[[0]*n for i in range(n)]
        for i in range(n):
            for j in range(i):
                dp[i][j]=sum(dp[i-j-1][j:])
            dp[i][i]=1
        print(sum(dp[n-1]))
    except EOFError:
        break