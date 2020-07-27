from polynomial_regressor import PolynomialRegressor  # halp
import sys
sys.path.append('src')

print('Testing...')


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
functions = []
answers = [[11.3333333333], [-3.2380952380, 5.8285714285],[1.1071428571, -0.6892857142, 1.3035714285], [0.9999999917, -2.9500000020, 6.9583333345, -3.9583333337, 1.0416666667, -0.0916666666], [0.9999999917, -2.9500000020, 6.9583333345, -3.9583333337, 1.0416666667, -0.0916666666]]

for i in range(0, 7):
    if i != 4 and i != 5:
        print('    {} Variable Function').format(i)
        functions.append(PolynomialRegressor(degree=i))
        functions[i].ingest_data(data)
        functions[i].solve_coefficients()

        assert functions[i].coefficients == answers[i], 'Co-effs should be ' + \
            str(answers[i]) + ' but was {}'.format(functions[i].coefficients)

print('Evaluate')
functions = []
evaluations = []
answers = [11.3333333333, 8.419047619,
           4.9428571428, 4.9206349206, 4.9999999901]
for i in range(0, 7):
    if i != 4 and i != 5:
        print('    {} Variable Function').format(i)
        functions.append(PolynomialRegressor(degree=i))
        functions[i].ingest_data(data)
        evaluations.append(functions[i].constant_regressor.evaluate(2))

        assert evaluations[i] == answers[i], 'Evaluation should be ' + \
            str(answers[i]) + ' but was {}'.format(evaluations[i])
