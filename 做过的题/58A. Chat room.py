s=input()
l="hello"
f=0
for i in s:
    if i==l[f]:
        f+=1
    if f==5:
        break
if f==5:
    print("YES")
else:
    print('NO')