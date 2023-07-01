month,day=map(str, input().split())
num = int(month+day)
if num>=121 and num<=218:
    print("Aquarius")
elif num>=219 and num<=320:
    print("Pisces")
elif num>=321 and num<=420:
    print("Aries")
elif num>=421 and num<=521:
    print("Taurus")
elif num>=522 and num<=621:
    print("Gemini")
elif num>=622 and num<=722:
    print("Cancer")
elif num>=723 and num<=823:
    print("Leo")
elif num>=824 and num<=923:
    print("Virgo")
    
elif num>=924 and num<=1023:
    print("Libra")
elif num>=1024 and num<=1122:
    print("Scorpio")
elif num>=1123 and num<=1221:
    print("Sagittarius")
else:
    print("Capricorn")