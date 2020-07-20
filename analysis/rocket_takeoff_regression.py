import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor

data = [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)]

quadratic = PolynomialRegressor(2)
quadratic.ingest_data(data)
quadratic.solve_coefficients()
print('')
print('Quadratic Error:', quadratic.sum_squared_error())
print('Altitude of rocket at 200 seconds:', quadratic.evaluate(200))
print('')

cubic = PolynomialRegressor(3)
cubic.ingest_data(data)
cubic.solve_coefficients()
print('')
print('Cubic Error:', cubic.sum_squared_error())
print('Altitude of rocket at 200 seconds:', cubic.evaluate(200))
print('')
print("From the code Cubic is better but from Desmos TM, the Quadratic is better i'll tell you in class")
print('')