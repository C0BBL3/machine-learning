import math
import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor

data = [(10, 0.05), (100, 0.35), (1000, 0.95)]

def logistic_regression_function(x, beta_0, beta_1):  #for testing
    return 1 / (1 + math.e ** (beta_0 + beta_1 * x))

# 0.05 = 1/(1 + e ^ (beta_0 + beta_1 * 10))
# 0.35 = 1/(1 + e ^ (beta_0 + beta_1 * 100))
# 0.95 = 1/(1 + e ^ (beta_0 + beta_1 * 1000))

# beta_0 + beta_1 * 10 = ln(1/0.05 - 1)
# beta_0 + beta_1 * 100 = ln(1/0.35 - 1)
# beta_0 + beta_1 * 1000 = ln(1/0.95 - 1)

# [[1, 10],     [[beta_0],   [[ln(1/0.05 - 1)]
#  [1, 100], *   [beta_1]] =  [ln(1/0.35 - 1)]
#  [1, 1000]]                 [ln(1/0.95 - 1)]]

print('poly_regress')
new_data = [[1, 10, math.log(1/0.05 - 1)], [1, 100, math.log(1/0.35 - 1)], [1, 1000, math.log(1/0.95 - 1)]]

poly_regress = PolynomialRegressor()
poly_regress.ingest_data(new_data)
poly_regress.solve_coefficients()
#print('poly_regress coeffs', poly_regress.coefficients)

print('\nprobability of a player who has played 500 hours:', logistic_regression_function(500, poly_regress.coefficients[0], poly_regress.coefficients[1]))

print('\nhow long an average player practices:', (math.log(1/0.5 - 1) - poly_regress.coefficients[0]) / poly_regress.coefficients[1])
