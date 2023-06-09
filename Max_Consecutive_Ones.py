n=int(input())
a=list(map(int,input().split()))
m=0
b=[]
for i in range(len(a)):
    c=1
    if a[i]==1:
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                c+=1
            else:
                break
        b.append(c)
for i in b:
    if  i >m:
        m=i
print(m)