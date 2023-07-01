while True:
    try:
        num_of_decks = int(input())
        for _ in range(num_of_decks):
            cards = input().split()
            suits = {'S': [], 'H': [], 'D': [], 'C': []}

            for card in cards:
                suit = card[0]
                number = int(card[1:])
                suits[suit].append(number)

            sorted_cards = []
            for suit in ['S', 'H', 'D', 'C']:
                if suits[suit]:
                    sorted_cards.extend([suit + str(card) for card in sorted(suits[suit], reverse=True)])
            # print(sorted_cards)
            print(' '.join(sorted_cards))
    except:
        break


# while True:
#     try:
#         for g in range(int(input())):
#             card = list(input().split())
#             # S>H>D>C

#             s = []
#             h = []
#             d = []
#             c = []
#             # for _ in range(12):
#             #     s,h,d,c.append(0)
#             for i in range(len(card)):
#                 if card[i][0] == "S":
#                     s.append(card[i][1:])
#                 if card[i][0] == "H":
#                     h.append(card[i][1:])
#                 if card[i][0] == "D":
#                     d.append(card[i][1:])
#                 if card[i][0] == "C":
#                     c.append(card[i][1:])

#             s = list(map(int, s))
#             h = list(map(int, h))
#             d = list(map(int, d))
#             c = list(map(int, c))

#             s.sort(reverse=True)
#             h.sort(reverse=True)
#             d.sort(reverse=True)
#             c.sort(reverse=True)

#             if len(s) != 0:
#                 print("S", end="")
#                 print(*s, sep=" S", end="")
#                 print("", end="")
#             if len(h) != 0:
#                 if len(s)!=0:
#                     print(' ', end="")
                
#                 print("H", end="")
#                 print(*h, sep=" H", end="")
#                 # print("", end="")
#             if len(d) != 0:
#                 if len(s)!=0 or len(h)!=0:
#                     print(' ', end="")
                
#                 print("D", end="")
#                 print(*d, sep=" D", end="")
#                 # print("", end="")
#             if len(c) != 0:
#                 if len(s)!=0 or len(h)!=0 or len(d)!=0:
                    
#                     print(' ', end="")
#                 print("C", end="")
#                 print(*c, sep=" C", end="")
#                 # print("", end="")
#             print()
#     except:
#         break
