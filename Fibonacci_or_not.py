def fib(num):
    a = 0
    b = 1
    while b<num:
        c = a+b
        a = b
        b = c
    if b==num or a==num:
        return True
    if b > num:
        return False

num = int(input())
if fib(num):
    print("True")
else:
    print("False")