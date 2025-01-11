def ds(d,m,y):
    return y*365+20*month.index(m)+d+1

def sd(a):
    y=(a-1)//260
    d=a%260%20
    m=a%260%13
    if m==0:
        m=13
    return ' '.join([str(m),day[d],str(y)])

n=int(input())
print(n)
month=['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu','uayet']
day=['ahau','imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac']
for i in range(n):
    l=list(input().split())
    print(sd(ds(int(l[0][:-1]),l[1],int(l[2]))))