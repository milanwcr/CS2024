from collections import deque
import sys
input = sys.stdin.read
def bfs(x,y,H,m,n,l,h):
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    queue=deque([(x,y)])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n and h[nx][ny]<H and not l[nx][ny]:
                l[nx][ny]=True
                queue.append((nx,ny))

def main():
    data = input().split()
    idx = 0
    k = int(data[idx])
    idx += 1
    results = []

    for _ in range(k):
        m, n = map(int, data[idx:idx + 2])
        idx += 2
        h = []
        for i in range(m):
            h.append(list(map(int, data[idx:idx + n])))
            idx += n
        l=[[False]*(n) for i in range(m)]

        I, J = map(int, data[idx:idx + 2])
        idx += 2

        p = int(data[idx])
        idx += 1

        for _ in range(p):
            a, b = map(int, data[idx:idx + 2])
            bfs(a-1,b-1,h[a-1][b-1],m,n,l,h)
            idx += 2

        results.append("Yes" if l[I-1][J-1] else "No")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()