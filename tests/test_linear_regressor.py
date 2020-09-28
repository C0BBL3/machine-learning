import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from dataframe import DataFrame

data_dict_1 = {
    'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
    'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
    'condiments': [[], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly']],
    'ratings': [[1], [1], [4], [0], [4], [8], [1], [0], [5], [0], [9], [0], [0], [0], [0], [0]]
}
df1 = DataFrame(data_dict_1, column_order=['beef', 'pb', 'condiments'])
df1.create_dummy_variables('condiments')
df1.append_pairwise_interactions()
df1.append_columns({
    'constant': [1 for _ in range(len(data_dict_1['ratings']))],
})
df1.filter_columns(['constant', 'beef', 'pb', 'mayo', 'jelly', 'beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly'])

print('\nTesting...\n')

linear_regressor = LinearRegressor(df1, data_dict_1['ratings'], prediction_column='ratings')
linear_regressor.solve_coefficients()
print("    Testing LinearRegressor's solve_coefficients()")
assert linear_regressor.coefficients == {'beef': 0.25, 'pb': 0.4, 'mayo': -1.25, 'jelly': 1.5, 'beef_pb': -0.21, 'beef_mayo': 1.05, 'beef_jelly': -0.85, 'pb_mayo': -0.65, 'pb_jelly': 0.65, 'mayo_jelly': -3.25, 'constant': 2.1875}, "LinearRegressor's coeffs are wrong, they should be {'beef': 0.25, 'pb': 0.4, 'mayo': -1.25, 'jelly': 1.5, 'beef_pb': -0.21, 'beef_mayo': 1.05, 'beef_jelly': -0.85, 'pb_mayo': -0.65, 'pb_jelly': 0.65, 'mayo_jelly': -3.25, 'constant': 2.1875}, but were " + str(linear_regressor.coefficients)
print("    LinearRegressor's solve_coefficients() Passed!!!\n")

print("    Testing LinearRegressor's gather_all_inputs()")
assert linear_regressor.gather_all_inputs({'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1}) == {'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1, 'beef_pb': 25, 'beef_mayo': 5, 'beef_jelly': 5, 'pb_mayo': 5, 'pb_jelly': 5, 'mayo_jelly': 1, 'constant': 1}, "LinearRegressor's gather_all_inputs() was wrong, it should be {'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1, 'beef_pb': 25, 'beef_mayo': 5, 'beef_jelly': 5, 'pb_mayo': 1, 'pb_jelly': 1, 'mayo_jelly': 1, 'constant': 1}, but was " + str(linear_regressor.gather_all_inputs({'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1}))
print("    LinearRegressor's gather_all_inputs() Passed!!!\n")

print("    Testing LinearRegressor's predict()")
assert linear_regressor.predict({'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1}) == -1.8125, "LinearRegressor's predict() was wrong, it should be -1.8125, but was {}".format(linear_regressor.predict({'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1, }))
print("    LinearRegressor's predict() #1 Passed!!!\n")

print("    Testing LinearRegressor's predict()")
assert linear_regressor.predict({'beef': 0, 'pb': 3, 'mayo': 0, 'jelly': 1}) == 6.8375, "LinearRegressor's predict() was wrong, it should be 6.8375, but was {}".format(linear_regressor.predict({'beef': 0, 'pb': 3, 'mayo': 0, 'jelly': 1}))
print("    LinearRegressor's predict() #2 Passed!!!\n")

print("    Testing LinearRegressor's predict()")
assert linear_regressor.predict({'beef': 1, 'pb': 1, 'mayo': 1, 'jelly': 0}) == 1.7775, "LinearRegressor's predict() was wrong, it should be 1.7775, but was {}".format(linear_regressor.predict({'beef': 1, 'pb': 1, 'mayo': 1, 'jelly': 0}))
print("    LinearRegressor's predict() #3 Passed!!!\n")

print("    Testing LinearRegressor's predict()")
assert linear_regressor.predict({'beef': 6, 'pb': 0, 'mayo': 1, 'jelly': 0}) == 8.7375, "LinearRegressor's predict() was wrong, it should be 8.7375, but was {}".format(linear_regressor.predict({'beef': 6, 'pb': 0, 'mayo': 1, 'jelly': 0}))
print("    LinearRegressor's predict() #4 Passed!!!\n")

print('All Tests Passed!!!')
