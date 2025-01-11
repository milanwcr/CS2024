l=input()
for i in range(len(l)):
    if 'a'<=l[i]<='z':
        print(l[i].upper(),end='')
        continue
    if 'A'<=l[i]<='Z':
        print(l[i].lower(),end='')
        continue
    print(l[i],end='')