str1 = input()
n = int(input())

new_str = ""
for i in str1:
    if (ord(i) >= ord("a") and ord(i) <= ord("z")) or (ord(i) >= ord("A") and ord(i) <= ord("Z")):
        b = ord(i) + n 
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            if b > ord("z"):
                b -= 26
        elif ord(i) >= ord("A") and ord(i) <= ord("Z"):
            if b > ord("Z"):
                b -= 26
        new_str += chr(b)
    elif (ord(i) >= ord("0") and ord(i) <= ord("9")):
        new_str += str((int(i)+n)%10)
    else:
        new_str += i
print(new_str)
