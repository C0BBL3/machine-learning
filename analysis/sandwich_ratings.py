import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor

#   1 * beta_0 + 0 * beta_1 + 0 * beta_2 = 1
#   1 * beta_0 + 1 * beta_1 + 0 * beta_2 = 2
#   1 * beta_0 + 2 * beta_1 + 0 * beta_2 = 4
#   1 * beta_0 + 4 * beta_1 + 0 * beta_2 = 8
#   1 * beta_0 + 6 * beta_1 + 0 * beta_2 = 9
#   1 * beta_0 + 0 * beta_1 + 2 * beta_2 = 2
#   1 * beta_0 + 0 * beta_1 + 4 * beta_2 = 5
#   1 * beta_0 + 0 * beta_1 + 6 * beta_2 = 7
#   1 * beta_0 + 0 * beta_1 + 8 * beta_2 = 6

#   [[1, 0, 0],                   [[1],
#    [1, 1, 0],                    [2],
#    [1, 2, 0],                    [4],
#    [1, 4, 0],    [[beta_0],      [8],
#    [1, 6, 0],     [beta_1],  =   [9],
#    [1, 0, 2],     [beta_2]]      [2],
#    [1, 0, 4],                    [5],
#    [1, 0, 6],                    [7],
#    [1, 0, 8]]                    [6]]

sandwiches = [[1, 0, 0, 1], [1, 1, 0, 2], [1, 2, 0, 4], [1, 4, 0, 8], [1, 6, 0, 9], [1, 0, 2, 2], [1, 0, 4, 5], [1, 0, 6, 7], [1, 0, 8, 6]]

poly_regress = PolynomialRegressor()
poly_regress.ingest_data(sandwiches)
poly_regress.solve_coefficients()

print('5 roast beef + 5 tbsp of peanut butter =', (poly_regress.coefficients[1] + poly_regress.coefficients[2] * 5 + poly_regress.coefficients[2] * 5))

#rating = 1.1493506493506493 + 1.4220779220779225 * (slices of beef) + 0.7584415584415587 * (tbsp peanut butter)

# Yes, you should belive that 5 roast beef + 5 tbsp of peanut butter has a high rating because computers don't lie and the conputer said it had a high rating


