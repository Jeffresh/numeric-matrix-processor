def print_matrix(mat):
    for row in mat:
        print(*row)


def get_dimensions(message):
    return list(map(int, input(message).split()))


def get_matrix(n_rows, message):
    print(message)
    return [list(map(float, input().split())) for _ in range(n_rows)]


def scalar_multiplication(mat, scalar):
    return [list(map(lambda x: x * scalar, mat[i])) for i in range(len(mat))]


def get_minor(mat, row, column):
    sub_mat = [row[:] for row in mat]
    sub_mat.pop(row)
    for row in range(len(sub_mat)):
        sub_mat[row].pop(column)
    return sub_mat


def get_adj_mat(mat):
    adj = []

    for i in range(len(mat)):
        adj.append([(-1) ** ((i + 1) + j + 1) * determinant(get_minor(mat, i, j)) for j in range(len(mat[0]))])

    return adj


def determinant(mat):
    det = 0
    if len(mat) == 1:
        return mat[0][0]
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:
        for j in range(len(mat[0])):
            det += mat[0][j] * (-1) ** (1 + j + 1) * determinant(get_minor(mat, 0, j))

    return det


def transpose(mat):
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]


def inverse(mat):
    return scalar_multiplication(transpose(get_adj_mat(mat)), 1 / determinant(mat))


if __name__ == '__main__':
    a, b = get_dimensions("Enter size of first matrix:")
    mat_a = get_matrix(a, "Enter first matrix:")

    adj_mat = get_adj_mat(mat_a)

    print('ad matrix')
    print(adj_mat)

    inverse_mat = inverse(mat_a)
    print('inv matrix')
    print_matrix(inverse_mat)
