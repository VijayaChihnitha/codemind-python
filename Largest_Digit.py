num=int(input())
max=0
while(num>0):
    remainder=num%10
    if max<remainder:
        max=remainder
    num=num//10
    
print(max)
    
