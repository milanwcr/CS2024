n=int(input())
l=bin(n)
l=l[2:]
if l==l[::-1]:
    print('Yes')
else:
    print('No')