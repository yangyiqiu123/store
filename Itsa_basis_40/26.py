def compare(a):
    a_plus = 0

    for i in str(a):
        a_plus += int(i)
    return (a_plus, a)

n = int(input())
num = list(map(int, input().split()))

num = sorted(num, key=compare)
print(*num)

# ------------------------------------------------------------------------------

# def sum_digit(x):
#     sum = 0
#     for digit in str(x):
#         sum += int(digit)
#     return sum


# n = int(input())
# num = list(map(int, input().split(" ")))

# sort = []
# for j in range(n):
    
#     temp = num[0]
    
#     for i in num:
        
#         if sum_digit(i) <= sum_digit(temp):
#             if sum_digit(i) != sum_digit(temp):
#                 temp = i
#             elif temp > i:
#                 temp = i
                
#     num = num[:num.index(temp)]+num[num.index(temp)+1:]
#     sort.append(temp)

# print(*sort, sep=" ")

# ------------------------------------------------------------------------------

# def get_digit_sum(n):
#     return sum(int(digit) for digit in str(n))

# N = int(input())
# numbers = list(map(int, input().split()))

# numbers = sorted(numbers, key=lambda x: (get_digit_sum(x), x))


# print(*numbers, sep=" ")


