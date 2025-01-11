d=input()
l=list("qwertyuiopasdfghjkl;zxcvbnm,./")
a=input()
for i in range(len(a)):
    if d=="R":
        print(l[l.index(a[i])-1],end='')
    else:
        print(l[l.index(a[i])+1],end='')