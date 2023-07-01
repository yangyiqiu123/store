dict = {}
letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "X",
    "Y",
    "W",
    "Z",
    "I",
    "O",
]
for i, j in zip(letters, [x for x in range(10, 36)]):
    dict[i] = j

n = input()


num = (
    dict[n[0]] // 10
    + (9 * (dict[n[0]] % 10))
    + (8 * int(n[1]))
    + (7 * int(n[2]))
    + (6 * int(n[3]))
    + (5 * int(n[4]))
    + (4 * int(n[5]))
    + (3 * int(n[6]))
    + (2 * int(n[7]))
    + int(n[8])
    + int(n[9])
)
if num % 10 == 0:
    print("CORRECT!!!")
else:
    print("WRONG!!!")
