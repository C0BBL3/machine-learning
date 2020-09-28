from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor(LinearRegressor):
    def __init__(self, dataframe, ratings, prediction_column='ratings', max_value = 10):
        super().__init__(dataframe, ratings, prediction_column='ratings')
        self.max_value = max_value
        self.ratings = [[math.log((max_value / rating[0]) - 1)] for rating in [[0.1] if rating[0] == 0 else rating for rating in ratings]]

    def regression_function(self, gathered_inputs, coeffs):
      return self.max_value / (1 + math.e ** sum([gathered_inputs[key] * coeffs[key] for key in gathered_inputs]))
