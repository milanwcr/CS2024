from math import sqrt
def find(s):
    c=int(s)
    if c!=0 and sqrt(c)%1==0:
        return True
    for i in range(1,1+len(s)):
        c=int(s[:i])
        if c!=0 and sqrt(c)%1==0:
            if find(s[i:]):
                return True
    return False

a=input()
if find(a):
    print('Yes')
else:
    print('No')