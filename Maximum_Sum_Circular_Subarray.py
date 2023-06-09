n=int(input())
a=list(map(int,input().split()))
s=0
m=-99
for i in range(n):
    s=a[i]
    if s>m:
        m=s
    if a[i]==a[n-1]:
        for j in range(0,i):
            s=s+a[j]
            if s>m:
                m=s
    else:
        for j in range(i+1,n):
            s=s+a[j]
            if s>m:
                m=s
print(m)