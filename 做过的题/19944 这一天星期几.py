n=int(input())
w=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i in range(n):
    l=input()
    c=int(l[0:2])
    y=int(l[2:4])
    m=int(l[4:6])
    d=int(l[6:8])
    if m<=2:
        m+=12
        if y==0:
            y=99
            c-=1
        else:
            y-=1
    print(w[(y+y//4+c//4-2*c+d-1+(26*(m+1))//10)%7])