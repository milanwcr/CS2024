while True:
    try:
        s=input()
        f=1
        for i in range(2,len(s)+1):
            for j in range(len(s)-1,-1,-1):
                if int(s)*(i*(10**(len(s)-j))-1)==(10**(len(s))-1)*int(s[j:]):
                    f+=1
                    break
            if f!=i:
                print(f'{s} is not cyclic')
                break
        if f==len(s):
            print(f'{s} is cyclic')
    except EOFError:
        break