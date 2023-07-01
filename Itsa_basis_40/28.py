import sys

ans = [0, 0, 0, 0, 0, 0, 0]
prize = [2000000, 200000, 40000, 10000, 4000, 1000, 200]

p = sys.stdin.readline().rstrip()
h1 = sys.stdin.readline().rstrip()
h2 = sys.stdin.readline().rstrip()
h3 = sys.stdin.readline().rstrip()


suffixes = set()
for i in [h1, h2, h3]:
    for j in range(6):
        suffixes.add(i[j:])
        
n=int(sys.stdin.readline().rstrip())


for _ in range(n):
    num = sys.stdin.readline().rstrip()

    if num == p:
        ans[0] += 1
        continue
    
    # for i in [h1, h2, h3]:
    #     for j in range(6):
    #         if i[j:] == num[j:]:
    #             ans[j + 1] += 1
    #             break
            
    # for i in range(6):
    #     p=0
    #     for j in [h1, h2, h3]:
    #         if j[i:] == num[i:]:
    #             ans[i+1]+=1
    #             p=1
    #             break
    #     if p==1:
    #         break
    
    for j in range(6):
        if num[j:] in suffixes:
            ans[j + 1] += 1
            break
    


print(*ans)

# money = 0
money = sum(prize[i] * ans[i] for i in range(7))
print(money)




# for _ in range(int(input())):
#     num = input()

#     if num == p:
#         ans[0] += 1
#         continue
#     for i in [h1, h2, h3]:
#         for j in range(6):
#             if i[j:] == num[j:]:
#                 ans[j + 1] += 1
#                 break
        # else:
        #     continue
        # break
