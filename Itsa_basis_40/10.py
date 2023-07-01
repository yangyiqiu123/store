def gcd(x,y):
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)
while True:
    try:
                
        x,y=map(int,input().split())
        print(gcd(x,y))
    except:
        break