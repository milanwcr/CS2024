while True:
    try:
        l=input()
        if l[0]=='.' or l[0]=='@' or l[len(l)-1]=='.' or l[len(l)-1]=='@':
            print('NO')
            continue
        if '@' not in l:
            print('NO')
            continue
        if '@' in l[l.index('@')+1:]:
            print('NO')
            continue
        if '.' not in l[l.index('@')+1:] or l[l.index('@')+1]=='.' or l[l.index('@')-1]=='.':
            print('NO')
            continue
        print('YES')
    except EOFError:
        break