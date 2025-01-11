n=int(input())
l=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
f=0
for i in l:
    if n%i==0:
        print('YES')
        f=1
        break
if f==0:
    print('NO')