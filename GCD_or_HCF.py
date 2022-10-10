a,b=map(int,input().split())

def lcm(a,b):
    t=2
    res=1
    while a>=t or b>=t:
      #print(t,a,b)
      if a%t==0 and b%t==0:
        a=a//t
        b=b//t
        res=res*t
      else:
        t+=1
    return res

print(lcm(a,b))
  
    
