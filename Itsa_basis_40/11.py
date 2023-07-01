while True:
    try:
        # import numpy as np
        row, column = map(int, input().split())
        # matrix = np.zeros((row,column))
        matrix = []
        for i in range(row):
            matrix.append(list(map(int, input().split())))

        for i in range(column):
            for j in range(row):
                print(matrix[j][i], end="")
                if j < row-1:
                    print(' ', end="")
            print()
    except EOFError:
        break

# for i in range(column):
#     for j in range(row):
#         print
