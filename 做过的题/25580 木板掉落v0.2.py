h,l,n=map(int,input().split())
v=list(map(float,input().split()))
v.sort()
print(f'{h-5*((l/v[n//2])**2):.2f}')