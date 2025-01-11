from collections import deque
def bfs(x):
    queue=deque([(x,[])])
    se=set([n])
    while queue:
        x,l=queue.popleft()
        if x==m:
            print(len(l))
            print(''.join(l))
            return
        if x*3 not in se:
            lcopy=l[:]
            lcopy.append('H')
            queue.append((x*3,lcopy))
            se.add(x*3)
        if x//2 not in se:
            lcopy=l[:]
            lcopy.append('O')
            queue.append((x//2,lcopy))
            se.add(x//2)
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    bfs(n)