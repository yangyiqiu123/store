while True:
    try:
        x,y=map(int,input().split())
        if (x)**2+(y)**2<=200**2:
            print("inside")
        else:
            print("outside")

    except:
        break