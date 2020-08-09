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

            det += mat[0][j] * (-1) ** (1 + j + 1) * determinant(sub_mat)

    return det
