# Objectives
#
# Write a program that reads a matrix and a constant and outputs the result of their multiplication.
#
# The first line of the input contains the number of rows and the number of columns of the matrix.
# Next lines contain rows of the matrix. The last line contains the constant.
#
# The constant and the elements of the matrix are integers.


def scalar_multiplication(mat, scalar):
    return [list(map(lambda x: x * scalar, mat[i])) for i in range(len(mat))]


def print_matrix(mat):
    for row in mat:
        print(*row)


def multiply_by_constant():
    a, b = list(map(int, input().split()))
    mat_a = [list(map(int, input().split())) for _ in range(a)]
    scalar = int(input())

    mat_sc = scalar_multiplication(mat_a, scalar)
    print_matrix(mat_sc)


if __name__ == '__main__':
    multiply_by_constant()
