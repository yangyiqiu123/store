while True:
    try:
        num=int(input())
        j=0
        for i in range(2,num):
            if num%i==0:
                print("NO")
                j=1
                break
        if j==0:
            print("YES")
    except:
        break