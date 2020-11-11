import random
import sys
sys.path.append('src')
from deprecated_polynomial_regressor import PolynomialRegressor

training_data_array, testing_data_array = [], [] 
for x in [x / 10 for x in range(1, 101)]:
    if random.randint(0,10) < 3: training_data_array.append([x, 3+0.5*x**2+(-5 + 10*random.random())]) 
    else: testing_data_array.append([x, 3+0.5*x**2+(-5 + 10*random.random())]) 
#A: le data sets ^^^

#B: I think the quadratic or maybe the cubic regressors will be the most accurate because the linear regressor would underfit and the higher powers would overfit.

linear_regressor = PolynomialRegressor(degree = 1)
linear_regressor.ingest_data(training_data_array)
linear_regressor.solve_coefficients()
print('Linear Regressor RSS: ', linear_regressor.rss(testing_data_array))

quadratic_regressor = PolynomialRegressor(degree = 2)
quadratic_regressor.ingest_data(training_data_array)
quadratic_regressor.solve_coefficients()
print('Quadratic Regressor RSS: ', quadratic_regressor.rss(testing_data_array))

cubic_regressor = PolynomialRegressor(degree = 3)
cubic_regressor.ingest_data(training_data_array)
cubic_regressor.solve_coefficients()
print('Cubic Regressor RSS: ', cubic_regressor.rss(testing_data_array))

quartic_regressor = PolynomialRegressor(degree = 4)
quartic_regressor.ingest_data(training_data_array)
quartic_regressor.solve_coefficients()
print('Quartic Regressor RSS: ', quartic_regressor.rss(testing_data_array))

quintic_regressor = PolynomialRegressor(degree = 5)
quintic_regressor.ingest_data(training_data_array)
quintic_regressor.solve_coefficients()
print('Quintic Regressor RSS: ', quintic_regressor.rss(testing_data_array))
#C,D: ^^^^^ The Cubic Regressor consitantly has the lowest error by a mile, with the Linear, Quadratic, and Quartic regressors trading blows for runner up with the Quarticc regressor lagging a bit behind the Linear and Quadratic regressors. Finally the Quintic Regressor with consitantly the highest. I believe that this data makes sense because Quintic Regressor always overfits, with the Quartic overfitting but not nearly as much, with the Cubic regressor having the closest fit to the true fit line, and the Quadratic and the Linear regressors underfitting just a bit with the Linear regressor underfitting a bit more than the Quadratic regressor.
