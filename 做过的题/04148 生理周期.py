n=0
while True:
    p,e,i,d=map(int,input().split())
    n+=1
    if p==-1:
        break
    if i<d:
        f=d+33-(d-i)%33
    elif (d-i)%33==0:
        f=d+33
    else:
        f=d+(i-d)%33
    for j in range(f,50003,33):
        if (j-p)%23==0 and (j-e)%28==0:
            print(f"Case {n}: the next triple peak occurs in {j-d} days.")
            break