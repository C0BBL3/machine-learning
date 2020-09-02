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
      return 10 / (1 + math.e ** sum([betas[i] * x[i] for i in range(0,len(x))]))

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
print('No ingredients:', logistic_regression_function([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [coeff for coeff in coefficients]))  # 2.66
assert logistic_regression_function([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [coeff for coeff in coefficients]) == 2.6649393988782637, 'logistic_regression_function was not right, it should be 2.66ish but was {}'.format(logistic_regression_function([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [coeff for coeff in coefficients]))
print('mayo only:', logistic_regression_function([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [coeff for coeff in coefficients]))  # 0.59
assert logistic_regression_function([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [coeff for coeff in coefficients]) == 0.5948305763144304, 'logistic_regression_function was not right, it should be 0.59ish but was {}'.format(logistic_regression_function([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [coeff for coeff in coefficients]))
print('mayo and jelly:', logistic_regression_function([1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], [coeff for coeff in coefficients]))  # 0.07
assert logistic_regression_function([1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], [coeff for coeff in coefficients]) == 0.06645818238664847, 'logistic_regression_function was not right, it should be 0.07ish but was {}'.format(logistic_regression_function([1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], [coeff for coeff in coefficients]))
print('5 slices beef + mayo:', logistic_regression_function([1, 5, 0, 1, 0, 0, 5, 0, 0, 0, 0], [coeff for coeff in coefficients]))  # 7.64
assert logistic_regression_function([1, 5, 0, 1, 0, 0, 5, 0, 0, 0, 0], [coeff for coeff in coefficients]) == 7.64416486422044, 'logistic_regression_function was not right, it should be 7.64ish but was {}'.format(logistic_regression_function([1, 5, 0, 1, 0, 0, 5, 0, 0, 0, 0], [coeff for coeff in coefficients]))
print('5 tbsp pb + jelly:', logistic_regression_function([1, 0, 5, 0, 1, 0, 0, 0, 0, 5, 0], [coeff for coeff in coefficients]))  # 8.94\
assert logistic_regression_function([1, 0, 5, 0, 1, 0, 0, 0, 0, 5, 0], [coeff for coeff in coefficients]) == 8.939575266972463, 'logistic_regression_function was not right, it should be 8.94ish but was {}'.format(logistic_regression_function([1, 0, 5, 0, 1, 0, 0, 0, 0, 5, 0], [coeff for coeff in coefficients]))
print('5 slices beef + 5 tbsp pb + mayo + jelly:', logistic_regression_function([1, 5, 5, 1, 1, 25, 5, 5, 5, 5, 1], [coeff for coeff in coefficients]))  # 0.02
assert logistic_regression_function([1, 5, 5, 1, 1, 25, 5, 5, 5, 5, 1], [coeff for coeff in coefficients]) == 0.023417479576338898, 'logistic_regression_function was not right, it should be 0.02ish but was {}'.format(logistic_regression_function([1, 5, 5, 1, 1, 25, 5, 5, 5, 5, 1], [coeff for coeff in coefficients]))