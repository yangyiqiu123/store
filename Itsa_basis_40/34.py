while True:
    try:
        h, s = map(int, input().split())
        if s == 1:
            print(f"{(h-80)*0.7:.1f}")
        else:
            print(f"{(h-70)*0.6:.1f}")

    except:
        break
