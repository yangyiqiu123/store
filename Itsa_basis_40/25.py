for _ in range(int(input())):
    str = input()
    ans = 0
    for i in str:
        ans += ord(i)
    print(ans)