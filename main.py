import pandas as pd


def pairing(n1, n2):
    if n1 == "C" and n2 == "G":
        return True
    elif n1 == "G" and n2 == "C":
        return True
    elif n1 == "A" and n2 == "U":
        return True
    elif n1 == "U" and n2 == "A":
        return True
#     elif n1 == "U" and n2 == "G":
#         return True
#     elif n1 == "G" and n2 == "U":
#         return True
    return False


def max_value(matrix, col, row):
    max_value = [0, 0]
    for k in range(col, row):
        if matrix[col][k] + matrix[k + 1][row] > max_value[0]:
            max_value[0] = matrix[col][k] + matrix[k + 1][row]
            max_value[1] = k
    return max_value


def InitFillMatrix(sequence):
    length = len(sequence)
    matrix = [[0 for x in range(length)] for y in range(length)]
    notations = [['' for h in range(len(sequence))] for y in range(len(sequence))]  # initializing notation matrix
    LstBifurcations = []
    maxK = 0
    valueBifur = 0
    valueMax = 0
    for i in range(1, len(sequence)):
        for j in range(len(sequence) - i):
            row = i + j
            if row - j >= 0:
                valueMax = max_value(matrix, j, row)
                diagcell = matrix[j + 1][row - 1] + int(pairing(sequence[j], sequence[row]))
                matrix[j][row] = max(matrix[j + 1][row], matrix[j][row - 1], diagcell, valueMax[0])

                if matrix[j][row] == matrix[j][row - 1]:  # left
                    notations[j][row] = '-'
                elif matrix[j][row] == matrix[j + 1][row]:  # bottom
                    notations[j][row] = '|'
                elif matrix[j][row] == diagcell:  # diagonally
                    notations[j][row] = '//'
                elif matrix[j][row] == valueMax[0]:  # if the maximum was the value of k
                    notations[j][row] = valueMax[1]
            else:
                matrix[j][row] = 0
    FRAMEMAT = pd.DataFrame(matrix, columns=list(sequence), index=list(sequence), dtype=int)
    FRAMENOTATIONS = pd.DataFrame(notations, columns=list(sequence), index=list(sequence))
    print(FRAMEMAT)
    print(FRAMENOTATIONS)
    return notations


# sequence = input("Enter the sequence: ")
# """matrix,NOTATION=InitFillMatrix(sequence)
# for i in range(len(sequence)):
#     for j in range(len(sequence)):
#         if not j + 1 == len(sequence):
#             print(matrix[i][j], ',', end="")
#
#         else:
#             print(matrix[i][j])
# """
# print(InitFillMatrix(sequence))

# print(InitFillMatrix("GGGAAAUCC"))
print(InitFillMatrix("CGGACCCAGACUUUC"))
sequence = "CGGACCCAGACUUUC"
list = InitFillMatrix(sequence)
list2 = ["." for x in range(0, len(sequence))]
# print(list)
# k = 5
i = 0
j = len(sequence) - 1


def tracback(i, j):
    while i != j and i - 1 != j:
        if list[i][j] == "//":
            list2[i] = "("
            list2[j] = ")"
            i += 1
            j -= 1

        elif list[i][j] == "|":
            i += 1
        elif list[i][j] == "-":
            j -= 1
        elif int(list[i][j]):
            x = i
            k = list[i][j]
            y = k
            tracback(x, y)
            x = k + 1
            y = j
            tracback(x, y)
            break


tracback(i, j)
print(list2)
