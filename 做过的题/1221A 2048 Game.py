from collections import Counter
for i in range(int(input())):
    n=int(input())
    c=Counter([int(s) for s in input().split()])
    c[2]+=c[1]//2
    c[4]+=c[2]//2
    c[8]+=c[4]//2
    c[16]+=c[8]//2
    c[32]+=c[16]//2
    c[64]+=c[32]//2
    c[128]+=c[64]//2
    c[256]+=c[128]//2
    c[512]+=c[256]//2
    c[1024]+=c[512]//2
    c[2048]+=c[1024]//2
    if c[2048]>=1:
        print("YES")
    else:
        print("NO")