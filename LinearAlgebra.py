
class Vector(list):
    def __init__(self, *args):
        for num in args:
            self.append(num)

    def __add__(self, vec):
        if len(self) != len(vec):
            raise ArithmeticError('To add two vectors they need to be of same size.')
        return_vec = Vector()
        for i in range(len(self)):
            return_vec.append(self[i] + vec[i])
        return return_vec

    def __mul__(self, scalar):
        vec = Vector()
        for e in self:
            vec.append(e * scalar)
        return vec

    def same_length_as(self, compare_vec):
        return len(self) == len(compare_vec)


class Matrix(list):
    def __init__(self, *args):
        for vec in args:
            self.append(vec)

    def get_dimensions(self):
        return Vector(len(self), len(super().__getitem__(0)))

    def __add__(self, mat):
        if self.get_dimensions() != mat.get_dimensions():
            raise ArithmeticError('Only matrices of same size can be added.')
        mat = Matrix()
        for i in range(len(self)):
            vec = Vector()
            for j in range(len(self[0])):
                vec.append(self[i][j] + mat[i][j])
            mat.append(vec)
        return mat

    def __mul__(self, scalar):
        m = self.copy()
        for i, j, e in m.get_iterator():
            m[i][j] *= scalar
        return m

    def get_iterator(self):
        for i, e in enumerate(self):
            for j, list_entry in enumerate(e):
                yield (i, j, list_entry)

    def copy(self):
        return_list = super().copy()
        m = Matrix()
        for e in return_list:
            m.append(e)
        return m

    def validate(self):
        if len(self == 0):
            return
        length = len(self[0])
        for e in self:
            if len(e) != length:
                raise Exception('Matrix has unequal length columns.')


def dot_product(vec_1, vec_2):
    if not vec_1.same_length_as(vec_2):
        raise ArithmeticError('vectors need to be of same length to calculate dot product.')
    r = 0
    for i, e in enumerate(vec_1):
        r += e * vec_2[i]
    return r


def matrix_inverse():
    pass


def matrix_transpose(mat):
    r_mat = Matrix()
    for i in range(mat.get_dimensions()[1]):
        vec = Vector()
        for j in range(mat.get_dimensions()[0]):
            vec.append(mat[j][i])
        r_mat.append(vec)
    return r_mat


def matrix_multiply(mat_1, mat_2):
    if mat_1.get_dimensions()[0] != mat_2.get_dimensions()[1]:
        raise Exception('Number of collums in matrix one doesnt match the number of rows in matrix two.')
    new_matrix = Matrix()
    for el_2 in mat_2:
        new_column = Vector()
        for el_1 in matrix_transpose(mat_1):
            new_column.append(dot_product(el_1, el_2))
        new_matrix.append(new_column)
    return new_matrix
