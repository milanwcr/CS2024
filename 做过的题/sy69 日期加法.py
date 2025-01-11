from datetime import datetime,timedelta
x,y,z=map(int ,input().split('-'))
a=int(input())
dt=datetime(x,y,z)
t=dt+timedelta(days=a)
print(t.strftime("%Y-%m-%d"))