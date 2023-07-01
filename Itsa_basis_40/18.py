keyboard = "  ~!@#$%^&*()_+  1234567890-=  qwertyuiop[]  asdfghjkl;'` \\zxcvbnm,./  QWERTYUIOP{}|  ASDFGHJKL:\"  ZXCVBNM<>?"
# keyboard = "  1234567890-=  qwertyuiop[]  asdfghjkl;'` \\zxcvbnm,./ "
str = input().lower()

ans = ""
for char in str:
    i = keyboard.find(char)
    if i != -1:
        if i < len(keyboard) - 1:
            ans += keyboard[i + 1]
        else:
            ans += char
    else:
        ans += char

print(ans)
