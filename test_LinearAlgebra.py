import unittest
import pytest
from hypothesis import given, example
import hypothesis.strategies as st
from LinearAlgebra import Vector, Matrix, dot_product, matrix_transpose, matrix_inverse, matrix_multiply


@given(st.floats(), st.floats(), st.floats())
def test_vector(x, y, z):
    assert Vector(x*2, y*2) == Vector(x, y) * 2
    assert Vector(6, 5) == Vector(5, 1) + Vector(1, 4)


def test_matrix_scaler_multiply():
    mat = Matrix(Vector(1, 2), Vector(10, 4))
    assert Matrix(Vector(2, 4), Vector(20, 8)) == mat * 2


def test_Matrix_matrix_multiply():
    mat = Matrix(Vector(1, 2), Vector(10, 4))
    assert Matrix(Vector(21, 10), Vector(50, 36)) == matrix_multiply(mat, mat)


def test_Matrix_get_item():
    mat = Matrix(Vector(1, 2), Vector(10, 4))
    assert 4 == mat[1][1]


def test_matrix_get_dimensions():
    mat = Matrix(Vector(1, 2), Vector(10, 4))
    assert Vector(2, 2) == mat.get_dimensions()


def test_dot_product():
    vec_1 = Vector(5, 4, 7)
    vec_2 = Vector(4, 4, 6)
    vec_r = dot_product(vec_1, vec_2)
    assert vec_r == 78


def test_matrix_transpose():
    mat_1 = Matrix(Vector(5, 4), Vector(7, 6))
    assert Matrix(Vector(5, 7), Vector(4, 6)) == matrix_transpose(mat_1)
    mat_2 = Matrix(Vector(1, 2, 3), Vector(4, 5, 6))
    assert Matrix(Vector(1, 4), Vector(2, 5), Vector(3, 6)) == matrix_transpose(mat_2)
