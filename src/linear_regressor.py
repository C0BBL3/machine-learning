from matrix_class import Matrix
from dataframe import DataFrame
import math

class LinearRegressor:
    def __init__(self, dataframe, ratings, prediction_column='ratings', max_value = 10):
        data_dict = {key: value for key, value in dataframe.data_dict.items() if key != prediction_column}
        column_order = [col for col in dataframe.columns if col != prediction_column]
        self.dataframe = DataFrame(data_dict, column_order)
        self.ratings = ratings
        self.coefficients = {}
        self.array = dataframe.to_array()
        self.max_value = max_value

    def solve_coefficients(self):
        X_matrix = Matrix(elements=self.array)
        #print('X_matrix', X_matrix.elements)
        Y_matrix = Matrix(elements=self.ratings)
        result = (((X_matrix.transpose() @ X_matrix).inverse()) @ X_matrix.transpose()) @ Y_matrix
        self.apply_coeffs([arr[0] for arr in result.elements])

    def apply_coeffs(self, coeff_result):
        for i, key in enumerate(self.dataframe.data_dict.keys()):
            self.coefficients[key] = coeff_result[i]
            
    def gather_all_inputs(self, inputs):
        result = inputs
        cartesian = self.dataframe.cartesian_product([inputs.keys(), inputs.keys()])
        for keys in cartesian:
            result['_'.join(keys)] = inputs[keys[0]] * inputs[keys[1]]
        result['constant'] = 1
        return result

    def predict(self, input_dict):
        return self.regression_function(self.gather_all_inputs(input_dict), self.coefficients)
    
    def regression_function(self, gathered_inputs, coeffs, max_value = 10):
        return sum([gathered_inputs[key] * coeffs[key] for key in gathered_inputs])
            
