import sys



ans = [0] * 7
prize = [2000000, 200000, 40000, 10000, 4000, 1000, 200]

p = sys.stdin.readline().rstrip()
h1 = sys.stdin.readline().rstrip()
h2 = sys.stdin.readline().rstrip()
h3 = sys.stdin.readline().rstrip()
suffixes = [set(i[j:] for i in [h1, h2, h3]) for j in range(6)]

n = int(sys.stdin.readline())

numbers = {}
prev_index = [0] * 6

for _ in range(n):
    num = sys.stdin.readline().rstrip()

    if num == p:
        ans[0] += 1
    else:
        for j in range(6):
            if num[j:] in numbers.get(j, suffixes[j]):
                ans[j + 1] += 1
                prev_index[j] = len(num) - 1 - j
                break

    for j in range(6):
        if j in numbers and prev_index[j] < len(numbers[j]):
            numbers[j] = numbers[j][prev_index[j]:]

print(*ans)
money = sum(prize[i] * ans[i] for i in range(7))
print(money)
