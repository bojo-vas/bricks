def print_matrix(num_matrix):
    num_r = len(num_matrix)
    num_c = len(num_matrix[0])
    new_r = num_r * 2 + 1
    new_c = num_c * 2 + 1

    new_matrix = [['*' for i in range(new_c)]]
    for j in range(new_r - 1):
        new_matrix.append(["*"])

    [print(x) for x in new_matrix]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(matrix)