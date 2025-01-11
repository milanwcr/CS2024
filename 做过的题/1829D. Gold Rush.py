for _ in range(int(input())):
    n,m=map(int,input().split())
    cn,cm,cnm=0,0,0
    while n%3==0:
        cn+=1
        n//=3
    while m%3==0:
        cm+=1
        m//=3
    if cn<cm or m%n!=0:
        print('NO')
        continue
    cn-=cm
    m//=n
    while m%2==0:
        cnm+=1
        m//=2
    if m!=1 or cnm>cn:
        print('NO')
        continue
    print('YES')