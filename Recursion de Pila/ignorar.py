def fibo(x):
    a=1
    b=1
    c=1
    d=0
    while a<=(x+2):
        d=b+c
        b=d+c
        c=c+b
        a+=3
    print(c)
    
        
