n,m=map(int,input().split())
b=0
while n//m-b!=0:
    a=n//m-b
    n+=a
    b+=a
print(n)