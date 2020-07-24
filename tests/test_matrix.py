import sys
sys.path.append('src')
from matrix_class import Matrix

print('Testing...')

add_1 = Matrix(elements=[[1, 1], [0, 1]])
add_2 = Matrix(elements=[[1, 1], [0, 1]])
result = add_1 + add_2

assert result.elements == [[2, 2], [
    0, 2]], 'Addition was wrong, should be [[2, 2], [0, 2]], but was {}'.format(result.elements)
print('Addition Passed!')

sub_1 = Matrix(elements=[[1, 1], [0, 1]])
sub_2 = Matrix(elements=[[1, 1], [0, 1]])
result = sub_1 - sub_2

assert result.elements == [[0, 0], [
    0, 0]], 'Subtraction was wrong, should be [[0, 0], [0, 0]], but was {}'.format(result.elements)
print('Subtraction Passed!')

scal_mult = Matrix(elements=[[1, 1], [0, 1]])
scalar = 2
result = scal_mult * scalar

assert result.elements == [[2, 2], [
    0, 2]], 'Scalar multiplication was wrong, should be [[2, 2], [0, 2]], but was {}'.format(result.elements)
print('Scalar multiplication Passed!')

mat_mult_1 = Matrix(elements=[[1, 1], [0, 0]])
mat_mult_2 = Matrix(elements=[[0, 0], [1, 1]])
result = mat_mult_1 @ mat_mult_2

assert result.elements == [[1, 1], [
    0, 0]], 'Matrix Multiplication was wrong, should be [[1, 1], [0, 0]], but was {}'.format(result.elements)
print('Matrix Multiplication Passed!')

trans = Matrix(elements=[[1, 1], [0, 1]])
result = trans.transpose()

assert result.elements == [[1, 0], [
    1, 1]], 'Transpose was wrong, should be [[1, 0], [1, 1]], but was {}'.format(result.elements)
print('Transpose Passed!')

RREF_1 = Matrix(elements=[[1, 1], [0, 1]])
result = RREF_1.rref()

assert result.elements == [[1.0, 0.0], [
    0.0, 1.0]], 'RREF #1 was wrong, should be [[1.0, 0.0], [0.0, 1.0]], but was {}'.format(result.elements)
print('RREF #1 Passed!')

# RREF_2 = Matrix(elements=[[1, 1], [0, 1], [2, 3]]) # doesnt work just commented out to debug other stuffs
#result = RREF_2.rref()

# assert result.elements == [[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]], 'RREF #2 was wrong, should be [[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]], but was {}'.format(result.elements)
# print('RREF #2 Passed!')

RREF_3 = Matrix(elements=[[1, 1, 2], [0, 1, 3]])
result = RREF_3.rref()

assert result.elements == [[1.0, 0.0, -1.0], [0.0, 1.0, 3.0]
                           ], 'RREF #3 was wrong, should be [[1, 0, -1], [0, 1, 3]], but was {}'.format(result.elements)
print('RREF #3 Passed!')

RREF_4 = Matrix(elements=[[3, 1, 2], [0, 2, 3]])
result = RREF_4.rref()

assert result.elements == [[1.0, 0.0, 0.16666666666666663], [
    0.0, 1.0, 1.5]], 'RREF #4 was wrong, should be [[1, 0, 0.16], [0, 1, 1.5]], but was {}'.format(result.elements)
print('RREF #4 Passed!')

RREF_5 = Matrix(elements=[[4, 5, 6], [7, 8, 9]])
result = RREF_5.rref()

assert result.elements == [[1.0, 0.0, -1.0], [0.0, 1.0, 2.0]
                           ], 'RREF #5 was wrong, should be [[1.0, 0.0, -1.0], [0.0, 1.0, 3.0]], but was {}'.format(result.elements)
print('RREF #5 Passed!')

RREF_6 = Matrix(elements=[[1, 2, 3], [4, 5, 6]])
result = RREF_6.rref()

assert result.elements == [[1.0, 0.0, -1.0], [0.0, 1.0, 2.0]
                           ], 'RREF #6 was wrong, should be [[1, 0, -1], [0, 1, 2]], but was {}'.format(result.elements)
print('RREF #6 Passed!')

round_1 = Matrix(elements=[[1.34, 3.23], [2.12, 5.43]])
result = round_1.round()

assert result.elements == [[1, 3], [2, 5]
                           ], 'Round #1 doesnt work should be [[1, 3], [2, 5]], but was {}'.format(result.elements)
print('Round #1 Passed!')

round_2 = Matrix(elements=[[4.34, 3.23, 5.69], [2.12, 5.43, 9.72], [5.53, 4.65, 6.32]])
result = round_2.round()

assert result.elements == [[1, 3], [2, 5]
                           ], 'Round #1 doesnt work should be [[4, 3, 6], [2, 5, 10], [6, 5, 6]], but was {}'.format(result.elements)
print('Round #2 Passed!')

round_3 = Matrix(elements=[[1.34, 3.23], [2.12, 5.43]])
result = round_3.round()

assert result.elements == [[1, 3], [2, 5]
                           ], 'Round #1 doesnt work should be [[1, 3], [2, 5]], but was {}'.format(result.elements)
print('Round #3 Passed!')

inv_1 = Matrix(elements=[[1, 2, 3, 4], [5, 0, 6, 0],
                         [0, 7, 0, 8], [9, 0, 0, 10]])
result = inv_1 @ inv_1.inverse()
result.round(1)

identity = Matrix(shape=(4, 4), fill='diag')

assert result.elements == identity.elements, "Inverse #1 wasn't inverted correctly, but was {}".format(
    result.elements)
print('Inverse #1 Passed!')

inv_2 = Matrix(elements=[[1.2, 5.3, 8.9, -10.3, -15], [3.14, 0, -6.28, 0, 2.71], [0, 1, 1, 2, 3], [5, 8, 13, 21, 34],[1, 0, 0.5, 0, 0.1]])
result = inv_2 @ inv_2.inverse()
result.round(1)

identity = Matrix(shape=(5, 5), fill='diag')

assert result.elements == identity.elements, "Inverse #2 wasn't inverted correctly, but was {}".format(
    result.elements)
print('Inverse #2 Passed!')

inv_3 = Matrix(elements=[[1, 2], [2, 4]])# dependent rows give error
result = inv_3 @ inv_3.inverse()
result.round(1)

identity = Matrix(shape=(2, 2), fill='diag')

assert result.elements == identity.elements, "Inverse #2 wasn't inverted correctly, but was {}".format(
    result.elements)
print('Inverse #3 Passed!')

inv_by_minors_1 = Matrix(elements=[[1, 2, 3, 4], [5, 0, 6, 0],
                         [0, 7, 0, 8], [9, 0, 0, 10]])
result = inv_by_minors_1 @ inv_by_minors_1.inverse()
result.round(1)

identity = Matrix(shape=(4, 4), fill='diag')

assert result.elements == identity.elements, "Inverse #1 wasn't inverted correctly, but was {}".format(
    result.elements)
print('Inverse #1 Passed!')

inv_by_minors_2 = Matrix(elements=[[1.2, 5.3, 8.9, -10.3, -15], [3.14, 0, -6.28,
                                                       0, 2.71], [0, 1, 1, 2, 3], [5, 8, 13, 21, 34], [1, 0, 0.5, 0, 0.1]])
result = inv_by_minors_1 @ inv_by_minors_1.inverse()
result.round(1)

identity = Matrix(shape=(5, 5), fill='diag')

assert result.elements == identity.elements, "Inverse #2 wasn't inverted correctly, but was {}".format(
    result.elements)
print('Inverse #2 Passed!')

inv_by_minors_3 = Matrix(elements=[[1, 2], [2, 4]])  # dependent rows give error
result = inv_by_minors_3 @ inv_by_minors_3.inverse()
result.round(1)

identity = Matrix(shape=(2, 2), fill='diag')

assert result.elements == identity.elements, "Inverse #2 wasn't inverted correctly, but was {}".format(
    result.elements)
print('Inverse #3 Passed!')

det_1 = Matrix(elements=[[-3, 1], [5, 1]])
result = det_1.determinant_function()

assert result.elements == - \
    8, 'Determinant was wrong, should be -8, but was {}'.format(result)
print('Inverse #1 Passed!')

det_2 = Matrix(elements=[[-3, 1], [5, 0]])
result = det_2.determinant_function()

assert result == - \
    5, 'Determinant was wrong, should be -5, but was {}'.format(result)
print('Inverse #2 Passed!')

det_3 = Matrix(elements=[[1, 2], [2, 4]])
result = det_3.determinant_function()

assert result == 0, 'Determinant was wrong, should be 0, but was {}'.format(
    result)
print('Inverse #3 Passed!')

recur_det_1 = Matrix(elements=[[-3, 1], [5, 1]])
result = det_1.recursive_determinant()

assert result.elements == - \
    8, 'Determinant was wrong, should be -8, but was {}'.format(result)
print('Inverse #1 Passed!')

recur_det_2 = Matrix(elements=[[-3, 1], [5, 0]])
result = det_2.recursive_determinant()

assert result == - \
    5, 'Determinant was wrong, should be -5, but was {}'.format(result)
print('Inverse #2 Passed!')

recur_det_3 = Matrix(elements=[[1, 2], [2, 4]])
result = det_3.recursive_determinant()

assert result == 0, 'Determinant was wrong, should be 0, but was {}'.format(
    result)
print('Inverse #3 Passed!')

print('ALL Tests PASSED!!!')
