import math
import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
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

data = [[1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0],
 [1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0],
 [1,  0,  0,  1,  1,  0,  0,  0,  0,  0,  1],
 [1,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [1,  5,  0,  1,  0,  0,  5,  0,  0,  0,  0],
 [1,  5,  0,  0,  1,  0,  0,  5,  0,  0,  0],
 [1,  5,  0,  1,  1,  0,  5,  5,  0,  0,  1],
 [1,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0],
 [1,  0,  5,  1,  0,  0,  0,  0,  5,  0,  0],
 [1,  0,  5,  0,  1,  0,  0,  0,  0,  5,  0],
 [1,  0,  5,  1,  1,  0,  0,  0,  5,  5,  1],
 [1,  5,  5,  0,  0, 25,  0,  0,  0,  0,  0],
 [1,  5,  5,  1,  0, 25,  5,  0,  5,  0,  0],
 [1,  5,  5,  0,  1, 25,  0,  5,  0,  5,  0],
 [1,  5,  5,  1,  1, 25,  5,  5,  5,  5,  1]]


def logistic_regression_function(x, betas):  # for testing
    return 1 / (1 + math.e ** sum([beta * x for beta in betas]))

print('poly_regress')
poly_regress = PolynomialRegressor()
poly_regress.ingest_data(data)
poly_regress.solve_coefficients()
print('poly_regress coeffs', poly_regress.coefficients)  # 2.66
print('no ingredients:', poly_regress.coefficients[0])  # 0.59
print('mayo only:', poly_regress.coefficients[3])  # 0.59
print('mayo and jelly:', poly_regress.coefficients[3] + poly_regress.coefficients[4])  # 0.07
print('5 slices beef + mayo:', 5 *
      poly_regress.coefficients[1] + poly_regress.coefficients[3])  # 7.64
print('5 tbsp pb + jelly:', 5 *
      poly_regress.coefficients[1] + poly_regress.coefficients[4])  # 8.94
print('5 slices beef + 5 tbsp pb + mayo + jelly:', 5 *
      poly_regress.coefficients[1] + 5 * poly_regress.coefficients[2] + poly_regress.coefficients[3] + poly_regress.coefficients[4])  # 0.02
