ans = input()
while True:
    num = input()
    a = 0
    b = 0
    if num == "0000":
        break
    else:
        for i in range(4):
            if num[i] == ans[i]:
                a += 1
            elif num[i] in ans :
                b += 1

            

    print(f"{a}A{b}B")
