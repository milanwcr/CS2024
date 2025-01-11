from heapq import heapify,heappop,heappush
l,r=[],[]
for _ in range(int(input())):
    s=list(input().split())
    if s[0]=='+':
        heappush(l,-int(s[1]))
        heappush(r,int(s[2]))
    else:
        del l[l.index(-int(s[1]))]
        del r[r.index(int(s[2]))]
    if not l:
        print('NO')
        continue
    lm,rm=-heappop(l),heappop(r)
    if lm>rm:
        print("YES")
    else:
        print("NO")
    heappush(l,-lm)
    heappush(r,rm)