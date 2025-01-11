def ye(x):
    le=0
    c=0
    while x[le] in a:
        le+=1
    for j in range(le):
        c+=(26**j)*(a.index(x[le-1-j])+1)
    return 'R'+x[le:]+'C'+str(c)

def ey(x):
    l=[]
    while x>=26:
        if x%26==0:
            l.append('Z')
            x=x//26-1
        else:
            l.append(a[x%26-1])    
            x//=26
    if x!=0:
        l.append(a[x-1])
    l.reverse()
    return ''.join(l)

a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
z=['1','2','3','4','5','6','7','8','9','0']

for i in range(int(input())):
    s=input()
    if "C" in s:
        if s.index('C')!=0 and s[s.index('C')-1] in z:
            print(ey(int(s[s.index('C')+1:]))+s[1:s.index('C')])
        else:
            print(ye(s))
    else:
        print(ye(s))