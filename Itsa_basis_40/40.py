while True:
    try:
        num = list(input().split())
        for i in range(len(num)):
            if num[i] == "X":
                num[i] = 10
            else:
                num[i] = int(num[i])

        ans1 = [num[0]]
        for i in range(9):
            ans1.append(num[i + 1] + ans1[i])
        ans2 = [ans1[0]]
        for i in range(9):
            ans2.append(ans1[i + 1] + ans2[i])

        if ans2[-1]%11==0:
                print("YES")
        else:
            print("NO")
    except:
        break
