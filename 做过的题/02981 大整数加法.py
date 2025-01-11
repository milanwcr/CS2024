a=input().lstrip('0')
b=input().lstrip('0')
if len(b)>len(a):
    a,b=b,a
a=[int(s) for s in a]
b=[int(s) for s in b]
a.reverse()
b.reverse()
a.append(0)
for i in range(len(b)):
    a[i],a[i+1]=(a[i]+b[i])%10,a[i+1]+(a[i]+b[i])//10
for i in range(len(b),len(a)-1):
    a[i],a[i+1]=a[i]%10,a[i+1]+a[i]//10
if a[-1]==0:
    del a[-1]
a.reverse()
if a==[]:
    print(0)
else:
    print(''.join(map(str,a)))