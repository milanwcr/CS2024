while True:
    a=float(input())
    if a==0:
        break
    n=1
    s=0
    while s<a:
        n+=1
        s+=1/n
    print(str(n-1)+" card(s)")