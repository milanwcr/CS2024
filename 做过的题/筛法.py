l=[i+2 for i in range(10000)]
n=1
while len(l)>n:
    i=n
    while len(l)>i:
        if l[i]%l[n-1]==0:
            del l[i]
        else:
            i+=1
    n+=1
print(l)
print(len(l),n)