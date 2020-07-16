from matrix_class import Matrix
import sys
sys.path.append('src')

print('Testing...')

add_1 = Matrix(elements=[[1, 1], [0, 1]])
add_2 = Matrix(elements=[[1, 1], [0, 1]])
result = add_1 + add_2

assert result.elements = [[2, 2], [0, 2]], 'Addition was wrong, should be [[2, 2], [0, 2]], but was {}'.format(result.elements)
print('Addition Passed!')

sub_1 = Matrix(elements=[[1, 1], [0, 1]])
sub_2 = Matrix(elements=[[1, 1], [0, 1]])
result = sub_1 - sub_2

assert result.elements = [[0, 0], [0, 0]], 'Subtraction was wrong, should be [[0, 0], [0, 0]], but was {}'.format(result.elements)
print('Subtraction Passed!')

scal_mult = Matrix(elements=[[1, 1], [0, 1]])
scalar = 2
result = scal_mult * scalar

assert result.elements = [[2, 2], [0, 2]], 'Scalar multiplication was wrong, should be [[2, 2], [0, 2]], but was {}'.format(result.elements)
print('Scalar multiplication Passed!')

mat_mult_1 = Matrix(elements=[[1, 1], [0, 0]])
mat_mult_2 = Matrix(elements=[[0, 0], [1, 1]])
result = mat_mult_1 @ mat_mult_2

assert result.elements = [[0, 0], [0, 0]], 'Matrix Multiplication was wrong, should be [[0, 0], [0, 0]], but was {}'.format(result.elements)
print('Matrix Multiplication Passed!')

trans = Matrix(elements=[[1, 1], [0, 1]])
result = trans.transpose()

assert result.elements = [[1, 0], [1, 1]], 'Transpose was wrong, should be [[1, 0], [1, 1]], but was {}'.format(result.elements)
print('Transpose Passed!')

RREF_1 = Matrix(elements=[[1, 1], [0, 1]])
result = RREF_1.rref()

assert result.elements = [[1, 2], [3, 7]], 'RREF #1 was wrong, should be [[1, 0], [0, 1]], but was {}'.format(result.elements)
print('RREF #1 Passed!')

RREF_2 = Matrix(elements=[[1, 1], [0, 1], [2, 3]])
result = RREF_2.rref()

assert result.elements = [[1, 0], [0, 1], [0, 0]], 'RREF #2 was wrong, should be [[1, 0], [0, 1], [0, 0]], but was {}'.format(result.elements)
print('RREF #2 Passed!')

RREF_3 = Matrix(elements=[[1, 1, 2], [0, 1, 3]])
result = RREF_3.rref()

assert result.elements = [[1, 0, -1], [0, 1, 3], 'RREF #3 was wrong, should be [[1, 0, -1], [0, 1, 3]], but was {}'.format(result.elements)
print('RREF #3 Passed!')

RREF_4= Matrix(elements=[[3, 1, 2], [0, 2, 3]])
result= RREF_4.rref()

assert result.elements= [[1, 0, 0.16], [0, 1, 1.5]], 'RREF #4 was wrong, should be [[1, 0, 0.16], [0, 1, 1.5]], but was {}'.format(result.elements)
print('RREF #4 Passed!')

RREF_5= Matrix(elements=[[1, 1, 2], [0, 1, 3]])
result= RREF_5.rref()

assert result.elements= [[1, 0, -1], [0, 1, 3], 'RREF #5 was wrong, should be [[1, 0, -1], [0, 1, 3]], but was {}'.format(result.elements)
print('RREF #5 Passed!')

RREF_6= Matrix(elements=[[1, 2, 3], [4, 5, 6]])
result= RREF_6.rref()

assert result.elements = [[1, 0, -1], [0, 1, 2]], 'RREF #6 was wrong, should be [[1, 0, -1], [0, 1, 2]], but was {}'.format(result.elements)
print('RREF #6 Passed!')

inv_1= Matrix(elements=[[-3, 1], [5, 0]])
result= inv.inverse()

assert result.elements= [[[0, 0.2], [1, 0.6]], 'Iverse #1 was wrong, should be [[[0, 0.2], [1, 0.6]], but was {}'.format(result.elements)
print('Inverse #1 Passed!')

inv_1= Matrix(elements=[[-3, 1], [5, 0]])
result= inv_1.inverse()

assert result.elements= [[[0, 0.2], [1, 0.6]], 'Iverse #1 was wrong, should be [[[0, 0.2], [1, 0.6]], but was {}'.format(result.elements)
print('Inverse #1 Passed!')

inv_2= Matrix(elements=[[-3, 1, 0], [5, 0, 0]])
result= inv_2.inverse()

assert result= 'ERROR: Matrix is not Invertible. Please give a Invertible matrix', "Inverse #2 was inverted, but it shouldn't be inverted, but was {}".format(result)
print('Inverse #2 Passed!')

inv_3= Matrix(elements=[[1, 2], [2, 4]])
result= inv_3.inverse()

assert result= 'ERROR: Matrix is not Invertible. Please give a Invertible matrix', "Inverse #3 was inverted, but it shouldn't be inverted, but was {}".format(result)
print('Inverse #3 Passed!')

inv_by_minors_1= Matrix(elements=[[-3, 1], [5, 0]])
result= inv_by_minors_1.inverse_by_minors()

assert result.elements= [[[0, 0.2], [1, 0.6]], 'Iverse #1 was wrong, should be [[[0, 0.2], [1, 0.6]], but was {}'.format(result.elements)
print('Inverse #1 Passed!')

inv_by_minors_2= Matrix(elements=[[-3, 1, 0], [5, 0, 0]])
result= inv_by_minors_2.inverse_by_minors()

assert result= 'ERROR: Matrix is not Invertible. Please give a Invertible matrix', "Inverse #2 was inverted, but it shouldn't be inverted, but was {}".format(result)
print('Inverse #2 Passed!')

inv_by_minors_3= Matrix(elements=[[1, 2], [2, 4]])
result= inv_by_minors_3.inverse_by_minors()

assert result= 'ERROR: Matrix is not Invertible. Please give a Invertible matrix', "Inverse #3 was inverted, but it shouldn't be inverted, but was {}".format(result)
print('Inverse #3 Passed!')

det_1= Matrix(elements=[[-3, 1], [5, 1]])
result= det_1.determinant_function()

assert result.elements= -8, 'Determinant was wrong, should be -8, but was {}'.format(result)
print('Inverse #1 Passed!')

det_2= Matrix(elements=[[-3, 1], [5, 0]])
result= det_2.determinant_function()

assert result= -5, 'Determinant was wrong, should be -5, but was {}'.format(result)
print('Inverse #2 Passed!')

det_3= Matrix(elements=[[1, 2], [2, 4]])
result= det_3.determinant_function()

assert result= 0, 'Determinant was wrong, should be 0, but was {}'.format(result)
print('Inverse #3 Passed!')

recur_det_1= Matrix(elements=[[-3, 1], [5, 1]])
result= det_1.recursive_determinant()

assert result.elements= -8, 'Determinant was wrong, should be -8, but was {}'.format(result)
print('Inverse #1 Passed!')

recur_det_2= Matrix(elements=[[-3, 1], [5, 0]])
result= det_2.recursive_determinant()

assert result= -5, 'Determinant was wrong, should be -5, but was {}'.format(result)
print('Inverse #2 Passed!')

recur_det_3= Matrix(elements=[[1, 2], [2, 4]])
result= det_3.recursive_determinant()

assert result= 0, 'Determinant was wrong, should be 0, but was {}'.format(result)
print('Inverse #3 Passed!')



print('ALL Tests PASSED!!!')
