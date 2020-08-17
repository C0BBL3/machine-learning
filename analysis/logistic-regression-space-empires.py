import math
import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor

data = [(0, 0.01), (0, 0.01), (0, 0.05), (10, 0.02), (10, 0.15), (50, 0.12), (50, 0.28), (73, 0.03), (80, 0.10), (115, 0.06), (150, 0.12), (170, 0.30), (175, 0.24),
        (198, 0.26), (212, 0.25), (232, 0.32), (240, 0.45), (381, 0.93), (390, 0.87), (402, 0.95), (450, 0.98), (450, 0.85), (450, 0.95), (460, 0.91), (500, 0.95)]


def logistic_regression_function(x, beta_0, beta_1):  # for testing
    return 1 / (1 + math.e ** (beta_0 + beta_1 * x))


print('poly_regress')
new_data = [(0, 0.01, math.log(1 / 0.01 - 1)), (0, 0.01, math.log(1 / 0.01 - 1)), (0, 0.05, math.log(1 / 0.05 - 1)), (10, 0.02, math.log(1 / 0.02 - 1)),
            (10, 0.15, math.log(1 / 0.15 - 1)),(50, 0.12, math.log(1 / 0.12 - 1)), (50, 0.28, math.log(1 / 0.28 - 1)), (73, 0.03, math.log(1 / 0.03 - 1)), 
            (80, 0.10, math.log(1 / 0.10 - 1)), (115, 0.06, math.log(1 / 0.06 - 1)), (150, 0.12, math.log(1 / 0.12 - 1)), (170, 0.30, math.log(1 / 0.3 - 1)), 
            (175, 0.24, math.log(1 / 0.24 - 1)), (198, 0.26, math.log(1 / 0.26 - 1)), (212, 0.25, math.log(1 / 0.25 - 1)), (232, 0.32, math.log(1 / 0.32 - 1)),
            (240, 0.45, math.log(1 / 0.45 - 1)), (381, 0.93, math.log(1 / 0.93 - 1)), (390, 0.87, math.log(1 / 0.87 - 1)), (402, 0.95, math.log(1 / 0.95 - 1)),
            (450, 0.98, math.log(1 / 0.98 - 1)), (450, 0.85, math.log(1 / - 1)), (450, 0.95, math.log(1 / 0.95 - 1)), (460, 0.91, math.log(1 / 0.91 - 1)), (500, 0.95, math.log(1 / 0.95 - 1))]

poly_regress=PolynomialRegressor()
poly_regress.ingest_data(new_data)
poly_regress.solve_coefficients()
# print('poly_regress coeffs', poly_regress.coefficients)

print('\nprobability of a player who has played 300 hours:', logistic_regression_function(
    300, poly_regress.coefficients[0], poly_regress.coefficients[1]))

print('\nhow long an average player practices:', (math.log(1/0.5 - 1) -
                                                  poly_regress.coefficients[0]) / poly_regress.coefficients[1])
