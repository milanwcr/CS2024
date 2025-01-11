def judge(a):
    f=0
    for i in range(2,a):
        if a%i==0:
            f=1
            break
    if f==0:
        return True
    else:
        return False

s=int(input())
for i in range(s//2-1):
    if judge(s//2-i) and judge(s+i-s//2):
        print((s//2-i)*(s+i-s//2))
        break