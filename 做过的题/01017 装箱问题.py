from math import ceil
while True:
    ans=0
    l=[int(s) for s in input().split()]
    if l==[0, 0, 0, 0, 0, 0]:
        break
    ans+=l[5]+l[4]+l[3]
    l[0]=max(l[0]-l[4]*11,0)
    l[0]=max(0,l[0]-max(0,l[3]*20-4*l[1]))
    l[1]=max(0,l[1]-5*l[3])
    ans+=ceil(l[2]/4)
    l[2]=l[2]%4
    if l[2]==1:
        l[0]=max(0,l[0]-7-max(0,20-4*l[1]))
        l[1]=max(0,l[1]-5)
    elif l[2]==2:
        l[0]=max(0,l[0]-6-max(0,12-4*l[1]))
        l[1]=max(0,l[1]-3)
    elif l[2]==3:
        l[0]=max(0,l[0]-5-max(0,4-4*l[1]))
        l[1]=max(0,l[1]-1)
    ans+=ceil(l[1]/9)
    l[1]=l[1]%9
    if l[1]!=0:
        l[0]=max(0,l[0]-36+4*l[1])
    ans+=ceil(l[0]/36)
    print(ans)