while True:
    try:

        year = int(input())
        ans = 0
        if year % 4 == 0:
            ans = 1
            if year % 100 == 0:
                ans = 0
                if year % 400 == 0:
                    ans = 1
        if ans == 1:
            print("Bissextile Year")
        else:
            print("Common Year")
    except:
        break