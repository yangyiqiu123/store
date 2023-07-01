while True:
    try:
        num=int(input())
        ans=0
        for i in range(1,num+1):
            if i%3==0:
                ans+=i
        print(ans)
        
    except:
        break