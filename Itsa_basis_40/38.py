summer = [2.10, 3.02, 4.39, 4.97, 5.63]
unsummer = [2.10, 2.68, 3.61, 4.01, 4.50]


summer = 0
unsummer = 0

num = int(input())
for i in range(1,num+1):
    if i <= 120:
        summer += 2.10
        unsummer += 2.10
    elif i >= 121 and i <= 330:
        summer += 3.02
        unsummer += 2.68
    elif i >= 331 and i <= 500:
        summer += 4.39
        unsummer += 3.61
    elif i >= 501 and i <= 700:
        summer += 4.97
        unsummer += 4.01
    elif i >= 701:
        summer += 5.63
        unsummer += 4.50
print(f"Summer months:{summer:.2f}")
print(f"Non-Summer months:{unsummer:.2f}")
