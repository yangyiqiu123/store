while True:
    try:
        for _ in range(int(input())):
            t,m,k=map(int,input().split())
            pri=list(map(int,input().split()))
            pri = sorted(pri)
            # print(pri)
            s = sum(x for x in pri[:m])
            if s<=t:
                print(s)
            else:
                print("Impossible")
    except:
        break
    