n=int(input())
a=[]
for i in range(n):
    x,y=input().split()
    a.append([int(y),i,x])
a.sort(key=lambda x:(-x[0],x[1]))
i=0
while i<n and a[i][0]>=60:
    print(a[i][2])
    i+=1
if i<n:
    aa=a[i:]
    aa.sort(key=lambda x:x[1])
    for j in aa:
        print(j[2])