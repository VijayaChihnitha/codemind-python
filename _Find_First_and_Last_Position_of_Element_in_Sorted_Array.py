n=int(input())
a=list(map(int,input().split()))
s=int(input())
b=[]
for i in range(0,n):
    if a[i]==s:
        b.append(i)
        break
else:
    b.append(-1)
for i in range(n-1,-1,-1):
    if a[i]==s:
        b.append(i)
        break
else:
    b.append(-1)
print(*b)