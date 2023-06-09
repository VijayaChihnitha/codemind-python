n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=list(map(int,input().split()))
d=[]
for i in range(n):
    d.insert(b[i],a[i])
print(*d)