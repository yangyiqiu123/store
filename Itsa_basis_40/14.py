while True:
    try:
        str = input()
        if len(str) % 2 == 0:
            # print(str[:len(str)//2])
            # print(str[len(str)//2:][::-1])
            if str[: len(str) // 2] == str[len(str) // 2 :][::-1]:
                print("YES")
            else:
                print("NO")
        else:
            # print(str[:len(str)//2])
            # print(str[len(str)//2+1:][::-1])
            if str[: len(str) // 2] == str[len(str) // 2 + 1 :][::-1]:
                print("YES")
            else:
                print("NO")

    except:
        break
