from matrix_class import Matrix
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

    def solve_coefficients(self, rounding = False):
        X_matrix = Matrix(elements=self.array)
        #print('X_matrix', X_matrix.elements)
        Y_matrix = Matrix(elements=self.ratings)
        result = (((X_matrix.transpose() @ X_matrix).inverse()) @ X_matrix.transpose()) @ Y_matrix
        self.coeff_result = [arr[0] for arr in result.elements]
        for i, key in enumerate(self.dataframe.data_dict.keys()):
            self.coefficients[key] = round(self.coeff_result[i], 5)
            
    def gather_all_inputs(self, inputs):
        result = inputs
        cartesian = self.dataframe.cartesian_product([inputs.keys(), inputs.keys()])
        for keys in cartesian:
            result['_'.join(keys)] = inputs[keys[0]] * inputs[keys[1]]
        result['constant'] = 1
        return result

    def predict(self, input_dict):
        gathered_inputs = self.gather_all_inputs(input_dict)
        return sum([gathered_inputs[key]*self.coefficients[key] for key in gathered_inputs])
            
