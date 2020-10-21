import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

data = {
    'percentile': [95, 95, 92, 85, 80, 85, 95, 87, 99, 95],
    'act_score': [33, 34, 35, 30, 36, 29, 36, 31, 36, 32],
    'extra_curricular': [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    'acceptance': [[1], [0], [1], [0], [1], [0], [1], [0], [1], [0]]
}
df2 = DataFrame(data, column_order=['percentile', 'act_score', 'extra_curricular'])
df2.append_pairwise_interactions()
df2.append_columns({
    'constant': [1 for _ in range(len(data['acceptance']))],
})
logistic_regressor_2 = LogisticRegressor(df2, data['acceptance'], prediction_column='acceptance', max_value = 1, precision = 0.2)
logistic_regressor_2.solve_coefficients()
print('\ncoeffs')
for key, value in logistic_regressor_2.coefficients.items():
    print(key, ':', value)
print('\nevaluation')
for key, value in logistic_regressor_2.evaluate().items():
    print('person', key + 1, ':', value*100, '%', 'chance of getting in to great college')

print(logistic_regressor_2.regression_function({'percentile':95, 'act_score':34, 'extra_curricular':1, 'percentile_act_score':95*34, 'percentile_extra_curricular':95, 'act_score_extra_curricular':34, 'constant':1}, logistic_regressor_2.coefficients))

