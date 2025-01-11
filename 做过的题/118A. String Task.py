l=input()
for i in l:
    if i.lower()!='a' and i.lower()!='o' and i.lower()!='y' and i.lower()!='e' and i.lower()!='i' and i.lower()!='u':
        print('.'+i.lower(),end='')