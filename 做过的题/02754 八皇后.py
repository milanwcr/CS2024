def find(l,s,depth):
    if depth==8:
        return [[]]
    store=[]
    for i in range(8-depth):
        if l[i]+depth not in s[0] and l[i]-depth not in s[1]:
            sss=[set(se) for se in s]
            sss[0].add(l[i]+depth)
            sss[1].add(l[i]-depth)
            ll=l[:]
            ll.pop(i)
            ss=find(ll,sss,depth+1)
            for j in ss:
                store.append([l[i]]+j)
    return store

ans=find([1,2,3,4,5,6,7,8],[set(),set()],0)
i=0
while i<len(ans):
    if len(ans[i])!=8:
        del ans[i]
    else:
        i+=1
for _ in range(int(input())):
    print(''.join(map(str,ans[int(input())-1])))