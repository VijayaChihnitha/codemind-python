n=int(input())
a=list(map(int,input().split()))
s=int(input())
b=list(map(int,input().split()))
c=0
for i in a:
    if i not in b:
        c=1
        break
for i in b:
    if i not in a:
        c=1
        break
if c==0:
    print('True')
else:
    print('False')