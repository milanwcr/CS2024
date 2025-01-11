n=int(input())
a=[[int(s)] for s in input().split()]
for i in range(n):
    a[i].append(i+1)
a.sort()
ans=[a[i][1] for i in range(n)]
sum=0
for i in range(n-1):
    sum+=a[i][0]*(n-i-1)
print(' '.join(map(str,ans)))
print(f"{sum/n:.2f}")