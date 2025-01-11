一、数据结构  

1.string操作 string.split() ; string.strip() 移除首位指定字符; string.find(item) 会输出第一个位置,或给出 -1 . 

2.list/tuple操作  list(range(3))==[0,1,2] ；len(list)列表长度 ; list.append(item) 末尾加入元素;; list.insert(index,  item) 插入元素;  list.reverse(self) 反转；list.pop(index) ,返回 index 处元素的值； list.index(item) 会输出第一个位置；

3.deque操作   from collections import deque ；queue.popleft() 弹出头部； queue.pop()弹出尾部 ； queue.appendleft() 插入头部； queue.append()插入尾部 

二、dp模板

1.0-1背包

```python
def  knapsack_2d(weights, values, W):   
    n = len(weights)   
    dp = [[0] * (W + 1) for _ in range(n + 1)]   
    for i in range(1, n + 1):     
        for j in range(W + 1):       
            if j >= weights[i - 1]:           
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] +  values[i - 1])
            else: 
                dp[i][j] = dp[i - 1][j]   
    return dp[n][W]

```

2.完全背包

```python
def knapsack_complete(weights, values, capacity):
    dp = [0] * (capacity + 1)
    dp[0] = 0
    for i in range(len(weights)): 
        for j in range(weights[i], capacity + 1): 
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]

```

三、dfs模板

04123 马走日

```python
def find(i,j,depth,s):
    for k in range(8):
        ni=i+dx[k]
        nj=j+dy[k]
        if 0<=ni<n and 0<=nj<m and (ni,nj) not in s:
            l=list(s)
            ll=l[:]
            ll.append((ni,nj))
            find(ni,nj,depth+1,set(ll))
    if depth==n*m:
        ans[0]+=1

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]
for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    ans=[0]
    find(x,y,1,set([(x,y)]))
    print(ans[0])
```

四、bfs模板

04129: 变换的迷宫

```python
from collections import deque
def bfs(x,y):
    queue=deque([(x,y,0)])
    while queue:
        x,y,t=queue.popleft()
        for j in range(4):
            nx,ny=x+dx[j],y+dy[j]
            if 0<=nx<r and 0<=ny<c:
                if find[nx][ny][(t+1)%k]:
                    continue
                if a[nx][ny]=='E':
                    return t+1
                if a[nx][ny]!='#' or (t+1)%k==0:
                    find[nx][ny][(t+1)%k]=True
                    queue.append((nx,ny,t+1))
    return 'Oop!'
                    

dx,dy=[0,1,0,-1],[1,0,-1,0]
for _ in range(int(input())):
    r,c,k=map(int,input().split())
    a=[list(input()) for i in range(r)]
    find=[[[False for l in range(k)] for j in range(c)] for i in range(r)]
    for i in range(r):
        if 'S' in a[i]:
            find[i][a[i].index('S')][0]=True
            print(bfs(i,a[i].index('S')))
            break
```

