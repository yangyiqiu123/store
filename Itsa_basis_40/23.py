money, a1, a2, a3 = map(int,input().split(','))
money=money-(15*a1)-(20*a2)-(30*a3)
if money > 0:
    l50 = money//50
    money = money % 50
    l5 = money//5
    money = money % 5
    l1 = money//1
    money = money % 1
    print(f"{l1},{l5},{l50}")
else:
    print("0")