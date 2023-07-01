while True:
    try:
        num = list(map(int, input().split()))
        n = len(num) / 2
        dict = {}

        for i in num:
            if i not in dict.keys():
                dict[i] = 1
            else:
                dict[i] += 1

        new = sorted(dict, key=lambda x: dict[x])
        # print(new)
        if dict[new[-1]]>n:
            print(new[-1])
        else:
            print("NO")
    except:
        break