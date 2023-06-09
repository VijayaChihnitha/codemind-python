n=int(input())
a=list(map(int,input().split()))
ec=0
for i in range(len(a)):
    c=0
    while(a[i]>0):
        d=a[i]%10
        a[i]=a[i]//10
        c+=1
    if c%2==0:
        ec+=1
print(ec)