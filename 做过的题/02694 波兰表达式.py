def cal():
    x=l.pop(0)
    if x in a:
        return str(eval(cal()+x+cal()))
    else:
        return x

l=input().split()
a=['*','+','-','/']
print('{:.6f}'.format(float(cal())))