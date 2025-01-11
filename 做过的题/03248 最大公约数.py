while True:
    try:
        m,n=map(int,input().split())
        while m%n!=0:
            m,n=n,m%n
        print(n)
    except EOFError:
        break