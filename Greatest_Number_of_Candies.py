n=int(input())
a=list(map(int,input().split()))
s=int(input())
b=[]
m=[]
l=max(a)
for i in a:
    b.append(i+s)
for i in b:
    if i>=l:
        m.append('True')
    else:
        m.append('False')
print(*m)