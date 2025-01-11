n=int(input())
l=input().split()
l.append('')
s=0
for i in range(n):
    s+=len(l[i])
    print(l[i],end='')
    if i==n-1:
        break
    if s+len(l[i+1])+1>80:
        s=0
        print()
        continue
    else:
        s+=1
        print(' ',end='')