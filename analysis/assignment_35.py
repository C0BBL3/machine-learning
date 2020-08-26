import math
import sys
sys.path.append('src')
from matrix_class import Matrix
'''
data = [[1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 4],
        [1, 0, 0, 1, 1, 0.1],
        [1, 5, 0, 0, 0, 4],
        [1, 5, 0, 1, 0, 8],
        [1, 5, 0, 0, 1, 1],
        [1, 5, 0, 1, 1, 0.1],
        [1, 0, 5, 0, 0, 5],
        [1, 0, 5, 1, 0, 0.1],
        [1, 0, 5, 0, 1, 9],
        [1, 0, 5, 1, 1, 0,1],
        [1, 5, 5, 0, 0, 0,1],
        [1, 5, 5, 1, 0, 0,1],
        [1, 5, 5, 0, 1, 0,1],
        [1, 5, 5, 1, 1, 0,1]]'''

data = [[1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 1],
        [1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0, 1],
        [1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0, 4],
        [1,  0,  0,  1,  1,  0,  0,  0,  0,  0,  1, 0.1],
        [1,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0, 4],
        [1,  5,  0,  1,  0,  0,  5,  0,  0,  0,  0, 8],
        [1,  5,  0,  0,  1,  0,  0,  5,  0,  0,  0, 1],
        [1,  5,  0,  1,  1,  0,  5,  5,  0,  0,  1, 0.1],
        [1,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0, 5],
        [1,  0,  5,  1,  0,  0,  0,  0,  5,  0,  0, 0.1],
        [1,  0,  5,  0,  1,  0,  0,  0,  0,  5,  0, 9],
        [1,  0,  5,  1,  1,  0,  0,  0,  5,  5,  1, 0.1],
        [1,  5,  5,  0,  0, 25,  0,  0,  0,  0,  0, 0.1],
        [1,  5,  5,  1,  0, 25,  5,  0,  5,  0,  0, 0.1],
        [1,  5,  5,  0,  1, 25,  0,  5,  0,  5,  0, 0.1],
        [1,  5,  5,  1,  1, 25,  5,  5,  5,  5,  1, 0.1]]


def logistic_regression_function(x, betas):  # for testing
      return 10 / (1 + math.e ** sum([beta * x for beta in betas]))

def new_data_array_generator(data):
    return [(x, math.log(1 / y - 1)) for (x, y) in data]


def solve_coefficients(data):
      X_data = []
      Y_data = []
      for arr in data:
            X_data.append(arr[:-1])
            Y_data.append([math.log((10 / arr[-1]) - 1)])
      X_matrix = Matrix(elements=X_data)
      #print('\nX_matrix.elements', X_matrix.elements,)
      Y_matrix = Matrix(elements=Y_data)
      #print('Y_matrix.elements', Y_matrix.elements)
      X_transpose = X_matrix.transpose()  # xT
      #print('xT', X_transpose.elements)
      X_transpose_times_X = X_transpose @ X_matrix  # xT * x
      #print('(xT * x)', X_transpose_times_X.elements)
      X_transpose_times_X_inverse = X_transpose_times_X.inverse()
      #print('(xT * x)^-1', X_transpose_times_X_inverse.elements)
      X_transpose_times_X_inverse_times_X_transpose = X_transpose_times_X_inverse @ X_transpose
      #print('(xT * x)^-1 * xT', X_transpose_times_X_inverse_times_X_transpose.elements)
      result = X_transpose_times_X_inverse_times_X_transpose @ Y_matrix
      # (xT * x)^-1 * xT * y
      #print('(xT * x)^-1 * xT * y', result.elements, '\n')
      coefficients = []
      for results in result.elements:
            if results != result.elements:
                  coefficients.append(results[0])

      print('Coeffs', coefficients, '\n')
      return coefficients

#print('poly_regress')
coefficients = solve_coefficients(data)
print('poly_regress coeffs', coefficients)  # 2.66
print('no ingredients:', coefficients[0])  # 0.59
print('mayo only:', coefficients[0] + coefficients[3])  # 0.59
print('mayo and jelly:', coefficients[0] + coefficients[3] + coefficients[4])  # 0.07
print('5 slices beef + mayo:', coefficients[0] + 5 *
      coefficients[1] + coefficients[3])  # 7.64
print('5 tbsp pb + jelly:', coefficients[0] + 5 *
      coefficients[1] + coefficients[4])  # 8.94
print('5 slices beef + 5 tbsp pb + mayo + jelly:', coefficients[0] + 5 *
      coefficients[1] + 5 * coefficients[2] + coefficients[3] + coefficients[4])  # 0.02
