for i in range(int(input())):
    n = list(input().split())
    w = n[0]
    num = list(map(int, n[1:5]))

    # print(n)
    # print(p)
    # print(num)

    i = 0
    j = 0
    # 0 1 2 3
    a1 = num[0]
    a2 = num[1]
    b1 = num[2]
    b2 = num[3]
    if w == '+':
          print((a1+b1), (a2+b2))
    elif w == '-':
        print((a1-b1), (a2-b2))
    elif w == '*':
        print((a1*b1-a2*b2), (a2*b1+a1*b2))
    elif w == '/':
        print(((a1*b1+a2*b2)/(b1*b1+b2*b2), (a2*b1-a1*b2)/(b1*b1+b2*b2)))
