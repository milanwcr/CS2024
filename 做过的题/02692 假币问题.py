ans=['heavy','light']
for _ in range(int(input())):
    a=[0 for s in range(12)]
    l=[]
    for i in range(3):
        l.append(list(input().split()))
        for k in range(len(l[i][0])):
            a[ord(l[i][0][k])-65]+=2*int(l[i][2]!='even')-1
            a[ord(l[i][1][k])-65]+=2*int(l[i][2]!='even')-1
    maxx=max(a)
    for i in range(12):
        if a[i]==maxx:
            f,an=0,0
            for j in range(3):
                if l[j][2]=='up':
                    if f==0:
                        an=int(chr(65+i) in l[j][1])
                        f=1
                    else:
                        f+=int(int(chr(65+i) in l[j][1])!=an)
                if l[j][2]=='down':
                    if f==0:
                        an=int(chr(65+i) in l[j][0])
                        f=1
                    else:
                        f+=int(int(chr(65+i) in l[j][0])!=an)
            if f==1:
                print(f'{chr(65+i)} is the counterfeit coin and it is {ans[an]}.')