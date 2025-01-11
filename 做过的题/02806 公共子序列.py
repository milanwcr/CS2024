while True:
    try:
        a,b=input().split()
        al=len(a)
        bl=len(b)
        dp=[[0]*(bl+1) for i in range(al+1)]
        for i in range(al):
            for j in range(bl):
                if a[i]==b[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        print(dp[al][bl])
    except EOFError:
        break