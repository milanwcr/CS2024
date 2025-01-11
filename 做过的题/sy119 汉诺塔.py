def move(m,x,y):
    if m==1:
        return [f'{a[x]}->{a[y]}']
    return move(m-1,x,3-x-y)+[f'{a[x]}->{a[y]}']+move(m-1,3-x-y,y)

n=int(input())
a=['A','B','C']
ans=move(n,0,2)
print(len(ans))
print('\n'.join(ans))