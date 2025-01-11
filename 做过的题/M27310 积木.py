def find(ss,l):
    for j in l:
        if ss[0] in a[j]:
            if len(ss)==1:
                return 'YES'
            else:
                lcopy=l[:]
                del lcopy[lcopy.index(j)]
                if find(ss[1:],lcopy)=='YES':
                    return 'YES'
    return "NO"
n=int(input())
a=[]
for i in range(4):
    a.append(input())
for i in range(n):
    s=input()
    print(find(s,[0,1,2,3]))