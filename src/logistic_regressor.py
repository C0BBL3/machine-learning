from matrix_class import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor(LinearRegressor):
    def __init__(self, dataframe, ratings, prediction_column='ratings', max_value = 10):
        super().__init__(dataframe, ratings, prediction_column='ratings', max_value = 10)
        self.ratings = [[math.log((max_value / rating[0]) - 1)] for rating in [[0.1] if rating[0] == 0 else rating for rating in ratings]]

    def apply_coeffs(self, coeff_result):
        for i, key in enumerate(self.dataframe.data_dict.keys()):
            self.coefficients[key] = coeff_result[i]

    def regression_function(self, gathered_inputs, coeffs, max_value = 10):
      return max_value / (1 + math.e ** sum([gathered_inputs[key] * coeffs[key] for key in gathered_inputs]))
