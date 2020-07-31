def mul_dimensions(n_columns_a, n_rows_b):
    return n_columns_a == n_rows_b


def dot_product(mat_a, mat_b, n_columns_a, n_rows_a, n_columns_b):
    return [[sum([mat_a[k][j] * mat_b[j][i] for j in range(n_columns_a)]) for i in range(n_columns_b)] for k in
            range(n_rows_a)]


def print_matrix(mat):
    for row in mat:
        print(*row)


def mul_matrices():
    a, b = list(map(int, input().split()))
    mat_a = [list(map(int, input().split())) for _ in range(a)]
    c, d = list(map(int, input().split()))
    mat_b = [list(map(int, input().split())) for _ in range(c)]

    if not mul_dimensions(b, c):
        print('ERROR')
    else:
        mat_sum = dot_product(mat_a, mat_b, b, a, d)
        for row in mat_sum:
            print(*row)


if __name__ == '__main__':
    mul_matrices()
