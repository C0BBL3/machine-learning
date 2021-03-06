from matrix import Matrix
from dataframe import DataFrame
import math

class LinearRegressor:
    def __init__(self, dataframe, ratings, prediction_column='ratings'):
        data_dict = {key: value for key, value in dataframe.data_dict.items() if key != prediction_column}
        column_order = [col for col in dataframe.columns if col != prediction_column]
        self.dataframe = DataFrame(data_dict, column_order)
        self.ratings = ratings
        self.coefficients = {}
        self.array = dataframe.to_array()

    def solve_coefficients(self, round_coeffs = False, num_decimal = 2):
        X_matrix = Matrix(elements=self.array)
        Y_matrix = Matrix(elements=self.ratings)
        result = (((X_matrix.transpose() @ X_matrix).inverse()) @ X_matrix.transpose()) @ Y_matrix
        coeff_result = [arr[0] for arr in result.elements]
        for i, key in enumerate(self.dataframe.data_dict.keys()):
            if round_coeffs: self.coefficients[key] = round(coeff_result[i], num_decimal)
            else: self.coefficients[key] = coeff_result[i]
            
    def gather_all_inputs(self, inputs):
        result = inputs
        cartesian = self.dataframe.cartesian_product([inputs.keys(), inputs.keys()])
        for keys in cartesian:
            result['_'.join(keys)] = inputs[keys[0]] * inputs[keys[1]]
        result['constant'] = 1
        return result

    def predict(self, input_dict):
        return self.regression_function(self.gather_all_inputs(input_dict), self.coefficients)
    
    def regression_function(self, gathered_inputs, coeffs):
        return sum([gathered_inputs[key] * coeffs[key] for key in gathered_inputs])
            
    def evaluate(self):
        evaluation = {}
        for i in range(0, len(list(self.dataframe.data_dict.values())[0])):
            gathered_inputs = {key:values[i] for key, values in self.dataframe.data_dict.items()}
            evaluation[i] = self.regression_function(gathered_inputs, self.coefficients)