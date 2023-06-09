n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if a[i]==k:
        c=1
    elif b[i]==k:
        c=1
    elif a[i]<k and b[i]>k:
        c+=1
    else:
        continue
print(c)