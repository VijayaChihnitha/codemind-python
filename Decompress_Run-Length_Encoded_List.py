n=int(input())
a=list(map(int,input().split()))
f=[]
b=[]
for i in range(len(a)):
    if i%2==0:
        f.append(a[i])
    else:
        b.append(a[i])
d=[]
for i in range(len(f)):
    c=f[i]
    while (c):
        d.append(b[i])
        c-=1
print(*d)