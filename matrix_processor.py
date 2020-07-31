class MatrixProcessor:
    OPTIONS = ["0", "1", '2', '3']

    def __init__(self):
        self.action = None

    @staticmethod
    def check_input(option):
        return option in MatrixProcessor.OPTIONS

    def same_dimensions(self, n_rows_a, n_columns_a, n_rows_b, n_columns_b):
        return n_rows_a == n_rows_b and n_columns_a == n_columns_b

    def mul_dimensions(self, n_columns_a, n_rows_b):
        return n_columns_a == n_rows_b

    def addition(self, mat_a, mat_b, n_rows, n_columns):
        return [[str(mat_a[i][j] + mat_b[i][j]) for j in range(n_columns)] for i in range(n_rows)]

    def scalar_multiplication(self, mat, scalar):
        return [list(map(lambda x: x * scalar, mat[i])) for i in range(len(mat))]

    def dot_product(self, mat_a, mat_b, n_columns_a, n_rows_a, n_columns_b):
        return [[sum([mat_a[k][j] * mat_b[j][i] for j in range(n_columns_a)]) for i in range(n_columns_b)] for k in
                range(n_rows_a)]

    def print_matrix(self, mat):
        for row in mat:
            print(*row)

    def binary_operation_input(self):
        a, b = list(map(int, input("Enter size of first matrix:").split()))
        print("Enter first matrix:")
        mat_a = [list(map(float, input().split())) for _ in range(a)]
        c, d = list(map(int, input("Enter size of second matrix:").split()))
        print("Enter second matrix:")
        mat_b = [list(map(float, input().split())) for _ in range(c)]

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
        a, b = list(map(int, input("Enter size of matrix:").split()))
        mat_a = [list(map(float, input("").split())) for _ in range(a)]
        scalar = float(input())

        return self.scalar_multiplication(mat_a, scalar)

    def menu(self):
        while True:
            print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
            choice = input('Your choice:')
            res_mat = None
            if MatrixProcessor.check_input(choice):
                self.action = choice
                if self.action == '0':
                    exit()
                elif self.action == '1':
                    res_mat = self.add_matrices()
                elif self.action == '2':
                    res_mat = self.multiply_by_constant()
                elif self.action == '3':
                    res_mat = self.multiply_matrices()
                print("The result is:")
                self.print_matrix(res_mat)
            else:
                raise ValueError('This option doesnt exist')


if __name__ == '__main__':
    my_matrix_processor = MatrixProcessor()
    my_matrix_processor.menu()
