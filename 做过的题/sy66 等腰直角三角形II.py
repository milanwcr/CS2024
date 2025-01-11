n=int(input())
print('*')
if n!=2:
    for i in range(n-2):
        print('*',end='')
        for j in range(i):
            print(' ',end='')
        print('*')
for i in range(n):
    print('*',end='')