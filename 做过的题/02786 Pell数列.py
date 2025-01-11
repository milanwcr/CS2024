n=int(input())
for i in range(n):
    k=int(input())
    if k==1:
        print(1)
        continue
    x,y=1,2
    for j in range(k-2):
        x,y=y,(2*y+x)%32767
    print(y%32767)