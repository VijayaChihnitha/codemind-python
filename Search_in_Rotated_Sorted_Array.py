n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
n=0
for i in range(len(a)):
    if i==n-1:
        i=n%i
    if a[i]==b:
        c=i
        n+=1
if n==0:
    print("-1")
else:
    print(c)