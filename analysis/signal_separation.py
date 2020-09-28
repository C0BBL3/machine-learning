import math
import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from dataframe import DataFrame

print('')
data_dict_1 = {
    'constant': [1 for _ in range(0,25)],
    'ratings': [[4.0], [8.9], [17.2], [28.3], [41.6], [56.5], [72.4], [88.7], [104.8], [120.1], [134.0], [145.9], [155.2], [161.3], [163.6], [161.5], [154.4], [141.7], [122.8], [97.1], [64.0], [22.9], [-26.9], [-85.7], [-154.4]],
    'x': [x/5 for x in range(0,25)]
    
}
df1 = DataFrame(data_dict_1, column_order=['constant', 'x'])
df1.append_columns({
    'x^2': [x ** 2 for x in data_dict_1['x']],
    'x^3': [x ** 3 for x in data_dict_1['x']],
})
data_dict_2 = {
    'constant': [1 for _ in range(0,25)],
    'x': [x/5 for x in range(0,25)],
    'ratings': [[7.0], [5.6], [3.56], [1.23], [-1.03], [-2.89], [-4.06], [-4.39], [-3.88], [-2.64], [-0.92], [0.95], [2.63], [3.79], [4.22], [3.8], [2.56], [0.68], [-1.58], [-3.84], [-5.76], [-7.01], [-7.38], [-6.76], [-5.22]],    
}
df2 = DataFrame(data_dict_2, column_order=[])
df2.append_columns({
    'a': [math.sin(x) for x in data_dict_2['x']],
    'b': [math.cos(x) for x in data_dict_2['x']],
    'c': [math.sin(2 * x) for x in data_dict_2['x']],
    'd': [math.cos(2 * x) for x in data_dict_2['x']],
})

linear_regressor_1 = LinearRegressor(df1, data_dict_1['ratings'], prediction_column='ratings')
linear_regressor_1.solve_coefficients(round_ = True)
assert  linear_regressor_1.coefficients == {'constant': 4.0, 'x': 15.0, 'x^2': 50.0, 'x^3': -12.5}, "Exponential Coeffs are wrong, they should be {'constant': 4.0, 'x': 15.0, 'x^2': 50.0, 'x^3': -12.5}, but were " + str(linear_regressor_1.coefficients)
print("Exponential Coeffs:", linear_regressor_1.coefficients)

linear_regressor_2 = LinearRegressor(df2, data_dict_2['ratings'], prediction_column='ratings')
linear_regressor_2.solve_coefficients(round_ = True)
assert  linear_regressor_2.coefficients == {'a': 1.0, 'b': 2.0, 'c': -3.0, 'd': 5.0}, "Sine & Cosine Coeffs are wrong, they should be {'a': 1.0, 'b': 2.0, 'c': -3.0, 'd': 5.0}, but were " + str(linear_regressor_2.coefficients)
print("Sine & Cosine Coeffs", linear_regressor_2.coefficients)