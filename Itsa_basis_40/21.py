while True:
    try:
        max = -10000000
        min = 1000000000
        num = list(map(float, input().split()))
        for i in num:
            num = i
            if num > max:
                max = num
            if num < min:
                min = num

        print(f"maximum:{max:.2f}")
        print(f"minimum:{min:.2f}")
    except:
        break
