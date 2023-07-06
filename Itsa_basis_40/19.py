# rc = int(input())
# time = list(map(int, input().split()))
# time2 = []
# for i in range(1, len(time), 2):
#     time2.append([time[i-1], time[i]-time[i-1]])
# time2 = sorted(time2, key=lambda x: x[1])
# # print(time2)
# ans = 0
# while len(time2) != 0:
#     remove = []
#     count = time2[0][0] + time2[0][1]
#     remove.append(time2[0])
#     for i in range(1, len(time2)):
#         if time2[i][0] >= count:
#             count += time2[i][1]
#             remove.append(time2[i])
#     new = []
#     for i in time2:
#         if i not in remove:
#             new.append(i)
#     time2 = new
#     ans += 1
# print(ans)


# n = int(input())
# times = list(map(int, input().split()))

# events = []
# for i in range(0, len(times), 2):
#     events.append((times[i], 1))
#     events.append((times[i + 1], -1))
# events.sort()

# current_tasks = 0
# max_tasks = 0
# for event in events:
#     current_tasks += event[1]
#     max_tasks = max(max_tasks, current_tasks)

# print(max_tasks)


while True:
    try:
        order = int(input())
        time = list(map(int, input().split()))
        cars = order

        for i in range(0, len(time), 2):
            for j in range(1, len(time), 2):
                if time[i] - time[j] >= 0:
                    time[j] = time[i + 1]

                    cars -= 1

                    break

        if cars == 0:
            print(1)
        else:
            print(cars)
    except EOFError:
        break
