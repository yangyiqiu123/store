a1,a2=map(int,input().split())
b1,b2=map(int,input().split())

h=((b1*60+b2)-(a1*60+a2))//30

ans=0
for i in range(1,h+1):
    # if i<=1:
    #     ans+=0
    if  i<=4:
        ans+=30
    elif i>4 and i<=8:
        ans+=40
    else:
        ans+=60
print(ans)