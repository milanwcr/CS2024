from math import sqrt
n=int(input())
for i in range(n):
    a,b,c=map(float,input().split())
    if b*b-4*a*c>0:
        x1,x2=str(format((-b + sqrt(b*b-4*a*c))/(2*a),'.5f')),str(format((-b - sqrt(b*b-4*a*c))/(2*a),'.5f'))
        if x1=='-0.00000':
            x1='0.00000'
        if x2=='-0.00000':
            x2='0.00000'
        print('x1='+x1+';x2='+x2)
    elif b*b-4*a*c==0:
        x=str(format(-b/(2*a),'.5f'))
        if x=='-0.00000':
            x='0.00000'
        print('x1=x2='+x)
    else:
        x=str(format(-b/(2*a),'.5f'))
        if x=='-0.00000':
            x='0.00000'
        xx=str(format(sqrt(-b*b+4*a*c)/(2*a),'.5f'))
        if xx=='-0.00000':
            xx='0.00000'
        print('x1='+x+'+'+xx+'i;x2='+x+'-'+xx+'i')