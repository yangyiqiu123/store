r=float(input())
n = int(input())
p = int(input())

ans = 0

for i in range(n):
    ans = ans + p
    ans = ans + r*ans
    
print(int(ans))