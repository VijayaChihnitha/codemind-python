def spy(num):
    sums=0
    product=1
    while num>0:
        digit=num%10
        sums=sums+digit
        product=product*digit
        num=num//10
    if sums==product:
        return True
    else:
        return False
#driver code
num=int(input())
if(spy(num)):
    print("Spy Number")
else:
    print("Not Spy Number")