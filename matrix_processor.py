class MatrixProcessor:
    OPTIONS = ["0", "1", '2', '3', '4', '5']

    def __init__(self):
        self.action = None

    @staticmethod
    def check_input(option):
        return option in MatrixProcessor.OPTIONS

    @staticmethod
    def same_dimensions(n_rows_a, n_columns_a, n_rows_b, n_columns_b):
        return n_rows_a == n_rows_b and n_columns_a == n_columns_b

    @staticmethod
    def mul_dimensions(n_columns_a, n_rows_b):
        return n_columns_a == n_rows_b

    @staticmethod
    def addition(mat_a, mat_b, n_rows, n_columns):
        return [[str(mat_a[i][j] + mat_b[i][j]) for j in range(n_columns)] for i in range(n_rows)]

    @staticmethod
    def scalar_multiplication(mat, scalar):
        return [list(map(lambda x: x * scalar, mat[i])) for i in range(len(mat))]

    @staticmethod
    def dot_product(mat_a, mat_b, n_columns_a, n_rows_a, n_columns_b):
        return [[sum([mat_a[k][j] * mat_b[j][i] for j in range(n_columns_a)]) for i in range(n_columns_b)] for k in
                range(n_rows_a)]

    @staticmethod
    def print_matrix(mat):
        for row in mat:
            print(*row)

    def binary_operation_input(self):
        a, b = self.get_dimensions("Enter size of first matrix:")
        mat_a = self.get_matrix(a, "Enter first matrix:")
        c, d = self.get_dimensions("Enter size of second matrix:")
        mat_b = self.get_matrix(c, "Enter second matrix:")

        return a, b, c, d, mat_a, mat_b

    def add_matrices(self):
        a, b, c, d, mat_a, mat_b = self.binary_operation_input()

        if not self.same_dimensions(a, b, c, d):
            print('ERROR')
        else:
            return self.addition(mat_a, mat_b, a, b)

    def multiply_matrices(self):
        a, b, c, d, mat_a, mat_b = self.binary_operation_input()
        if not self.mul_dimensions(b, c):
            print('ERROR')
        else:
            return self.dot_product(mat_a, mat_b, b, a, d)

    def multiply_by_constant(self):
        a, b = self.get_dimensions("Enter size of matrix:")
        mat_a = self.get_matrix(a, "Enter matrix:")
        scalar = float(input())

        return self.scalar_multiplication(mat_a, scalar)

    @staticmethod
    def get_dimensions(message):
        return list(map(int, input(message).split()))

    @staticmethod
    def get_matrix(n_rows, message):
        print(message)
        return [list(map(float, input().split())) for _ in range(n_rows)]

    @staticmethod
    def determinant(mat):
        det = 0
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        else:
            for j in range(len(mat[0])):
                sub_mat = [row[:] for row in mat]
                sub_mat.pop(0)
                for row in range(len(sub_mat)):
                    sub_mat[row].pop(j)

                det += mat[0][j] * (-1) ** (1 + j + 1) * MatrixProcessor.determinant(sub_mat)

        return det

    def get_determinant(self):
        a, b = self.get_dimensions("Enter size of matrix:")
        mat_a = self.get_matrix(a, "Enter matrix:")

        return self.determinant(mat_a)

    def get_transpose(self, choice):
        n_rows, n_cols = self.get_dimensions("Enter matrix size:")
        mat = self.get_matrix(n_rows, 'Enter matrix:')
        transposed = None
        if choice == '1':
            transposed = [[mat[i][j] for i in range(n_rows)] for j in range(n_cols)]
        if choice == '2':
            transposed = [[mat[i][j] for i in range(n_rows - 1, -1, -1)] for j in range(n_cols - 1, -1, -1)]
        if choice == '3':
            transposed = [[mat[i][j] for j in range(n_cols - 1, -1, -1)] for i in range(n_rows)]
        if choice == '4':
            transposed = [[mat[i][j] for j in range(n_cols)] for i in range(n_cols - 1, -1, -1)]

        return transposed

    def submenu_transpose(self):
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        choice = input("Your choice:")
        res_mat = None

        if choice in ['1', '2', '3', '4']:
            res_mat = self.get_transpose(choice)

        return res_mat

    def menu(self):
        res = None
        while True:
            print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
            choice = input('Your choice:')
            res_mat = None
            if MatrixProcessor.check_input(choice):
                self.action = choice
                if self.action == MatrixProcessor.OPTIONS[0]:
                    exit()
                elif self.action == MatrixProcessor.OPTIONS[1]:
                    res_mat = self.add_matrices()
                elif self.action == MatrixProcessor.OPTIONS[2]:
                    res_mat = self.multiply_by_constant()
                elif self.action == MatrixProcessor.OPTIONS[3]:
                    res_mat = self.multiply_matrices()
                elif self.action == MatrixProcessor.OPTIONS[4]:
                    res_mat = self.submenu_transpose()
                elif self.action == MatrixProcessor.OPTIONS[5]:
                    res = self.get_determinant()

                print("The result is:")
                if not res:
                    self.print_matrix(res_mat)
                else:
                    print(res)
            else:
                raise ValueError('This option doesnt exist')


if __name__ == '__main__':
    my_matrix_processor = MatrixProcessor()
    my_matrix_processor.menu()
