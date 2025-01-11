for i in range(int(input())):
    n=int(input())
    a=[int(s) for s in input().split()]
    b=[int(s) for s in input().split()]
    print(min(n*min(a)+sum(b),min(b)*n+sum(a)))