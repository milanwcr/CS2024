n=int(input())
l={i**3 : i for i in range(2,n+1)}
ans=[]
for b in range(2,n+1):
    for c in range(b,n+1):
        for d in range(c,n+1):
            if (b**3+c**3+d**3) in l:
                ans.append((l[b**3+c**3+d**3],b,c,d))
ans.sort()
for s in ans:
    print(f"Cube = {s[0]}, Triple = ({s[1]},{s[2]},{s[3]})")