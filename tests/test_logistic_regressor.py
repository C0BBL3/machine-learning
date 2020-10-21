import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

data_dict = {
    'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
    'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
    'condiments': [[], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly']],
    'ratings': [[1], [1], [4], [0], [4], [8], [1], [0], [5], [0], [9], [0], [0], [0], [0], [0]]
}
df1 = DataFrame(data_dict, column_order=['beef', 'pb', 'condiments'])
df1.create_dummy_variables('condiments')
df1.append_pairwise_interactions()
df1.append_columns({
    'constant': [1 for _ in range(len(data_dict['ratings']))],
})
df1.filter_columns(['constant', 'beef', 'pb', 'mayo', 'jelly', 'beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly'])

print('\nTesting...\n')

logistic_regressor = LogisticRegressor(df1, data_dict['ratings'], prediction_column='ratings')
logistic_regressor.solve_coefficients()
print("    Testing LogisticRegressor's solve_coefficients()")
assert logistic_regressor.coefficients == {'constant': 1.0124843557460994, 'beef': -0.039007927877478754, 'pb': -0.020479441264601272, 'mayo': 1.7482537807332401, 'jelly': -0.39777219344147574, 'beef_pb': 0.14970983216061512, 'beef_mayo': -0.7485491608030758, 'beef_jelly': 0.4682131227124217, 'pb_mayo': 0.3295836866004326, 'pb_jelly': -0.5288267030694539, 'mayo_jelly': 2.644133515347267}, "LogisticRegressor's coeffs are wrong, they should be {'constant': 1.0124843557460994, 'beef': -0.039007927877478754, 'pb': -0.020479441264601272, 'mayo': 1.7482537807332401, 'jelly': -0.39777219344147574, 'beef_pb': 0.14970983216061512, 'beef_mayo': -0.7485491608030758, 'beef_jelly': 0.4682131227124217, 'pb_mayo': 0.3295836866004326, 'pb_jelly': -0.5288267030694539, 'mayo_jelly': 2.644133515347267}, but were " + str(logistic_regressor.coefficients)
print("    LogisticRegressor's solve_coefficients() Passed!!!\n")

print("    Testing LogisticRegressor's predict()")
assert logistic_regressor.predict({'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1}) == 0.023417479576338898, "LogisticRegressor's predict() was wrong, it should be 0.023417479576338898, but was {}".format(logistic_regressor.predict({'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1, }))
print("    LogisticRegressor's predict() #1 Passed!!!\n")

print("    Testing LogisticRegressor's predict()")
assert logistic_regressor.predict({'beef': 0, 'pb': 3, 'mayo': 0, 'jelly': 1}) == 7.375370259327204, "LogisticRegressor's predict() was wrong, it should be 7.375370259327204, but was {}".format(logistic_regressor.predict({'beef': 0, 'pb': 3, 'mayo': 0, 'jelly': 1}))
print("    LogisticRegressor's predict() #2 Passed!!!\n")

print("    Testing LogisticRegressor's predict()")
assert logistic_regressor.predict({'beef': 1, 'pb': 1, 'mayo': 1, 'jelly': 0}) == 0.8076522077650422, "LogisticRegressor's predict() was wrong, it should be 0.8076522077650422, but was {}".format(logistic_regressor.predict({'beef': 1, 'pb': 1, 'mayo': 1, 'jelly': 0}))
print("    LogisticRegressor's predict() #3 Passed!!!\n")

print("    Testing LogisticRegressor's predict()")
assert logistic_regressor.predict({'beef': 6, 'pb': 0, 'mayo': 1, 'jelly': 0}) == 8.770303903540405, "LogisticRegressor's predict() was wrong, it should be 8.770303903540405, but was {}".format(logistic_regressor.predict({'beef': 6, 'pb': 0, 'mayo': 1, 'jelly': 0}))
print("    LogisticRegressor's predict() #4 Passed!!!\n")

print('All Tests Passed!!!')


