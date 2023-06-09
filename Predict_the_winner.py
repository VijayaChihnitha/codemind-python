n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(0,n,2):
    s=s+a[i]
for i in range(1,n,2):
    c=c+a[i]
if abs(s-c)%4==0:
    print('X')
else:
    print('Y')