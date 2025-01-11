def cal(s):
    if s==[]:
        return 0
    su=0
    x=0
    if 'hundred' in s:
        su+=(shu.index(s[0])+1)*100
        x=2
    if len(s)-x==1:
        if s[-1] in shuu:
            su+=(shuu.index(s[-1])+2)*10
        else:
            su+=shu.index(s[-1])+1
    if len(s)-x==2:
        su+=(shuu.index(s[-2])+2)*10+shu.index(s[-1])+1
    return su

shu=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
shuu=['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
l=input().split()
f=1
ans=0
xm,xl=0,0
if l[0]=='negative':
    del l[0]
    f=-1
if 'million' in l:
    ans+=1000000*cal(l[:l.index('million')])
    xm=l.index('million')+1
if 'thousand' in l:
    ans+=1000*cal(l[xm:l.index('thousand')])
    xl=l.index('thousand')+1
if l[-1]=='zero':
    print(0)
else: 
    if xl!=len(l) and xm!=len(l):
        ans+=cal(l[max(xl,xm):])
    print(ans*f)