for _ in range(int(input())):
    e,f=map(int,input().split())
    w=f-e
    n=int(input())
    dp=[0]+[float('inf')]*(w)
    for i in range(n):
        p,ww=map(int,input().split())
        for j in range(ww,w+1):
            dp[j]=min(dp[j],dp[j-ww]+p)
    if dp[w]==float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[w]}.')