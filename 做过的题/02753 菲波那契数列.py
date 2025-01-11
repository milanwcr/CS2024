n=int(input())
for i in range(n):
    a=int(input())
    x,y=1,1
    for j in range(a-2):
        x,y=y,x+y
    print(y)