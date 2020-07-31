# Objectives
#
# In this stage, you should write a program that:
#
#     Reads matrix A A A from the input.
#     Reads matrix B B B from the input.
#     Outputs their sum if it is possible to add them. Otherwise, it should output the ERROR message.
#
# Each matrix in the input is given in the following way: the first line contains the number of rows
# nnn and the number of columns mmm. Then nnn lines follow, each containing mmm integers
# representing one row of the matrix.
#
# Output the result in the same way but don't print the dimensions of the matrix.


def same_dimensions(n_rows_a, n_columns_a, n_rows_b, n_columns_b):
    return n_rows_a == n_rows_b and n_columns_a == n_columns_b


def addition(mat_a, mat_b, n_rows, n_columns):
    return [[str(mat_a[i][j] + mat_b[i][j]) for j in range(n_columns)] for i in range(n_rows)]


def print_matrix(mat):
    for row in mat:
        print(*row)


if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    mat_a = [list(map(int, input().split())) for _ in range(a)]
    c, d = list(map(int, input().split()))
    mat_b = [list(map(int, input().split())) for _ in range(c)]

    if not same_dimensions(a, b, c, d):
        print('ERROR')
    else:
        mat_sum = addition(mat_a, mat_b, a, b)
        for row in mat_sum:
            print(*row)
