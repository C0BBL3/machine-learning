from polynomial_regressor import PolynomialRegressor  # halp
import sys
sys.path.append('src')

rint('Testing...')


def single_variable_function(x):
    return (x-1)**2


def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3


def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4


def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6


data = [(0, 1), (1, 2), (2, 5), (3, 10), (4, 20), (5, 30)]

print('Co-effs')
print('    constant Function')
constant_regressor = PolynomialRegressor(degree=0)
constant_regressor.ingest_data(data)
constant_regressor.solve_coefficients()

assert constant_regressor.coefficients == [
    11.3333333333], 'Co-effs should be [11.3333333333] but was {}'.format(constant_regressor.coefficients)

print('    1 Variable Function')
constant_regressor = PolynomialRegressor(degree=1)
constant_regressor.ingest_data(data)
constant_regressor.solve_coefficients()

assert constant_regressor.coefficients == [-3.2380952380,
                                           5.8285714285], 'Co-effs should be [-3.2380952380, 5.8285714285] but was {}'.format(constant_regressor.coefficients)

print('    2 Variable Function')
linear_regressor = PolynomialRegressor(degree=2)
linear_regressor.ingest_data(data)
linear_regressor.solve_coefficients()

assert linear_regressor.coefficients == [1.1071428571, -0.6892857142,
                                         1.3035714285], 'Co-effs should be [1.1071428571, -0.6892857142, 1.3035714285] but was {}'.format(constant_regressor.coefficients)

print('    3 Variable Function')
quadratic_regressor = PolynomialRegressor(degree=3)
quadratic_regressor.ingest_data(data)
quadratic_regressor.solve_coefficients()

assert quadratic_regressor.coefficients == [0.9999999917, -2.9500000020, 6.9583333345, -3.9583333337, 1.0416666667, -
                                            0.0916666666], 'Co-effs should be [0.9999999917, -2.9500000020, 6.9583333345, -3.9583333337, 1.0416666667, -0.0916666666] but was {}'.format(constant_regressor.coefficients)

print('    6 Variable Function')
sixth_degree_regressor = PolynomialRegressor(degree=5)
sixth_degree_regressor.ingest_data(data)
sixth_degree_regressor.solve_coefficients()

assert sixth_degree_regressor.coefficients == [0.9999999917, -2.9500000020, 6.9583333345, -3.9583333337,
                                               1.0416666667, -0.0916666666], 'Co-effs should be [0.9999999917, -2.9500000020, 6.9583333345, -3.9583333337, 1.0416666667, -0.0916666666] but was {}'.format(constant_regressor.coefficients)

print('Evaluate')
print('    constant Function')
constant_regressor = PolynomialRegressor(degree=0)
constant_regressor.ingest_data(data)
evaluate = constant_regressor.evaluate(2)

assert evaluate == 11.3333333333, 'Evaluation should be 11.3333333333 but was {}'.format(
    evaluate)

print('    1 Variable Function')
constant_regressor = PolynomialRegressor(degree=1)
constant_regressor.ingest_data(data)
constant_regressor.evaluate(2)

assert evaluate == 8.419047619, 'Evaluation should be 8.419047619 but was {}'.format(
    evaluate)

print('    2 Variable Function')
linear_regressor = PolynomialRegressor(degree=2)
linear_regressor.ingest_data(data)
constant_regressor.evaluate(2)

assert evaluate == 4.9428571428, 'Evaluation should be 4.9428571428 but was {}'.format(
    evaluate)

print('    3 Variable Function')
quadratic_regressor = PolynomialRegressor(degree=3)
quadratic_regressor.ingest_data(data)
constant_regressor.evaluate(2)

assert evaluate == 4.9206349206, 'Evaluation should be 4.9206349206 but was {}'.format(
    evaluate)

print('    6 Variable Function')
sixth_degree_regressor = PolynomialRegressor(degree=5)
sixth_degree_regressor.ingest_data(data)
constant_regressor.evaluate(2)

assert evaluate == 4.9999999901, 'Evaluation should be 4.9999999901 but was {}'.format(
    evaluate)
