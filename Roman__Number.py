n=int(input())
num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
rom=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
i=12
while n:
    d=n//num[i]
    n%=num[i]
    while d:
        print(rom[i],end="")
        d-=1
    i-=1