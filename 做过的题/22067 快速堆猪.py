pig,minn=[],[]
while True:
    try:
        s=input()
        if s=='pop' and pig:
            pig.pop()
            minn.pop()
        if s=='min' and pig:
            print(minn[-1])
        if s[:4]=='push':
            pig.append(int(s[5:]))
            if not minn:
                minn.append(pig[-1])
            else:
                m=minn[-1]
                minn.append(min(m,pig[-1]))

    except EOFError:
        break