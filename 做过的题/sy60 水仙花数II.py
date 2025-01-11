a,b=map(int,input().split())
l=[]
f=0
for i in range(a,b+1):
    j=(i//100)**3+((i%100)//10)**3+(i%10)**3
    if i==j:
        l.append(str(i))
        f=1
if f==0:
    print('NO')
else:
    print(' '.join(l))