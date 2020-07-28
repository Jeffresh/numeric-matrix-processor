# Objectives
#
# In this stage, you should write a program that:
#
#     Reads matrix A A A from the input.
#     Reads matrix B B B from the input.
#     Outputs their sum if it is possible to add them. Otherwise, it should output the ERROR message.
#
# Each matrix in the input is given in the following way: the first line contains the number of rows
# nnn and the number of columns mmm. Then nnn lines follow, each containing mmm integers representing one row of the matrix.
#
# Output the result in the same way but don't print the dimensions of the matrix.


if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    mat_a = [list(map(int, input().split())) for _ in range(a)]
    c, d = list(map(int, input().split()))
    mat_sum = []
    mat_b = [list(map(int, input().split())) for _ in range(c)]

    if a != c or b != d:
        print('ERROR')
    else:
        mat_sum = [[str(mat_a[i][j] + mat_b[i][j]) for j in range(b)] for i in range(a)]
        for row in mat_sum:
            print(*row)
