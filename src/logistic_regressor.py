from matrix_class import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor(LinearRegressor):
    def __init__(self, dataframe, ratings, prediction_column='ratings', max_value = 10):
        super().__init__(dataframe, ratings, prediction_column='ratings', max_value = 10)
        data_dict = {key: value for key, value in dataframe.data_dict.items() if key != prediction_column}
        column_order = [col for col in dataframe.columns if col != prediction_column]
        self.dataframe = DataFrame(data_dict, column_order)
        self.ratings = self.logistic_function([[0.1] if rating[0] == 0 else rating for rating in ratings], max_value)
        self.coefficients = {}
        self.array = dataframe.to_array()

    def apply_coeffs(self, coeff_result):
        for i, key in enumerate(self.dataframe.data_dict.keys()):
            self.coefficients[key] = coeff_result[i]

    def logistic_function(self, ratings, max_value):
        return [[math.log((max_value / rating[0]) - 1)] for rating in ratings]

    def regression_function(self, gathered_inputs, coeffs, max_value = 10):
      return 10 / (1 + math.e ** sum([gathered_inputs[key] * coeffs[key] for key in gathered_inputs]))
