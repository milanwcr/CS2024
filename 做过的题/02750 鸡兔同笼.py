a=int(input())
if a%2!=0:
    print('0 0')
else:
    if a%4==0:
        print(str(a//4)+' '+str(a//2))
    else:
        print(str(a//4+1)+' '+str(a//2))