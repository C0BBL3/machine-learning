from polynomial_regressor import PolynomialRegressor
import matplotlib.pyplot as plt
import math
import sys
sys.path.append('src')

data = [(0, 0.01), (0, 0.01), (0, 0.05), (10, 0.02), (10, 0.15), (50, 0.12), (50, 0.28), (73, 0.03), (80, 0.10), (115, 0.06), (150, 0.12), (170, 0.30), (175, 0.24),
        (198, 0.26), (212, 0.25), (232, 0.32), (240, 0.45), (381, 0.93), (390, 0.87), (402, 0.95), (450, 0.98), (450, 0.85), (450, 0.95), (460, 0.91), (500, 0.95)]


def logistic_regression_function(x, beta_0, beta_1):  # for testing
    return 1 / (1 + math.e ** (beta_0 + beta_1 * x))


def new_data_array_generator(data):
    return [(x, math.log(1 / y - 1)) for (x, y) in data]


print('poly_regress')
new_data = new_data_array_generator(data)

poly_regress = PolynomialRegressor()
poly_regress.ingest_data(new_data)
poly_regress.solve_coefficients()
# print('poly_regress coeffs', poly_regress.coefficients)

print('\nprobability of a player who has played 300 hours:', logistic_regression_function(
    300, poly_regress.coefficients[0], poly_regress.coefficients[1]))

plt.style.use('bmh')
plt.plot([logistic_regression_function(x, poly_regress.coefficients[0],
                                       poly_regress.coefficients[1]) for x in range(0, 751)])
plt.legend(['Predicted y-values'])
plt.ylabel('Probability')
plt.xlabel('Number of hours')
plt.title('Predicted probability of winning vs number of hours played')
plt.savefig('plot.png')
plt.show()
