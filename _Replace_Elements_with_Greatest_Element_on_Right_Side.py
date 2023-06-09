n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if i==(len(a)-1):
        a[i]=-1
    else:
        b=[]
        for j in range(i+1,len(a)):
            b.append(a[j])
            m=max(b)
        a[i]=m
print(*a)