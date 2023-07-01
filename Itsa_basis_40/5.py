while True:
    try:
        num=int(input())
        ans=""
        for _ in range(8):
            ans=ans+str(num%2)
            num=num//2
        print(ans[::-1])
    except:
        break
    