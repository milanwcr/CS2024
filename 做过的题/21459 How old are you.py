n=int(input())
while n!=1:
    if n%2!=0:
        print("{}*3+1={}".format(n,n*3+1))
        n=n*3+1
    else:
        print("{}/2={}".format(n,int(n/2)))
        n=int(n/2)